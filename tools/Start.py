import random
from enemys import group1

# start the game
while True:
    start = input('''
---------------------------------------------------------------------------
Hello!
Do you wont to play a game ?
[Y]es / [N]o : ''')

    # character selection
    if start.lower() == 'y':
        char = input('''---------------------------------------------------------------------------
Select your character :
        /  hp  /  mp  / att. max / spell max att. /
        /------/------/----------/----------------/
Hero    :  200 /  30  /    60    /      20        /
        /------/------/----------/----------------/
Wizard :  150 /  80  /    30    /      60        /
        /------/------/----------/----------------/
[H]ero / [W]izard : ''')
        if char.lower() == 'h':
            user_name = 'Hero'
            user_hp = 200
            user_mp = 30
            user_att = random.randint(1, 60)
            user_spell = random.randint(1, 20)
            break
        elif char.lower() == 'w':
            user_name = 'Wizard'
            user_hp = 150
            user_mp = 80
            user_att = random.randint(1, 30)
            user_spell = random.randint(1, 60)
            break

    if start.lower() == 'n':
        quit()

    else:
        print('Invalid entry')

# fight group 1
group1.fight1(user_name, user_hp, user_mp)
