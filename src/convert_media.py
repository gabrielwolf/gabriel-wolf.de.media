#!/usr/local/bin/python3

"""
This script converts media data of a given dir for web use.
"""

import os

from src.main import read_dir


def get_output_file_names(file, extension):
    output = []
    if extension == ".jpg":
        output.append(file.replace(".jpg", "-preload.jpg"))
        output.append(file.replace(".jpg", "-400w.jpg"))
        output.append(file.replace(".jpg", "-600w.jpg"))
        output.append(file.replace(".jpg", "-800w.jpg"))
        output.append(file.replace(".jpg", "-1000w.jpg"))
        output.append(file.replace(".jpg", "-1500w.jpg"))
        output.append(file.replace(".jpg", "-2000w.jpg"))
        output.append(file.replace(".jpg", "-2500w.jpg"))
    return output


def is_done(file, extension, output_dir):
    had_to_be_done_files = []
    are_done_files = []

    had_to_be_done_files.append(get_output_file_names(file, extension))

    try:
        output_files = read_dir(output_dir, (".", "_"))
        for output_file in output_files:
            if output_file in had_to_be_done_files:
                are_done_files.append(output_file)
    except IOError:
        print("Could not read from disk!")
        raise

    had_to_be_done_files.sort()
    are_done_files.sort()

    if had_to_be_done_files == are_done_files:
        return True

    print(file + " is not (yet) web ready!")
    return False


def create(file, extension, input_dir, output_dir):
    files_to_be_done = get_output_file_names(file, extension)
    for file_to_be_done in files_to_be_done:
        print("convert %s/%s %s/%s" % (input_dir, file, output_dir, file_to_be_done))


def convert_media(input_dir, output_dir):
    try:
        input_files = read_dir(input_dir, (".", "_"))
        output_files = read_dir(output_dir, (".", "_"))
    except IOError:
        print("Could not read from disk!")
        raise
    for file in input_files:
        filename, extension = os.path.splitext(file)
        if extension == ".jpg":
            if not is_done(file, extension, output_dir):
                create(file, extension, input_dir, output_dir)


def main():
    # if len(sys.argv) < 3:
    #     print("This script converts media data from a given dir to a given dir for web use.")
    #     print("Usage: ./convert_dir input_dir output_dir")
    #     return False
    # convert_media(sys.argv[1], sys.argv[2])

    convert_media("/Users/jibazee/Desktop/media", "/Users/jibazee/Desktop/dist")


if __name__ == "__main__":
    main()
