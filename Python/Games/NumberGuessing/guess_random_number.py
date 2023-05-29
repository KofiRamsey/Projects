import random


def easy(attempts=0):
    top_of_range = int(input('Type the maximum number you want as the top of the range: '))
    random_num = random.randint(0, top_of_range)
    while True:
        user_guess = int(input('Type in your guess: '))

        if user_guess == random_num:
            print('Well Done! You guessed it right!')
            print(f'It took you {attempts} attempts to guess it right')
            play_again = input('\nDo you want to try again? ').lower()
            if play_again == 'yes':
                easy()
            else:
                quit()
        else:
            if user_guess > random_num:
                print('You are above the number\n')
                attempts += 1
            else:
                print('You are below the number\n')
                attempts += 1


def hard(attempts=0):
    print('YOU HAVE 20 ATTEMPTS TO GUESS THE NUMBER BETWEEN 1 AND 100\nGOOD LUCK')
    random_num = random.randint(0, 100)

    while True:
        user_guess = int(input('Type in your guess: '))

        if user_guess == random_num:
            print('Well Done! You guessed it right!')
            print(f'It took you {attempts} attempts to guess it right\n')

            play_again = input('\nDo you want to try again? ').lower()
            if play_again == 'yes':
                hard()
            else:
                quit()
        else:
            print('You got it wrong, try again')
            attempts += 1
            print(f'Attempts remaining: {20 - attempts}\n')
            if attempts == 20:
                print(f'Unfortunately you could not guess it in 20 attempts\nGAME OVER :(')
                print(f'The secret number was: {random_num}\n')

                play_again = input('\nDo you want to try again? ').lower()
                if play_again == 'yes':
                    hard()
                else:
                    quit()


print('''
Pick Difficulty:
- Easy
- Hard
''')
difficulty = input('> ').lower()

if difficulty == 'easy':
    easy()
elif difficulty == 'hard':
    hard()
else:
    print('Pick between "easy" or "hard"')
