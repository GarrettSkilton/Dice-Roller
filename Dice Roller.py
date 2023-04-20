import random

list = ['d6', 'd10', 'd12', 'd20']
for pick in list:
    pick_dice = input('Enter a dice to role; d6, d10, d12, or d20: ')
    if pick_dice in list:
        break
    else:
        print('Invalid input, try again!')
        continue

if pick_dice == 'd20':
    def d20():
        rolls = input('Enter a number of times to roll a twenty sided dice: ')
        try:
            rolls = int(rolls)
        except:
            if rolls == '' or type(rolls) == str:
                print('Invalid input, restarting...')
                quit()
        for i in range(rolls):
            yield random.randint(1, 20)


    for random_number in d20():
        print(f'Rolled {random_number}')

elif pick_dice == 'd12':
    def d12():
        rolls = input('Enter a number of times to roll a twelve sided dice: ')
        try:
            rolls = int(rolls)
        except:
            if rolls == '' or type(rolls) == str:
                print('Invalid input, restarting...')
                quit()
        for i in range(rolls):
            yield random.randint(1, 12)


    for random_number in d12():
        print(f'Rolled {random_number}')

elif pick_dice == 'd10':
    def d10():
        rolls = input('Enter a number of times to roll a ten sided dice: ')
        try:
            rolls = int(rolls)
        except:
            if rolls == '' or type(rolls) == str:
                print('Invalid input, restarting...')
                quit()
        for i in range(rolls):
            yield random.randint(1, 10)


    for random_number in d10():
        print(f'Rolled {random_number}')

if pick_dice == 'd6':
    def d6():
        rolls = input('Enter a number of times to roll a six sided dice: ')
        try:
            rolls = int(rolls)
        except:
            if rolls == '' or type(rolls) == str:
                print('Invalid input, restarting...')
                quit()
        for i in range(rolls):
            yield random.randint(1, 6)


    for random_number in d6():
        print(f'Rolled {random_number}')