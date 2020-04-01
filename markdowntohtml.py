"""
Python command-line program to convert a Markdown file to HTML

Basic Program flow:
1. Read in file
2. Split file into lines of



"""

__author__ = "Ajaydeep Singh"
__version__ = "0.1.0"

import argparse
from disassemble import get_paragraphs, covert_to_object
from link_handler import *


def convert(markdown_text):
    paragraphs = get_paragraphs(markdown_text)
    paragraph_objects = []
    for x in paragraphs:
        obj = covert_to_object(x)
        paragraph_objects.append(obj)

    paragraph_objects = convert_links(paragraph_objects)
    html_array = combine_text(paragraph_objects)
    return '\n'.join(html_array)


def combine_text(object_array):

    out_arr = []
    for x in object_array:
        if x.type == 'br':
            out_arr.append('')
        else:
            tags = '<' + x.type + '>' + x.content + '</' + x.type + '>'
            out_arr.append(tags)

    return out_arr


def main(args):
    """ Main entry point of the app """
    # print(args.file.read())
    data = args.file.read()
    out = convert(data)
    output_filename = str(args.file.name[:-3]) + '_new.html'

    f = open(output_filename, "w")
    f.write(out)
    f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'), help="Markdown file you would like to convert to HTML")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)