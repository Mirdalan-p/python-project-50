import argparse
from gendiff.engine import generate_diff
from gendiff.scripts.parser import make_parse

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')
parser.add_argument('-f', '--format',
                    dest="format",
                    choices=['stylish', 'plain', 'json'],
                    default="stylish",
                    help='set format of output')

parser.add_argument('first_file')
parser.add_argument("second_file")
args = parser.parse_args()


def main():
    first = make_parse(args.first_file)
    second = make_parse(args.second_file)
    formatter = args.format
    if formatter != 'plain' or formatter != 'json':
        return generate_diff(first, second, 'stylish')
    else:
        return generate_diff(first, second, formatter)
