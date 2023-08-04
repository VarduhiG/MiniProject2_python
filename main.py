import random

def dice_rolling():

    dicethrow_1 = random.randrange(1,7)

    dicethrow_2 = random.randrange(1,7)

    total = dicethrow_1 + dicethrow_2

    print('The sum of dice is {} + {} = {}'.format(dicethrow_1,dicethrow_2,total))

    return total





goal = dice_rolling()



if goal == 7 or goal == 11:

    print('You won')

    

elif goal == 2 or goal == 3 or goal == 12:

    print('You lose')



else:

    print('Now your goal number', goal)

    new_goal = goal

      

    

    while True:

        dice_roll = dice_rolling()

        if dice_roll == new_goal:

            print('You won')

            break

        elif dice_roll == 7:

            print('You lose')

            break
