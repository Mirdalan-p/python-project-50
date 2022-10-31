import argparse
import json


parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')
parser.add_argument('-f FORMAT', dest='--format FORMAT', default=json,
                    help="set format of output")

parser.add_argument('first_file')
parser.add_argument("second_file")

args = parser.parse_args()

print(args)

if __name__ == '__main__':
    pass