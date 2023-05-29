import random

ROWS = 3
COLUMNS = 3

SYMBOLS_COUNT = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

SYMBOL_VALUES = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}


def deposit():
    while True:
        deposit_amount = input('Enter a deposit amount: ')
        try:
            number_deposit_amount = float(deposit_amount)
            if number_deposit_amount <= 0:
                print('Invalid deposit amount, try again')
            else:
                return number_deposit_amount
        except ValueError:
            print('Invalid deposit amount, try again')


def get_number_of_lines():
    while True:
        lines = input('Enter the number of lines to bet on (1-3): ')
        try:
            number_of_lines = int(lines)
            if number_of_lines <= 0 or number_of_lines > 3:
                print('Invalid number of lines, try again')
            else:
                return number_of_lines
        except ValueError:
            print('Invalid number of lines, try again')


def get_bet(balance, lines):
    while True:
        bet = input('Enter the total bet: ')
        try:
            number_bet = float(bet)
            if number_bet <= 0 or number_bet > balance:
                print('Invalid bet, try again')
            else:
                return number_bet
        except ValueError:
            print('Invalid bet, try again')


def spin():
    symbols = []

    for symbol, count in SYMBOLS_COUNT.items():
        for _ in range(count):
            symbols.append(symbol)

    reels = []
    for _ in range(COLUMNS):
        reels.append([])
        reel_symbols = symbols[:]
        for _ in range(ROWS):
            random_index = random.randint(0, len(reel_symbols) - 1)
            selected_symbol = reel_symbols[random_index]
            reels[-1].append(selected_symbol)
            reel_symbols.pop(random_index)
    return reels


def transpose(reels):
    rows = []

    for i in range(ROWS):
        rows.append([])
        for j in range(COLUMNS):
            rows[-1].append(reels[j][i])

    return rows


def print_rows(rows):
    for row in rows:
        row_string = ' | '.join(row)
        print(row_string)


def get_winnings(rows, bet, lines):
    winnings = 0

    for row in range(lines):
        symbols = rows[row]
        all_same = all(symbol == symbols[0] for symbol in symbols)

        if all_same:
            winnings += bet * SYMBOL_VALUES[symbols[0]]

    return winnings


def game():
    balance = deposit()

    while True:
        print('You have a balance of $' + str(balance))
        number_of_lines = get_number_of_lines()
        bet = get_bet(balance, number_of_lines)
        balance -= bet * number_of_lines
        reels = spin()
        rows = transpose(reels)
        print_rows(rows)
        winnings = get_winnings(rows, bet, number_of_lines)
        balance += winnings
        print('You won $' + str(winnings))

        if balance <= 0:
            print('You ran out of money!')
            break

        play_again = input('Do you want to play again? (y/n) ').lower()

        if play_again != 'y':
            break


game()
