# Exercise 1 - part 1

# Import related library
import sys


# Define function for calculating average of input variable in terminal
def average(input_list: list, round_num: int = 2) -> float or str:
    try:
        correct_input_list = [float(string_number) for string_number in input_list]
        print('The Average is :')
        return round(sum(correct_input_list) / (len(input_list)), round_num)
    except ValueError as e:
        print(e)
        return 'Your input variable must be float!!!'



