import os
from datetime import datetime

media_files_directory = "../media/"
allowed_extensions = [".txt", ".jpg", ".mp4", ".wav"]
hidden_files_prefixes = (".", "_", "Makefile")


def read_dir(directory, hidden_files_prefixes):
    """
    returns a list of all non-hidden files in a given directory
    :param directory: string
    :param hidden_files_prefixes: tuple of strings
    :return: list
    """
    files = os.listdir(directory)
    files = [x for x in files if not x.startswith(hidden_files_prefixes)]
    return files


def sane_file_extensions(files, extensions):
    """
    returns False for lists that contain file names with other extensions than given.
    :param files: list of file name strings
    :param extensions: list of extensions strings e.g. [".jpg", ".txt"]
    """
    for file in files:
        filename, extension = os.path.splitext(file)
        if extension not in extensions:
            print("Invalid extension: " + file)
            return False
    return True


def sane_file_naming_schema(files):
    """
    returns False for lists that contain file names, that don't match the scheme.
    File names mustn't start with underscore, that leads to a negative result.
    Time is optional, just omit _HH-MM-SS

    Scheme:  YYYY-MM-DD_HH-MM-SS_title.extension
    Example: 2019-05-27_20-44-16_Sonnenuntergang in Petershausen.jpg

    :param files: list of file name strings
    """
    for file in files:
        filename, extension = os.path.splitext(file)
        parts = filename.split("_")
        if len(parts) == 1:
            # not a single underscore
            return False
        if len(parts) >= 2:
            # good conditions for the simple scheme
            try:
                test = datetime.strptime(parts[0], "%Y-%m-%d")  # valid date
            except ValueError:
                print("Invalid scheme:   ", file)
                return False
        if len(parts) >= 3:
            try:
                test = datetime.strptime(parts[1], "%H-%M-%S")
            except ValueError:
                print("Invalid scheme:   ", file)
                return False
    return True


def write_json(files, json_file):
    """
    Writes a *.json when given a sane list of file names
    :param files: list of sane file name strings
    :param json_file_name: string
    :return: True if file was written
    """
    pass


class Media(object):
    def __init__(self, **kwargs):
        # test if there is a date, and check if it is sane
        try:
            kwargs["date"]
            try:
                self.date = datetime.strptime(kwargs["date"], "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date!", kwargs["date"])
                raise
        except KeyError:
            print("Missing date!")
            raise

        # test if a given time is sane
        if kwargs.get("time") is not None:
            try:
                self.time = datetime.strptime(kwargs["time"], "%H-%M-%S")
            except ValueError:
                print("Invalid time! ", kwargs["time"])
                raise

        # test if a title is set
        try:
            self.title = kwargs["title"]
        except KeyError:
            print("Missing title!")
            raise


def main():
    files = read_dir(media_files_directory, hidden_files_prefixes)
    extension_test = sane_file_extensions(files, allowed_extensions)
    schema_test = sane_file_naming_schema(files)
    if extension_test and schema_test:
        print("Media directory is clean!")
        media_files_objects = []
        media_files_objects.append(Media(date="2019-06-02", time="15-16-02", title="Tagebuch"))
        print(media_files_objects[0].date)


if __name__ == "__main__":
    main()
