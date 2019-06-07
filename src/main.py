#!/usr/local/bin/python3

"""
This script tests the media source directory if it is "valid" and writes a sane JSON
"""

import codecs
import json
import os
from datetime import datetime

from PIL import Image

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
    files.sort(reverse=True)
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
    returns json for given file data if given file names match the scheme,
    otherwise returns False.
    File names mustn't start with underscore, that leads to False.
    Time is optional, just omit _HH-MM-SS

    Scheme:  YYYY-MM-DD_HH-MM-SS_title.extension
    Example: 2019-05-27_20-44-16_Sonnenuntergang in Petershausen.jpg

    :param files: list of file name strings
    """
    json = {}
    json["events"] = []
    for file in files:
        file_data = {}
        filename, extension = os.path.splitext(file)
        if extension == ".jpg":
            width, height = read_image_size(media_files_directory + file)
            file_data['width'] = width
            file_data['height'] = height
        parts = filename.split("_")
        if len(parts) == 1:
            # not a single field
            return False
        if len(parts) > 1:
            # see if first field is a valid date
            try:
                file_data["datetime"] = str(datetime.strptime(parts[0], "%Y-%m-%d"))
            except ValueError:
                print("Invalid scheme:   ", file)
                return False
        if len(parts) == 2:
            # we have just to fields so the second is the title
            file_data["title"] = parts[1]
        if len(parts) > 2:
            # three fields, so first and second field have to be date and time, third the title
            try:
                file_data["datetime"] = str(datetime.strptime(str(parts[0] + "_" + parts[1]), "%Y-%m-%d_%H-%M-%S"))
                file_data["title"] = parts[2]
            except ValueError:
                return False
        file_data["extension"] = extension.strip(".")
        file_data["url"] = file
        json["events"].append(file_data)

    return json


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
                self.time = datetime.strptime(kwargs["time"], "%H-%M-%S").time()
            except ValueError:
                print("Invalid time! ", kwargs["time"])
                raise

        # test if a title is set
        try:
            self.title = kwargs["title"]
        except KeyError:
            print("Missing title!")
            raise


def write_json(data, file_name):
    """
    Serializes and writes an object to a json file
    :param data: list of dictionaries
    :param file_name: string
    :return: True if file was written
    """
    try:
        json.dump(data, codecs.open(file_name, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)
        return True
    except TypeError:
        print("No valid JSON data!")
        raise
    except IOError:
        print("Could not write file to disk!")
        raise


def read_json(file_name):
    """
    Reads json data from a file
    :param file_name: string
    :return: json object
    """
    try:
        with open(file_name, "rt") as input_file:
            return json.loads(input_file.read())
    except TypeError:
        print("No valid JSON data!")
        raise
    except IOError:
        print("Could not read file from disk!")
        raise


def read_image_size(file_name):
    """
    Reads width and height from a file
    :param file_name: String
    :return: width, height
    """
    return Image.open(file_name).size


def main():
    files = read_dir(media_files_directory, hidden_files_prefixes)
    valid_extensions = sane_file_extensions(files, allowed_extensions)
    valid_schema = sane_file_naming_schema(files)
    if valid_extensions and valid_schema:
        print("Media directory is clean!")
        write_json(valid_schema, "../dist/media.json")


if __name__ == "__main__":
    main()
