#!/usr/bin/env python3
import os

from sympy import Matrix, pprint


def get_input() -> Matrix:
    """Get input from the user and convert to a Matrix Object"""
    # initialize the variables for the loop
    temp = "0"
    matrix = Matrix()
    counter = 0

    print('Enter the elements of the matrix row by row, seperated by spaces\nPress Enter when done')
    while temp:
        # get the input
        temp = input()
        if temp:
            # add the row to the matrix if the row isn't empty
            matrix = matrix.row_insert(counter, Matrix(
                [[int(i) for i in temp.split(' ')]]))
            counter += 1
    return matrix


def row_echelon(matrix: Matrix) -> Matrix:
    """Calculate and return the reduced row echelon form"""
    return matrix.rref()


def main_menu():
    """The main menu loop"""
    os.system('cls||clear')
    matrix = get_input()
    options = ['Reduced Row Echelon Form', 'Change Matrix', 'Quit']
    rref = None
    det = None

    while True:
        # Clear the screen
        os.system('cls||clear')

        # Print the matrix and an empty space below
        pprint(matrix)
        print()

        # Print the menu options and get input
        for counter, i in enumerate(options):
            print(f'[{counter+1}] {i}')
        choice = input('> ')

        # Convert input to a command
        try:
            choice = options[int(choice)-1]
        except:
            if 'q' in choice.lower() or 'quit' in choice.lower():
                break
            else:
                continue

        if choice == 'Reduced Row Echelon Form':
            # Calculate the reduced row echelon form if not already saved
            os.system('cls||clear')
            if not rref:
                rref = row_echelon(matrix)
                pprint(rref)
                input()
            else:
                pprint(rref)
                input()

        elif choice == 'Change Matrix':
            # Change the matrix into a new one
            os.system('cls||clear')
            matrix = get_input()
        elif choice == 'Quit':
            break


if __name__ == '__main__':
    main_menu()
