balance = 1000


def main():
    while True:

        option = int(input('''
**********************************
Enter an option:
**********************************
1 - Show Balance
2 - Deposit Money
3 - Withdraw Money
4 - Exit
----------------------------------
> '''))

        if option == 1:
            show_balance()
        elif option == 2:
            deposit()
        elif option == 3:
            withdraw()
        elif option == 4:
            print('Thank you! Have a great day!!')
            break
        else:
            print("Enter a valid option please!!")
            break


def show_balance():
    print(f'Your balance is {balance}')


def deposit():
    dep_ = float(input("Enter amount to deposit: "))
    global balance
    balance += dep_
    print(f"Your new balance is {balance}")


def withdraw():
    withdrawal = float(input("Enter amount to withdraw: "))
    global balance
    balance -= withdrawal
    print(f"Your new balance is {balance}")


main()
