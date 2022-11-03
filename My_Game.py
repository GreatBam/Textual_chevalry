# My first game ever, textual chevalry fight
# Jonathan, 13.03.22
import random


# Functions
def fight(user_name, user_hp, user_mp):
    # Set enemy
    enemy_name_list = ['bat', 'rat', 'vampire', 'golem']
    enemy_hp_list = [30, 60, 80, 120]
    enemy_att_list = [40, 60, 80, 100]
    rng_enemy = random.randint(0, 3)
    computer_hp = enemy_hp_list[rng_enemy]

    print('---------------------------------------------------------------------------')
    print('Your ennemy is a {}'.format(enemy_name_list[rng_enemy]))
    print('{} attack max, {} hp'.format(enemy_att_list[rng_enemy], enemy_hp_list[rng_enemy]))

    while True:
        computer_att = random.randint(0, enemy_att_list[rng_enemy])
        print('---------------------------------------------------------------------------')
        print('Your actual status : ' + str(user_name) + ' / ' + str(user_hp) + 'hp / ' + str(user_mp) + 'mp /')
        print('Enemy actual status : ' + str(enemy_name_list[rng_enemy]) + ' / ' + str(computer_hp) + 'hp /')
        action = input('Select an action : [A]ttack, [S]pell, [E]xit: ')
        print()

        # if you choose to attack
        if action.lower() == 'a':
            if user_name == 'Hero':
                user_att = random.randint(1, 60)
            else:
                user_att = random.randint(1, 30)

            user_hp = user_hp - computer_att
            computer_hp = computer_hp - user_att
            print('You made ' + str(user_att) + ' hit')
            print('Enemy: ' + str(computer_hp) + ' hp.')
            print('The enemy made ' + str(computer_att) + ' hit.')
            print('User: ' + str(user_hp) + ' hp')
            print()

            if user_hp <= 0 and computer_hp > 0:
                print('You lose')
                quit()
            elif computer_hp <= 0 and user_hp > 0:
                print('You won')
                rest(user_name, user_hp, user_mp)
            elif computer_hp <= 0 and user_hp <= 0:
                print('Par')
                quit()

        # if you choose to spell
        elif action.lower() == 's':
            if user_mp > 0:
                if user_name == 'Hero':
                    user_spell = random.randint(1, 20)
                else:
                    user_spell = random.randint(1, 60)

                user_hp = user_hp - computer_att
                computer_hp = computer_hp - user_spell
                user_mp = user_mp - 10
                print('You made ' + str(user_spell) + ' hit')
                print('Enemy: ' + str(computer_hp) + ' hp.')
                print('The enemy made ' + str(computer_att) + ' hit.')
                print('User: ' + str(user_hp) + ' hp')
                print()

                if user_hp <= 0 and computer_hp > 0:
                    print('You lose')
                    quit()
                elif computer_hp <= 0 and user_hp > 0:
                    print('You won')
                    rest(user_name, user_hp, user_mp)
                elif computer_hp <= 0 and user_hp <= 0:
                    print('Par')
                    quit()

            else:
                user_hp = user_hp - computer_att
                print("You don't have enough mp")
                print('The ennemy made you ' + str(computer_att) + 'hit.')
                print('User: ' + str(user_hp) + 'hp')
                print()

        elif action.lower() == 'e':
            quit()
        else:
            print('Invalid command')


# Inn
def rest(user_name, user_hp, user_mp):
    print('''---------------------------------------------------------------------------

    After the fight you arrived to an Inn
    Here you can [R]est (gives 50 hp), [T]ake a potion (gives 60 mp), [C]ontinue or [Q]uit the game

    ''')
    inn_rep = input('What would you do?: ')
    print('---------------------------------------------------------------------------')
    if inn_rep.lower() == 'r':
        user_hp = user_hp + 50
    elif inn_rep.lower() == 't':
        user_mp = user_mp + 60
    elif inn_rep.lower() == 'c':
        fight(user_name, user_hp, user_mp)
    elif inn_rep.lower() == 'q':
        quit()
    else:
        print('Invalid command')

    print('You now have ' + str(user_hp) + ' hp and ' + str(user_mp) + ' mp')
    fight(user_name, user_hp, user_mp)


# Game Loop
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

           hp  /  mp  / att. max / spell max att. 
        /------/------/----------/----------------/
  Hero  :  200 /  30  /    60    /      20        /
        /------/------/----------/----------------/
Wizzard :  150 /  80  /    30    /      60        /
        /------/------/----------/----------------/

[H]ero / [W]izzard : ''')
        if char.lower() == 'h':
            user_name = 'Hero'
            user_hp = 200
            user_mp = 30
            print('You selected the ' + user_name + ' !')
            fight(user_name, user_hp, user_mp)
        elif char.lower() == 'w':
            user_name = 'Wizzard'
            user_hp = 150
            user_mp = 80
            print('You selected the ' + user_name + ' !')
            fight(user_name, user_hp, user_mp)

    if start.lower() == 'n':
        quit()

    else:
        print()
        print('Invalid entry')
