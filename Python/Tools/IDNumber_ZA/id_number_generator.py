import random

x = random.randint(0, 9)
y = random.randint(0, 9)

print('Hello, Welcome to your ID generator\n')

while True:
    full_name = input('Enter your full name:'
                       '\n > ')
    if full_name == "":
        continue
    else:
        break


while True:
    year_of_birth = input('\nWhat year were you born in?'
                          '\n (yyyy)'
                          '\n > ')

    length = len(year_of_birth)

    if length > 4:
        continue
    elif length < 4:
        continue
    elif length == 4:
        break

while True:
    month_of_birth = input('\nWhat month were you born in?'
                           '\n (mm - please use the mm format (for example 01, 06, 12))'
                           '\n > ')
    limit = int(month_of_birth)

    if limit > 12:
        print('too high, only 01 to 12 accepted')
        continue
    elif limit < 1:
        print('too low, only 01 to 12 accepted')
        continue
    elif len(month_of_birth) != 2:
        continue
    else:
        break

while True:
    day_of_birth = input('\nWhat day were you born on?'
                         '\n (dd)'
                         '\n > ')
    limit = int(day_of_birth)

    if limit > 31:
        print('too high, only 01 to 31 accepted')
        continue
    elif limit < 1:
        print('too low, only 01 to 31 accepted')
        continue
    elif len(day_of_birth) != 2:
        continue
    else:
        break

gender = input('\nWhat is your Gender?'
               '\nMale or Female (M or F is accepted too)'
               '\n > ').lower()

email = input('\nWhat is your Email Address?'
              '\n > ').lower()

isCitizen = True
citizen_code = 0
citizen = input('\nAre you a citizen?'
                '\n(yes or no)'
                '\n > ').lower()

if citizen == 'yes':
    isCitizen = True
    citizen_code = 1
elif citizen == 'no':
    isCitizen = False
    citizen_code = 0

# Gender Code - Male(0001, 4999) and Female(5000, 9999)
if gender == 'female' or 'f':
    gen_code = random.randint(1, 4999)
    if 99 < gen_code < 1000:
        gen_code = f'0{gen_code}'
    elif 9 < gen_code < 100:
        gen_code = f'00{gen_code}'
    elif 0 < gen_code < 10:
        gen_code = f'000{gen_code}'
elif gender == 'male' or 'm':
    gen_code = random.randint(5000, 9999)
else:
    print('Invalid Gender!!')

# ---------------------------------------------------------------------------------------------------------------------
# Final Results

print(f'\nYour Full Details:'
      f'\nFull Name - {full_name.capitalize()}'
      f'\nAge - {2023 - int(year_of_birth)}'
      f'\nDate of Birth - {year_of_birth}/{month_of_birth}/{day_of_birth}'
      f'\nGender - {gender.upper()}'
      f'\nEmail Address - {email}'
      f'\nCitizen - {citizen.capitalize()}'
      f'\n'
      f'\nIdentification Number - {year_of_birth[2:]}{month_of_birth}{day_of_birth}{gen_code}{citizen_code}{x}{y}')
