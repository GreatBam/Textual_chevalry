# Jonathan, 11.03.22
import random

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
Wizzard :  150 /  80  /    30    /      60        /
        /------/------/----------/----------------/
[H]ero / [W]izzard : ''')
        if char.lower() == 'h':
            user_name = 'Hero'
            user_hp = 200
            user_mp = 30
            user_att = random.randint(1, 60)
            user_spell = random.randint(1, 20)
            break
        elif char.lower() == 'w':
            user_name = 'Wizzard'
            user_hp = 150
            user_mp = 80
            user_att = random.randint(1, 30)
            user_spell = random.randint(1, 60)
            break

    if start.lower() == 'n':
        quit()

    else:
        print('Invalid entry')


# introducing first ennemy
print('---------------------------------------------------------------------------')
print('You selected the ' + user_name + ' !')
print('Your first ennemy is a bat')
print('40 attack max, 60 hp')
print('---------------------------------------------------------------------------')


# first fight loop
computer_hp = 60
while True:
    computer_att = random.randint(1, 40)
    print('Actual status : ' + str(user_name) + ' / ' + str(user_hp) + 'hp / ' + str(user_mp) + 'mp /')
    action = input('Select an action : [A]ttack, [S]pell, [E]xit: ')
    print()
    if user_hp > 0 and computer_hp > 0:

        # if you choose to attack
        if action.lower() == 'a':

            # for the Hero
            if user_name == 'Hero':
                user_att = random.randint(1, 60)
                user_hp = user_hp - computer_att
                computer_hp = computer_hp - user_att
                print('You made ' + str(user_att) + 'hit and the ennemy ' + str(computer_att) + 'hit.')
                print('User: ' + str(user_hp) + ' hp')
                print('Ennemy: ' + str(computer_hp) + ' hp.')
                print()

                if user_hp <= 0 and computer_hp > 0:
                    print('You lose')
                    quit()
                elif computer_hp <= 0 and user_hp > 0:
                    print('You won')
                    break
                elif computer_hp <= 0 and user_hp <= 0:
                    print('Par')
                    quit()

            # for the Wizzard
            elif user_name == 'Wizzard':
                user_att = random.randint(1, 30)
                user_hp = user_hp - computer_att
                computer_hp = computer_hp - user_att
                print('You made ' + str(user_att) + 'hit and the ennemy ' + str(computer_att) + 'hit.')
                print('User: ' + str(user_hp) + ' hp')
                print('Ennemy: ' + str(computer_hp) + ' hp.')
                print()

                if user_hp <= 0 and computer_hp > 0:
                    print('You lose')
                    quit()
                elif computer_hp <= 0 and user_hp > 0:
                    print('You won')
                    break
                elif computer_hp <= 0 and user_hp <= 0:
                    print('Par')
                    quit()

        # if you choose to spell
        elif action.lower() == 's':
            if user_mp > 0:

                # for the Hero
                if user_name == 'Hero':
                    user_spell = random.randint(1, 20)
                    user_hp = user_hp - computer_att
                    computer_hp = computer_hp - user_spell
                    user_mp = user_mp - 10
                    print('You made ' + str(user_spell) + 'hit and the ennemy ' + str(computer_att) + 'hit.')
                    print('User: ' + str(user_hp) + ' hp / ' + str(user_mp) + ' mp')
                    print('Ennemy: ' + str(computer_hp) + ' hp.')
                    print()

                    if user_hp <= 0 and computer_hp > 0:
                        print('You lose')
                        quit()
                    elif computer_hp <= 0 and user_hp > 0:
                        print('You won')
                        break
                    elif computer_hp <= 0 and user_hp <= 0:
                        print('Par')
                        quit()

                # for the Wizzard
                elif user_name == 'Wizzard':
                    user_spell = random.randint(1, 60)
                    user_hp = user_hp - computer_att
                    computer_hp = computer_hp - user_spell
                    user_mp = user_mp - 10
                    print('You made ' + str(user_spell) + 'hit and the ennemy ' + str(computer_att) + 'hit.')
                    print('User: ' + str(user_hp) + ' hp / ' + str(user_mp) + ' mp')
                    print('Ennemy: ' + str(computer_hp) + ' hp.')
                    print()

                    if user_hp <= 0 and computer_hp > 0:
                        print('You lose')
                        quit()
                    elif computer_hp <= 0 and user_hp > 0:
                        print('You won')
                        break
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

    elif user_hp <= 0 and computer_hp > 0:
        print('You lose')
        quit()
    elif computer_hp <= 0 and user_hp > 0:
        print('You won')
        break
    elif computer_hp <= 0 and user_hp <= 0:
        print('Par')
        quit()


# introducing second ennemy
print('---------------------------------------------------------------------------')
print('Your next ennemy is a rat')
print('80 attack max, 100 hp')
print('---------------------------------------------------------------------------')


# second fight loop
computer_hp = 100
while True:
    computer_att = random.randint(1, 80)
    print('Actual status : ' + str(user_name) + ' / ' + str(user_hp) + 'hp / ' + str(user_mp) + 'mp /')
    action = input('Select an action : [A]ttack, [S]pell, [E]xit: ')
    print()
    if user_hp > 0 and computer_hp > 0:

        # if you choose to attack
        if action.lower() == 'a':

            # for the Hero
            if user_name == 'Hero':
                user_att = random.randint(1, 60)
                user_hp = user_hp - computer_att
                computer_hp = computer_hp - user_att
                print('You made ' + str(user_att) + 'hit and the ennemy ' + str(computer_att) + 'hit.')
                print('User: ' + str(user_hp) + ' hp')
                print('Ennemy: ' + str(computer_hp) + ' hp.')
                print()

                if user_hp <= 0 and computer_hp > 0:
                    print('You lose')
                    quit()
                elif computer_hp <= 0 and user_hp > 0:
                    print('You won')
                    break
                elif computer_hp <= 0 and user_hp <= 0:
                    print('Par')
                    quit()

            # for the Wizzard
            elif user_name == 'Wizzard':
                user_att = random.randint(1, 30)
                user_hp = user_hp - computer_att
                computer_hp = computer_hp - user_att
                print('You made ' + str(user_att) + 'hit and the ennemy ' + str(computer_att) + 'hit.')
                print('User: ' + str(user_hp) + ' hp')
                print('Ennemy: ' + str(computer_hp) + ' hp.')
                print()

                if user_hp <= 0 and computer_hp > 0:
                    print('You lose')
                    quit()
                elif computer_hp <= 0 and user_hp > 0:
                    print('You won')
                    break
                elif computer_hp <= 0 and user_hp <= 0:
                    print('Par')
                    quit()

        # if you choose to spell
        elif action.lower() == 's':
            if user_mp > 0:

                # for the Hero
                if user_name == 'Hero':
                    user_spell = random.randint(1, 20)
                    user_hp = user_hp - computer_att
                    computer_hp = computer_hp - user_spell
                    user_mp = user_mp - 10
                    print('You made ' + str(user_spell) + 'hit and the ennemy ' + str(computer_att) + 'hit.')
                    print('User: ' + str(user_hp) + ' hp / ' + str(user_mp) + ' mp')
                    print('Ennemy: ' + str(computer_hp) + ' hp.')
                    print()

                    if user_hp <= 0 and computer_hp > 0:
                        print('You lose')
                        quit()
                    elif computer_hp <= 0 and user_hp > 0:
                        print('You won')
                        break
                    elif computer_hp <= 0 and user_hp <= 0:
                        print('Par')
                        quit()

                # for the Wizzard
                elif user_name == 'Wizzard':
                    user_spell = random.randint(1, 60)
                    user_hp = user_hp - computer_att
                    computer_hp = computer_hp - user_spell
                    user_mp = user_mp - 10
                    print('You made ' + str(user_spell) + 'hit and the ennemy ' + str(computer_att) + 'hit.')
                    print('User: ' + str(user_hp) + ' hp / ' + str(user_mp) + ' mp')
                    print('Ennemy: ' + str(computer_hp) + ' hp.')
                    print()

                    if user_hp <= 0 and computer_hp > 0:
                        print('You lose')
                        quit()
                    elif computer_hp <= 0 and user_hp > 0:
                        print('You won')
                        break
                    elif computer_hp <= 0 and user_hp <= 0:
                        print('Par')
                        quit()

            else:
                print("You don't have enough mp")
                print()

        elif action.lower() == 'e':
            quit()
        else:
            print('Invalid command')

    elif user_hp <= 0 and computer_hp > 0:
        print('You lose')
        quit()
    elif computer_hp <= 0 and user_hp > 0:
        print('You won')
        break
    elif computer_hp <= 0 and user_hp <= 0:
        print('Par')
        quit()

# ending
print()
print('Congratulations !')
print()
print('Thanks for playing')
