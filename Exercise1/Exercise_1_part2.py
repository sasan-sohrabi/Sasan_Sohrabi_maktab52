# Exercise 1 - part 2

# Import related libraries
import argparse
from Exercise_1_part1 import average

if __name__ == '__main__':

    # Define parse args for python script
    parser = argparse.ArgumentParser(description='Average Calculator')

    parser.add_argument('-g', '--grades', action='store', metavar="STUDENT'S GRADES",
                        help='Input sequence of float number', required=True, nargs='*')

    parser.add_argument('-f', '--float', action='store', metavar='FLOAT', default='2',
                        help='Number of digits after decimals', nargs='?')

    args = parser.parse_args()

    print(average(args.grades, int(args.float)))
