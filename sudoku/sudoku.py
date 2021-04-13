import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def read_puzzle_file(filename):
    """
    Read a given file of puzzle strings.
    Separate the individual puzzles, and return a list of them.
    """
    file = open(filename, "r")
    contents = file.read()
    file.close()
    puzzle_strings = contents.splitlines()
    return puzzle_strings


def process_puzzle_string(puzzle_string):
    """
    Given a string of 81 digits for a particular puzzle.
    Separate the digits up into their rows and columns, and importantly
    remember to convert from strings to integers.
    [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        ...
    ]
    """
    puzzle = []
    for row in range(9):
        start_index = row * 9
        end_index = (row + 1) * 9
        numbers = []
        for col in range(start_index, end_index):
            digit = puzzle_string[col]
            numbers.append(int(digit))
        puzzle.append(numbers)
    return puzzle



def display_puzzle(puzzle):
    for i in range(len(puzzle)):
        row = puzzle[i]
        for j in range(len(row)):
            n = row[j]
            print(n)




puzzle_strings = read_puzzle_file("puzzles.dat")

first_puzzle = process_puzzle_string(puzzle_strings[0])
display_puzzle(first_puzzle)
