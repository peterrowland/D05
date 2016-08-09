#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    user_input = input("Please enter an integer:")

    try:
        user_num = int(user_input)

    except:
        print('Use only integers.')
        pass

    else:
        if user_num % 2 == 0:
            print('even')
        else:
            print('odd')

    return None


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    for row in range(0,10):
        print('')
        for i in range (0,10):
            # print ((row * 10) + i, end=' ')
            print ("%02d" % ((row * 10) + i), end=' ')

    print('')

def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    user_input = ''
    user_sum = 0
    count = 0

    while user_input.lower() != 'done':
        user_input = input("add a number to the average: ")

        try:
            user_sum += int(user_input)

        except:
            pass

        else:
            count += 1

    return (user_sum / count)


##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    even_odd()
    ten_by_ten()
    print(find_average())

if __name__ == '__main__':
    main()
