#!/usr/local/bin/python3

"""
This script converts media data of a given dir for web use.
"""

import os

from src.main import read_dir


def is_done(file, extension, output_dir):
    had_to_be_done_files = []
    if extension == ".jpg":
        had_to_be_done_files.append(file)
    are_done_files = []
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


def create(file, extension, output_dir):
    print(
        "convert -strip -interlace JPEG -sampling-factor 4:2:0 -define jpeg:dct-method=float -geometry 400x -sharpen 0x0.9 -quality 90 input.jpg input-400x.jpg")


def convert_media(input_dir, output_dir):
    try:
        input_files = read_dir(input_dir, (".", "_"))
        output_files = read_dir(input_dir, (".", "_"))
    except IOError:
        print("Could not read from disk!")
        raise
    for file in input_files:
        filename, extension = os.path.splitext(file)
        if extension == ".jpg":
            if not is_done(file, extension, output_dir):
                create(file, extension, output_dir)


def main():
    # if len(sys.argv) < 3:
    #     print("This script converts media data from a given dir to a given dir for web use.")
    #     print("Usage: ./convert_dir input_dir output_dir")
    #     return False
    # convert_media(sys.argv[1], sys.argv[2])

    convert_media("/Users/jibazee/Desktop/media", "/Users/jibazee/Desktop/dist")


if __name__ == "__main__":
    main()
