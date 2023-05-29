import random
import string

length = int(input('Length of Password: '))
include_symbols = input('Do you want to include symbols? (yes/no)\n > ')

if include_symbols == 'yes':
    include_symbols = True
else:
    include_symbols = False

def generate_password(length, include_symbols):
    characters = string.ascii_letters + string.digits
    if include_symbols:
        characters += string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    return password

print(f'\nPassword: {generate_password(length, include_symbols)}')
