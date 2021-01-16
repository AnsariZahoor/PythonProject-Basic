import random
roll = 'r'

while roll == 'r':
    num = random.randint(1,6)
    if num == 1 :
        print('o')
    if num == 2 :
        print('o ')
        print(' o')
    if num == 3 :
        print('o  ')
        print(' o ')
        print('  o')
    if num == 4 :
        print('o o')
        print('o o')
    if num == 5 :
        print('o o')
        print(' o ')
        print('o o')
    if num == 6 :
        print('o o')
        print('o o')
        print('o o')

    roll = input('Press r to roll & e to exit : ')
    print('\n')