def action(pull, name):
    while True:
        choose = int(input(f'{name}, please choose a number of sticks '))
        if choose < 1 or choose > 3:
            print(f'You tried to take {choose} sticks. Allowed 1, 2 or 3')
            continue
        if choose > pull:
            print('There arent so many sticks, try again')
            continue
        pull -= choose
        print(f'You have {pull} left')
        if pull < 1:
            print(f'{name} won')
            break
        return pull

print("We start new game")
player1_name = input('Please enter the name of the first player: ')
player2_name = input('Please enter the name of the second player: ')

print(f'The name of the first player: {player1_name}')
print(f'The name of the second player: {player2_name}')

pull = 10
while pull != 0:
    pull = action(pull, player1_name)
    pull2 = pull
    pull2 = action(pull2, player2_name)
    pull = pull2