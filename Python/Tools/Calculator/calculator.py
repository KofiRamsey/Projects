# NAME OF PERSON
name = input('Hello👋, What is your name🤓? ')
# EQUATIONS AVAILABLE
print(f'''
Hello {name.capitalize()}😃, What type of calculation would you like to perform today?
- add ➕
- subtract ➖
- multiply ✖
- divide ➗
- square 
- remainder
''', )
# ASKS USER TO PICK FROM OPTIONS AVAILABLE ABOVE
equation = input('Please pick an option above: ')


# FUNCTIONS
def addition():  # ADD 2 NUMBERS
    x = float(input("First number? "))
    y = float(input("Second number? "))
    answer = x + y
    print(f'The answer is {answer}')


def subtraction():  # SUBTRACT 2 NUMBERS
    x = float(input("First number? "))
    y = float(input("Second number? "))
    answer = x - y
    print(f'The answer is {answer}')


def multiplication():  # MULTIPLY 2 NUMBERS
    x = float(input("First number? "))
    y = float(input("Second number? "))
    answer = x * y
    print(f'The answer is {answer}')


def division():  # DIVIDE 2 NUMBERS
    x = float(input("First number? "))
    y = float(input("Second number? "))
    answer = x / y
    print('The answer is {:.2f}'.format(answer))


def squared():  # SQUARES A NUMBER
    x = float(input("First number? "))
    y = float(input("Second number? "))
    answer = x ** y
    print(f'The answer is {answer}')


def modulus_remainder():  # RETURNS A REMAINDER
    x = float(input("First number? "))
    y = float(input("Second number? "))
    answer = x % y
    print(f'The answer is {answer}')


if equation == 'add':
    addition()
elif equation == 'subtract':
    subtraction()
elif equation == 'divide':
    division()
elif equation == 'multiply':
    multiplication()
elif equation == 'square':
    squared()
elif equation == 'remainder':
    modulus_remainder()
else:  # RETURN THIS IF USER FAILS TO PICK WHATS AVAILABLE
    print('''
INVALID, PLEASE ENTER:
"add"
"subtract"
"multiply"
"divide"
"square"
"remainder"
''')


