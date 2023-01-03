import random as r
import time as t
game=True
def end():
    a=input('Do you want to play again? (y/n): ')
    if a=='y':
        return t.sleep(1),print('\n'*2)
    elif a=='n':
        return exit()
    else: print('Wrong anwser!'),end()
def check(a,b):
    if a>=21:
        if b=='Human':
            return print('\n\n\nYOU LOSE!!!'),t.sleep(3)
        else:
            return print('\n\n\nYOU WON!!!'),t.sleep(3)
while game==True:
    if r.randint(0,1)==0:
        current_player='Human'
        print('You go first')
        t.sleep(1)
    else:
        current_player='Computer'
        print('Computer go first')
        t.sleep(1)
    player_choice=0
    current_number=0
    choice=[1,2,3]
    while current_number<21:
        if current_player=='Human':
            while True:
                player_choice=int(input('Add a number from 1 to 3: '))
                t.sleep(1)   
                if player_choice in choice:
                    break              
                else:
                    print('Wrong choice. Do it again.')
                    t.sleep(1)
            current_number+=player_choice
            print('The current sum now is:',current_number)
            t.sleep(1)
            check(current_number,current_player)
            current_player='Computer'
        else:
            player_choice=r.randint(1,3)
            current_number+=player_choice
            print('Computer add',player_choice)
            t.sleep(1)
            print('The current sum now is:',current_number)
            t.sleep(1)
            check(current_number,current_player)
            current_player='Human'
    else: end()