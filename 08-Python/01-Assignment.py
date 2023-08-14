# OPERATION MENU
operation = input('''Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

number_1 = int(input("Enter your first number: "))
number_2 = int(input("Enter your first number: "))

# ADDITION LOGIC
if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)
    
# SUBTRACTION LOGIC
elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

# MULTIPLICATION LOGIC
elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

# DIVISION LOGIC
elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('You have not typed a valid operator, please run the program again')


