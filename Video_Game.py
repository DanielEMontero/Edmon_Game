import random


def run():
    num = None
    rnd = random.randint(0,100)
    while num != rnd:
        number = input('Please, choose a number between 0 to 100: ')
        try:
            num = int(number)
        except:
            print('Only, numbers')
            quit
        if num < rnd:
            print('The number is bigger')
        elif num > rnd:
            print('The number is smaller')
        else:
            print('You WON!!!')        


if __name__ == "__main__":
    run()
