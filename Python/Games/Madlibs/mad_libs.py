def mad_libs():
    print('Welcome to the Mad Libs game!')

    # Get user inputs
    adjective1 = input('Enter an adjective: ')
    animal = input('Enter an animal: ')
    verb1 = input('Enter a verb (present tense): ')
    adjective2 = input('Enter another adjective: ')
    noun1 = input('Enter a noun: ')
    noun2 = input('Enter another noun: ')
    verb2 = input('Enter another verb (present tense): ')
    adjective3 = input('Enter a third adjective: ')
    verb3 = input('Enter another verb (present tense): ')

    story = (f'Once upon a time, there was a(n) {adjective1} {animal} who loved to {verb1}. '
             f'They were so {adjective2} that they always wore a {adjective3} {noun1} and carried a {noun2} wherever they went. '
             f'One day, while {verb2} in the park, they saw a {adjective1} {animal} {noun1}. '
             f'They {verb1} over to get a closer look, but it suddenly started to {verb3}. '
             f'{animal.capitalize()} was so {adjective3} that they {verb2} {verb3} away as fast as they could, '
             f'with their {noun1} {noun2} still in hand.')

    print(story)


mad_libs()
