#!/usr/bin/env python3
import os

import sympy
from sympy import *


def get_input() -> Matrix:
    """Get input from the user and convert to a Matrix Object"""
    # initialize the variables for the loop
    temp = 1
    matrix = Matrix()
    counter = 0

    print('Enter the elements of the matrix row by row, seperated by spaces\nPress Enter when done')
    while temp:
        # get the input
        temp = input()
        if temp:
            if ',' in temp:
                rows = temp.split(',')
                for row in rows:
                    matrix = matrix.row_insert(counter, Matrix(
                        [[int(i) for i in row.split(' ') if i]]))
                    counter += 1
            # add the row to the matrix if the row isn't empty
            else:
                matrix = matrix.row_insert(counter, Matrix(
                    [[int(i) for i in temp.split(' ') if i]]))
                counter += 1
    return matrix


def row_echelon(matrix: Matrix) -> Matrix:
    """Calculate and return the reduced row echelon form"""
    try:
        temp_rref = matrix.rref()
        pprint(temp_rref)
        input()
        return temp_rref
    except:
        print("Error calculating Reduced Row Echelone Form")
        input()


def determin(matrix: Matrix):
    """Calculate and return the determinent of a matrix"""
    try:
        temp_det = matrix.det()
        print(f'Determinent of matrix is: {temp_det}')
        input()
        return temp_det
    except sympy.matrices.common.NonSquareMatrixError:
        print("Matrix is not a Square Matrix")
        input()
        return 0


def inverse(matrix: Matrix):
    """Return the inverse of a matrix"""
    try:
        return matrix.inv()
    except sympy.matrices.common.NonSquareMatrixError:
        print('Matrix is not invertible')
        return 0


def main_menu():
    """The main menu loop"""
    os.system('cls||clear')
    matrix = get_input()
    options = ['Reduced Row Echelon Form',
               'Determinent', 'Invert', 'Change Matrix', 'Quit']
    rref = None
    det = None
    inverted = None

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
            else:
                pprint(rref)
                input()

        elif choice == 'Determinent':
            # Calculate the determinent if not already saved
            os.system('cls||clear')
            if det == None:
                det = determin(matrix)
            else:
                print(f'Determinent of matrix is: {det}')

        elif choice == 'Invert':
            os.system('cls||clear')
            if det != 0 and inverted != 0:
                if inverted:
                    pprint(inverted)
                else:
                    inverted = inverse(matrix)
                    if inverted:
                        pprint(inverted)
            else:
                print('The matrix is not inversible')
            input()

        elif choice == 'Change Matrix':
            # Change the matrix into a new one
            os.system('cls||clear')
            matrix = get_input()
            det = None
            rref = None
        elif choice == 'Quit':
            break


if __name__ == '__main__':
    main_menu()
