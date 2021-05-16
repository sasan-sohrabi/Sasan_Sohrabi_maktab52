# Exercise 4

# Guess Number Exercise

# Import related libraries
import argparse

if __name__ == '__main__':
    # Define parse args for python script
    parser = argparse.ArgumentParser(description='Guessing Number')

    parser.add_argument('-f', '--fr', action='store', metavar="FROM NUMBER", default=0, type=int,
                        help='First range of random number')

    parser.add_argument('-t', '--to', action='store', metavar='TO NUMBER', default=1000, type=int,
                        help='End range of random number')
    parser.add_argument('-g', '--guess', action='store', metavar='COUNT GUESS', default=10, type=int,
                        help='Count of guess that program try to achieve answer')
    args = parser.parse_args()

    if args.fr < 0 or args.to < 0 or args.guess < 0:
        parser.error('Input must be positive integer')

    # questions function return the question will be asked from player.
    def questions(n):
        question = ['is that Lower than', 'is that Greater than', 'is that']
        return question[n]

    # median function return median of two input variable.
    def median(a, b):
        return (a + b) // 2

    # change function return variables that be changed in function.
    def change_ub(num, lb, ub):
        temp = num
        num = median(lb, temp)
        return temp, num

    # change function return variables that be changed in function.
    def change_lb(num, lb, ub):
        temp = num
        num = median(temp, ub)
        return temp, num

    # guess_number function is main function for guessing number game.
    def guess_number(attempts, lowerbound, upperbound):
        print(f'Choose a number between {lowerbound} and {upperbound}, and I`ve {attempts} attempts.', '\nReady?')
        count = 0
        num = (upperbound - lowerbound) // 2
        lb = lowerbound
        ub = upperbound
        temp = 0
        while count <= attempts:
            if ub - lb < 5:
                temp = attempts - count
                for i in range(temp):
                    if input(f'{count + 1}) {questions(2)} {lb} ?').lower() == 'yes':
                        return print('Yesss, I WIN!')
                    else:
                        lb = lb + 1
                    count += 1
                else:
                    return print('Im GameOver!')
            else:
                if count % 2 == 0:
                    if input(f'{count + 1}) {questions(0)} {num} ?').lower() == 'yes':
                        ub, num = change_ub(num, lb, ub)
                    else:
                        lb, num = change_lb(num, lb, ub)
                else:
                    if count % 2 != 0:
                        if input(f'{count + 1}) {questions(1)} {num} ?').lower() == 'no':
                            ub, num = change_ub(num, lb, ub)
                        else:
                            lb, num = change_lb(num, lb, ub)
            count += 1
        else:
            return print('Im GameOver!')


    guess_number(int(args.guess), int(args.fr), int(args.to))
