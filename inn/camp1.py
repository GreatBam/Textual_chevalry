def rest1(user_hp, user_mp):
    while True:
        print('''---------------------------------------------------------------------------
    After the fight you arrived to an Inn
    Here you can [R]est (gives hp), [T]ake a potion (gives mp), [C]ontinue or [Q]uit the game
        ''')
        inn_rep = input('What would you do?: ')
        print('---------------------------------------------------------------------------')
        if inn_rep.lower() == 'r':
            user_hp = user_hp + 50
            print('You now have ' + str(user_hp) + ' hp')
        elif inn_rep.lower() == 't':
            user_mp = user_mp + 60
            print('You now have ' + str(user_mp) + ' mp')
        elif inn_rep.lower() == 'c':
            print('Coming Soon !')
        elif inn_rep.lower() == 'q':
            quit()
