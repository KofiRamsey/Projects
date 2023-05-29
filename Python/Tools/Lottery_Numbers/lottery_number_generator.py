import random

lottery_numbers = []


def daily_lotto():
    for i in range(0, 5):
        number = random.randint(1, 36)
        lottery_numbers.append(number)


    lottery_numbers.sort()
    print(f'The lottery numbers are: {lottery_numbers}')


def lotto():
    for i in range(0, 6):
        number = random.randint(1, 52)
        lottery_numbers.append(number)

    lottery_numbers.sort()
    print(f'The lottery numbers are: {lottery_numbers}')


def powerball():
    for i in range(0, 5):
        number = random.randint(1, 50)
        poweroll = random.randint(1, 20)
        lottery_numbers.append(number)

    lottery_numbers.sort()
    print(f'Lottery Numbers: {lottery_numbers} | Powerball: {poweroll}')


intro = int(input('''
Welcome, Which lotto are you playing today??
1 - Daily Lotto
2 - Lotto
3 - Powerball
>  '''))

# results_generated = int(input('How many results do you want to generate? '))

if intro == 1:
    daily_lotto()
elif intro == 2:
    lotto()
elif intro == 3:
    powerball()




