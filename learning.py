"""
Write a Python program that asks for a number, n, and then prints out all the numbers between 1 and n, inclusive, and the numbers' squares and cubes.

The program should work like this:

Enter a number: 4
The number is 1, its square is 1 and its cube is 1.
The number is 2, its square is 4 and its cube is 8.
The number is 3, its square is 9 and its cube is 27.
The number is 4, its square is 16 and its cube is 64.

how to run python code https://www.w3schools.com/python/python_getstarted.asp

"""

# https://www.w3schools.com/python/python_output.asp
print('Enter a number: ')

# https://www.w3schools.com/python/python_variables.asp

# https://www.w3schools.com/python/python_user_input.asp
x = input()

# https://www.w3schools.com/python/python_casting.asp
target_number = int(x)
current_number = int(1)

# https://www.w3schools.com/python/python_operators_arithmetic.asp


# https://www.w3schools.com/python/python_while_loops.asp
while target_number >= current_number:
 square = current_number * current_number
 cube = current_number * current_number * current_number
 # https://www.w3schools.com/python/python_strings_concatenate.asp
 print('The number is ' + str(current_number) + ', its square is ' + str(square) + ', its cube is ' + str(cube))
 current_number += 1
else:
 print('Your chosen number has been reached. ') 