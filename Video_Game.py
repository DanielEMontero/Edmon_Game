###########################################################
###########################################################

################### VIDEO NUMBERS GAME ####################

###########################################################

####################### DESCRIPTION #######################
# This program let you play to guess the number with Edmon. 


######################### AUTHOR ##########################
# Ing. DANIEL EDUARDO MONTERO RAMÍREZ



import random


def run():
    num = None
    rnd = random.randint(0,100)
    attemp = 5
    while num != rnd and attemp > 0:
        number = input('Hi! I´m Edmon. Please, choose a number between 0 to 100. '+ ' You have ' + str(attemp) + ' attemps: ')
        attemp -= 1
        try:
            num = int(number)
        except:
            print('Only, numbers')
            quit
        if num < rnd:
            print('The number is bigger')
        elif num > rnd:
            print('The number is smaller')
    if num == rnd:
        print('You WON!!!')
    else:
        print('You Lost... :(')


if __name__ == "__main__":
    run()
