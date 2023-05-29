import random
from words import word_list


def main():
    word = random.choice(word_list)
    attempts = 7
    guesses = []
    done = False

    print('\nWELCOME AND GOOD LUCK!!')

    while not done:
        for letter in word:
            if letter.lower() in guesses:
                print(letter, end=' ')
            else:
                print('_ ', end=' ')

        guess = input(f'\nAttempts Left: {attempts} \nNext Guess: ')
        print('')
        if guess.lower() in guesses:
            print(f'You have already guessed the letter {guess.lower()}')
            continue
        guesses.append(guess.lower())
        print(f'Letters Guessed: {guesses}')

        if guess.lower() not in word.lower():
            attempts -= 1
            if attempts == 0:
                break

        done = True
        for letter in word:
            if letter.lower() not in guesses:
                done = False

    if done:
        print(f'Well done!!, You got the word: {word.upper()}')
    else:
        print(f'Game Over!!, The word was: {word.upper()}')

main()
