import random

user_wins = 0
computer_wins = 0
ties = 0
options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Type rock/paper/scissors or "Q" to end the game and get the results: ').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print(f'Computer picked {computer_pick}')
    if user_input == computer_pick:
        print('Tie!')
        ties += 1
        continue
    elif user_input == 'rock' and computer_pick == 'scissors':
        print('You won!')
        user_wins += 1
    elif user_input == 'paper' and computer_pick == 'rock':
        print('You won!')
        user_wins += 1
    elif user_input == 'scissors' and computer_pick == 'paper':
        print('You won!')
        user_wins += 1
    else:
        print('You lost!')
        computer_wins += 1

if user_wins > computer_wins:
    print('Congratulations You Won!!!')
else:
    print('You Lost, Better Luck Next Time!!')

print()
print(f'User: {user_wins}   vs  Computer: {computer_wins}')
print(f'Ties: {ties}')
print('Goodbye!, thanks for playing!')

