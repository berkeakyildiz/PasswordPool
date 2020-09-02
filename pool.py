#
# Created by Berke Akyıldız on 28/June/2019
#
import sys
from itertools import product

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def createPasswordPool(alphabet, wordCount):
    pool = open("pool.txt", "w+")
    for length in range(1, wordCount + 1):
        to_attempt = product(alphabet, repeat=length)
        for attempt in to_attempt:
            attempt = ''.join(attempt)
            pool.write(attempt + "\n")
    return pool.name


def appendPasswordPool(passwords):
    pool = open("pool.txt", "r+")
    for password in passwords:
        pass
    return pool.name


def main():
    arguments = sys.argv
    usage = "USAGE python pool.py [WORDSIZE] [OPTIONS]\n"
    help = usage + "[OPTIONS}\n-a: Add lowercase characters to pool\n-aA: Add lowercase and uppercase characters to pool\n-aA1: Add " \
                   "lowercase, uppercase and numbers to pool\n[CUSTOM CHARACTERS]: Example: python pool.py 2 -$ " \
                   "'?_*\n-pass: Add your custom passwords to the pool. Example: python pool.py -pass [\"test\", \"deneme\", \"adming\"]\n "
    alphabet = []
    wordCount = 0
    passwords = []
    if len(arguments) == 1:
        print(usage)

    if "-h" in arguments:
        print(help)
    if len(arguments) == 2:
        print(help)

    if len(arguments) > 2:
        wordCount = int(arguments[1])
    if "-a" in arguments:
        alphabet = alphabet + lowercase
    if "-A" in arguments:
        alphabet = alphabet + lowercase
        alphabet = alphabet + uppercase
    if "-aA1" in arguments:
        alphabet = alphabet + lowercase
        alphabet = alphabet + uppercase
        alphabet = alphabet + numbers
    if "-$" in arguments:
        i = arguments.index("-$")
        chars = arguments[i+1]
        for char in chars:
            alphabet.append(char)
    # print(alphabet)
    # print(wordCount)
    createPasswordPool(alphabet, wordCount)

    if "-pass" in arguments:
        index = arguments.index("-pass")
        for i in range(index + 1, len(arguments)):
            print(arguments[i])
            passwords.append(arguments[i])
    appendPasswordPool(passwords)


if __name__ == "__main__":
    main()
