#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body
def long_words():

    try:
        fin = open('words.txt')

    except:
        print("can't open file")

    else:
        c = 0
        for line in fin:
            word = line.strip()
            if len(word) > 20:
                print(word)
                c += 1

##############################################################################
def main():
    long_words()

if __name__ == '__main__':
    main()
