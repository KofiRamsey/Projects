from playsound import playsound
import time

# Define escape codes for clearing the console and returning the cursor to the top-left corner
CLEAR = "\033[2J"
CLEAR_AND_RETURN = '\033[H'

def alarm(seconds):
    time_elapsed = 0

    # Clear the console before starting the countdown
    print(CLEAR)

    # Loop until the specified number of seconds has elapsed
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        # Calculate the time remaining in minutes and seconds
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        # Print the time remaining in the top-left corner of the console
        print(f'{CLEAR_AND_RETURN}Alarm will go off in: {minutes_left:02d}:{seconds_left:02d}')

    # Play the alarm sound
    try:
        playsound('alarm.wav')
    except Exception as e:
        print(f'Error playing sound: {e}')

# Prompt the user for the number of minutes and seconds to wait
while True:
    try:
        minutes = int(input('How many minutes to wait: '))
        seconds = int(input('How many seconds to wait: '))

        # Validate user input
        if minutes < 0 or seconds < 0:
            raise ValueError('Please enter non-negative integers.')

        total_seconds = minutes * 60 + seconds
        break
    except ValueError as e:
        print(f'Error: {e}')

# Start the countdown
alarm(total_seconds)
