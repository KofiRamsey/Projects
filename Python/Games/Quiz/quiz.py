print('Welcome to this awesome computer quiz!!')

playing = input('Do you want to play? ').lower()
score = 0

def want_to_play():
    if playing == "yes":
        print('You chose YES SO LETS BEGIN!!')
    elif playing == "no":
        print('Okay then, maybe next time...HAVE A GREAT DAY!')
        quit()
    else:
        print('Yes or No please!!')
        quit()
want_to_play()

q1 = input('What does CPU stand for? ').lower()
if q1 == 'central processing unit':
    print('Correct!')
    score += 1
else:
    print('Wrong!')

q2 = input('What color is the sky? ').lower()
if q2 == 'blue':
    print('Correct!')
    score += 1
else:
    print('Wrong!')

q3 = input('What color are clouds? ').lower()
if q3 == 'white' or q3 == 'grey':
    print('Correct!')
    score += 1
else:
    print('Wrong!')

q4 = input('What color is grass? ').lower()
if q4 == 'green':
    print('Correct!')
    score += 1
else:
    print('Wrong!')

q5 = input('Who is the greatest soccer player? ').lower()
if q5 == 'messi':
    print('Correct!')
    score += 1
else:
    print('Wrong!')

def your_score():
    if score == 0:
        print(f'Your score is {score}, LOL! Did you even try??')
    elif score == 1:
        print(f'Your score is {score}, LOL!, {score} is not too bad right??')
    elif score == 2:
        print(f'Your score is {score}, You Tried!')
    elif score == 3:
        print(f'Your score is {score}, You did your best!')
    elif score == 4:
        print(f'Your score is {score}, Do not feel bad, nobody is perfect, WELL DONE!!')
    elif score == 5:
        print(f'Your score is {score}, Congratulations Genius!!, You get a prize!!')
    else:
        print("You just broke the system!!")
    print(f'You got {score/5 * 100}%')
your_score()
