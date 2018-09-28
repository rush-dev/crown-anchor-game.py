import random, os, time

dice_list = [4,6,8,10,20]
gameplay = 'y'
money = 100

input('Welcome to the Crown and Anchor Game! Press any key to continue.')
os.system('cls' or 'clear')

while gameplay == 'y' or 'Y' and money >= 1:
    dice = input('To start choose the number of sides for the three dice: \n4 \n6 \n8 \n10 \n20 \nEnter your answer here: ')

    if int(dice) not in dice_list:
        print('Error! Value not valid.')
        break

    print(f'Bank: ${money}')
    dice = int(dice)
    
# Dice sides error handling #
    while True:
        try:
            if dice == 4:
                print('4 sided dice')
                break
            elif dice == 6:
                print('6 sided dice')
                break
            elif dice == 8:
                print('8 sided dice')
                break
            elif dice == 10:
                print('10 sided dice')
                break
            elif dice == 20:
                print('20 sided dice')
                break

        except ValueError:
            print('Oops! That is not a valid entry. Please try again...')

    num = input(f'Great! now choose a number between 1 and {dice}: ')
    num = int(num)
    print(f'Your Number: {num}')

    print('Rolling the dice...')
    dice1 = random.randint(1,dice)
    dice2 = random.randint(1,dice)
    dice3 = random.randint(1,dice)

    time.sleep(2)
    print(f'Dice One: {dice1}\nDice Two: {dice2}\nDice Three: {dice3}')

# +1 Logic #

    if dice1 == num and dice2 != num and dice3 != num:
        print('You win and +1')
        money += 1
        print(f'Bank: ${money}')

    if dice2 == num and dice3 != num and dice1 != num:
        print('You win and +1')
        money += 1
        print(f'Bank: ${money}')

    if dice3 == num and dice1 != num and dice2 != num:
        print('You win and +1')
        money += 1
        print(f'Bank: ${money}')

# +2 Logic #

    if dice1 == num and dice2 == num and dice3 != num:
        print('You win and +2')
        money += 2
        print(f'Bank: ${money}')

    if dice2 == num and dice3 == num and dice1 != num:
        print('You win and +2')
        money += 2
        print(f'Bank: ${money}')

    if dice3 == num and dice1 == num and dice2 != num:
        print('You win and +2')
        money += 2
        print(f'Bank: ${money}')

# +3 and lose #

    if dice1 == num and dice2 == num and dice3 == num:
        print('You win and +3')
        money += 3
        print(f'Bank: ${money}')

    if dice1 != num and dice2 != num and dice3 != num:
        print('Your number did not match, you lose!')
        money -= 1
        print(f'Bank: {money}')

    gameplay = input('Play again? Y/N: ')
    #os.system('cls' or 'clear')

    if gameplay == 'n' or gameplay == 'N':
        print(f'Thanks for playing.\nTotal Money: ${money}')
        break