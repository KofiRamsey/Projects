secret_number = 10
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess the secret number: '))
    guess_count += 1
    if guess == secret_number:
        print('You guessed it right!!')
        break
    elif guess <= guess_limit:
        print('Try Again!')
    else:
        print('You Lose!')




