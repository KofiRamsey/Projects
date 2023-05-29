principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input('Enter the principal amount: '))
    if principle <= 0:
        print('The principal cannot be less than or equal to 0')

while rate <= 0:
    rate = float(input('Enter the interest rate: '))
    if rate <= 0:
        print('The interest rate cannot be less than or equal to 0')

while time <= 0:
    time = int(input('Enter the time in years: '))
    if time <= 0:
        print('The time cannot be less than or equal to 0')

total = principle * pow((1 + rate / 100), time)
print(f'Balance after {time} year(s): ${total:.2f}')

