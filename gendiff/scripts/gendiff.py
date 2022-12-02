import argparse
from gendiff.scripts.make_diff import generate_diff
from gendiff.formatters.get_stylish import make_stylish
from gendiff.formatters.get_plain import make_plain
from gendiff.scripts.parser import make_parse


parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')
parser.add_argument('-f', '--format',
                    dest="format",
                    choices=['stylish', 'plain', 'json'],
                    help='set format of output')

parser.add_argument('first_file')
parser.add_argument("second_file")
args = parser.parse_args()


def main(formatter='stylish'):
    data = (make_parse(args.first_file), make_parse(args.second_file))
    formatter = args.format
    if formatter == 'plain':
        print(make_plain(generate_diff(data)))
    else:
        print(make_stylish(generate_diff(data)))
