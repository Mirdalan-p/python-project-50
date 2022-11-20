import argparse
from gendiff.scripts.make_diff import generate_diff
from gendiff.scripts.stylish import make_stylish
from gendiff.scripts.parser import make_parse
from gendiff.scripts.get_diff import get_diff


parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')
parser.add_argument('-f', '--format', help="set format of output")

parser.add_argument('first_file')
parser.add_argument("second_file")

args = parser.parse_args()


def main():
    data = (make_parse(args.first_file), make_parse(args.second_file))
    
    print((generate_diff(data)))
