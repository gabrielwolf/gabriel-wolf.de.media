import os
from datetime import datetime

media_files_directory = '../media'


def dir_sane_file_extensions(directory, extensions):
    """
    returns False for directories that contain other files, that have other extensions than given.
    Dotfiles are not of concern.
    """
    files = os.listdir(directory)
    for file in files:
        if not file.startswith('.'):
            filename, extension = os.path.splitext(file)
            if extension not in extensions:
                return False
    return True


def dir_sane_file_naming_schema(directory):
    """
    returns False for directories that contain files, that don't match a scheme.
    Files beginning with _ are being ignored. They are considered to be temporarily disabled.

    Scheme:  YYYY-MM-DD_HH-MM-SS_title.extension
    Example: 2019-05-27_20-44-16_Sonnenuntergang in Petershausen.jpg

    Time is optional.
    """
    files = os.listdir(directory)
    for file in files:
        if not file.startswith('.') and not file.startswith('_'):
            filename, extension = os.path.splitext(file)
            parts = filename.split('_')
            if len(parts) == 1:
                return False
            if len(parts) == 2:
                try:
                    test = datetime.strptime(parts[0], '%Y-%m-%d')
                except ValueError:
                    print("Scheme not valid for file: ", file)
                    return False
            if len(parts) == 3:
                try:
                    test = datetime.strptime(parts[1], '%H-%M-%S')
                except ValueError:
                    print("Scheme not valid for file: ", file)
                    return False
    return True


def main():
    dir_sane_file_extensions(media_files_directory, ['.txt', '.jpg', '.mp4', '.wav'])
    dir_sane_file_naming_schema(media_files_directory)


if __name__ == 'main':
    main()
