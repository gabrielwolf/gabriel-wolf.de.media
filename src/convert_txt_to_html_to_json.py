#!/usr/local/bin/python3

"""
This script reads a given text file converts it to HTML into a JSON container.
This container then is written to disk.
"""

import json
import sys


def convert_txt_to_html_to_json(input_file, output_file):
    json_container = dict()
    with open(input_file, "rt") as file:
        # KISS way to preserve some whitespace in HTML
        data = file.read().replace("\n", "<br />").replace("     ", "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;").replace("    ",
                                                                                                              "&nbsp;&nbsp;&nbsp;&nbsp;").replace(
            "   ", "&nbsp;&nbsp;&nbsp;")
        json_container['text'] = data
    try:
        with open(output_file, "w") as output_file:
            json.dump(json_container, output_file, separators=(',', ':'), sort_keys=True, indent=4)
        return True
    except TypeError:
        print("No valid JSON data!")
        raise
    except IOError:
        print("Could not write file to disk!")
        raise


def main():
    if len(sys.argv) < 3:
        print("This script reads a given text file and wraps it into a JSON container.\n"
              "This container is then written to disk.")
        print("Usage: ./convert_txt_to_html_to_json input.txt output.json")
        return False
    convert_txt_to_html_to_json(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
