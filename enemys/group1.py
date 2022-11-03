import random
from inn.camp1 import rest1


def fight1(user_name, user_hp, user_mp):
    print('---------------------------------------------------------------------------')
    print('You selected the ' + user_name + ' !')
    print('Your first enemy is a bat')
    print('30 attack max, 40 hp')

    computer_hp = 40

    while True:
        computer_att = random.randint(1, 30)
        print('---------------------------------------------------------------------------')
        print('Actual status : ' + str(user_name) + ' / ' + str(user_hp) + 'hp / ' + str(user_mp) + 'mp /')
        action = input('Select an action : [A]ttack, [S]pell, [E]xit: ')
        print('---------------------------------------------------------------------------')
        print()
        if user_hp > 0:

            # if you choose to attack
            if action.lower() == 'a':

                # for the Hero
                if user_name == 'Hero':
                    user_att = random.randint(1, 60)
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
                        print('You won !')
                        break
                    elif computer_hp <= 0 and user_hp <= 0:
                        print('Par')
                        quit()

                # for the Wizard
                elif user_name == 'Wizard':
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
                        print('You won !')
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
                        print('You made ' + str(user_spell) + ' hit')
                        print('Enemy: ' + str(computer_hp) + ' hp.')
                        print('The enemy made ' + str(computer_att) + ' hit.')
                        print('User: ' + str(user_hp) + ' hp')
                        print()

                        if user_hp <= 0 and computer_hp > 0:
                            print('You lose')
                            quit()
                        elif computer_hp <= 0 and user_hp > 0:
                            print('You won !')
                            break
                        elif computer_hp <= 0 and user_hp <= 0:
                            print('Par')
                            quit()

                    # for the Wizard
                    elif user_name == 'Wizard':
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
                            print('You won !')
                            break
                        elif computer_hp <= 0 and user_hp <= 0:
                            print('Par')
                            quit()

                else:
                    user_hp = user_hp - computer_att
                    print("You don't have enough mp")
                    print('The enemy made you ' + str(computer_att) + ' hit.')
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
            print('You won !')
            break
        elif computer_hp <= 0 and user_hp <= 0:
            print('Par')
            quit()

    # second enemy
    print('---------------------------------------------------------------------------')
    print('Your next enemy is a rat')
    print('60 attack max, 80 hp')

    computer_hp = 80

    while True:
        computer_att = random.randint(1, 60)
        print('---------------------------------------------------------------------------')
        print('Actual status : ' + str(user_name) + ' / ' + str(user_hp) + 'hp / ' + str(user_mp) + 'mp /')
        action = input('Select an action : [A]ttack, [S]pell, [E]xit: ')
        print('---------------------------------------------------------------------------')
        print()

        if user_hp > 0:

            # if you choose to attack
            if action.lower() == 'a':

                # for the Hero
                if user_name == 'Hero':
                    user_att = random.randint(1, 60)
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
                        print('You won !')
                        break
                    elif computer_hp <= 0 and user_hp <= 0:
                        print('Par')
                        quit()

                # for the Wizard
                elif user_name == 'Wizard':
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
                        print('You won !')
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
                        print('You made ' + str(user_spell) + ' hit')
                        print('Enemy: ' + str(computer_hp) + ' hp.')
                        print('The enemy made ' + str(computer_att) + ' hit.')
                        print('User: ' + str(user_hp) + ' hp')
                        print()

                        if user_hp <= 0 and computer_hp > 0:
                            print('You lose')
                            quit()
                        elif computer_hp <= 0 and user_hp > 0:
                            print('You won !')
                            break
                        elif computer_hp <= 0 and user_hp <= 0:
                            print('Par')
                            quit()

                    # for the Wizard
                    elif user_name == 'Wizard':
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
                            print('You won !')
                            break
                        elif computer_hp <= 0 and user_hp <= 0:
                            print('Par')
                            quit()

                else:
                    user_hp = user_hp - computer_att
                    print("You don't have enough mp")
                    print('The enemy made you ' + str(computer_att) + ' hit.')
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
            print('You won !')
            break
        elif computer_hp <= 0 and user_hp <= 0:
            print('Par')
            quit()

    rest1(user_hp, user_mp)
