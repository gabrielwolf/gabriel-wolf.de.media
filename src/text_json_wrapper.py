#!/usr/local/bin/python3

"""
This script reads a given text file and wraps it into a JSON container.
This container is then written to disk.
"""
import codecs
import json
import sys


def convert_txt_to_html_to_json(input_file, output_file):
    json_container = dict()
    with open(input_file, "rt") as file:
        data = file.read().replace("\n", "<br>").replace("    ", "&nbsp;&nbsp;&nbsp;&nbsp;").replace("   ",
                                                                                                     "&nbsp;&nbsp;&nbsp;")
        json_container['text'] = data
        try:
            json.dump(json_container, codecs.open(output_file, 'w', encoding='utf-8'), separators=(',', ':'),
                      sort_keys=True, indent=4)
            return True
        except TypeError:
            print("No valid JSON data!")
            raise
        except IOError:
            print("Could not write file to disk!")
            raise


def main():
    convert_txt_to_html_to_json(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
