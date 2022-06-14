'''
Project:BST
Author:Aaron Zelenski
Course:CS 2420
Date:6 - 9 - 2022
'''

import string
from bst import BST
the_tree = BST()


class Pair:
    ''' Encapsulate letter,count pair as a single entity.

    Realtional methods make this object comparable
    using built-in operators.
    '''

    def __init__(self, letter, count=1):
        self.letter = letter
        self.count = count

    def __eq__(self, other):
        return self.letter == other.letter

    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'

    def __str__(self):
        return f'({self.letter}, {self.count})'


def make_tree():
    """reads txt file and can test all routines in here"""

    with open("around-the-world-in-80-days-3.txt", "r", encoding="utf-8") as story_file:
        line = story_file.read()
        any_punctuation = string.punctuation
        for char in line:
            if not char.isspace() and char not in any_punctuation:
                pair = Pair(char, 1)
                the_tree.add(pair)

    print(the_tree)
    # print()
    # print()
    # print(the_tree.rebalance())
    story_file.close()

    return the_tree


def main():
    """contains make_tree routine only"""
    make_tree()


if __name__ == "__main__":
    main()
