# Game start function

def game_start():

       
    global Player1
    global Player2
    global player_turn
    global player_marker
    global win
    
    Player1 = 'filler'
    Player2 = 'filler'
    player_turn = 'Player 2'
    player_marker = ' '
    win = False

    global row1
    global row2
    global row3
    global available_slots

    row1 = ['7','8','9']
    row2 = ['4','5','6']
    row3 = ['1','2','3']
    available_slots = [1,2,3,4,5,6,7,8,9]
    

    game_setup()

    while win == False:

        game_turn()

        win_condition()


# Choose player symbols and start game

def game_setup():
    
    global Player1
    global Player2
    global player_turn
    global player_marker
    global win
    
    global row1
    global row2
    global row3
    global available_slots
    
    
    while Player1 != 'X' and Player1 != 'O':
        Player1 = input("Player 1: Would you like to be X or O?: ")
        Player1 = Player1.upper()
        if Player1 != 'X' and Player1 != 'O':
            print('\n')
            print("Please type X or O")
            print('\n')
        else:
            if Player1 == 'X':
                Player2 = 'O'
                player_marker = Player2
            else:
                Player2 = 'X'
                player_marker = Player2
            print('\n')
            print(f'Player 1 is {Player1}')
            print('\n')
            print(f'Player 2 is {Player2}')
            print("\n")

# Build out game board

def display_board():
    
    global Player1
    global Player2
    global player_turn
    global player_marker
    global win
    
    global row1
    global row2
    global row3
    global available_slots

    print("\n")
    print(f' {row1[0]} | {row1[1]} | {row1[2]}')
    print('-----------')
    print(f' {row2[0]} | {row2[1]} | {row2[2]}')
    print('-----------')
    print(f' {row3[0]} | {row3[1]} | {row3[2]}')
    print("\n")

# Player turns 

def game_turn():
    
    global Player1
    global Player2
    global player_turn
    global player_marker
    global win
    
    global row1
    global row2
    global row3
    global available_slots

    slot_selection = ' '

    if player_turn == 'Player 2':
        player_turn = 'Player 1'
        player_marker = Player1
    else:
        player_turn = 'Player 2'
        player_marker = Player2

    display_board()

    while slot_selection not in available_slots:
        slot_selection = int(input(f'{player_turn}, please select an available slot: '))
        if slot_selection in available_slots:
            if slot_selection == 1:
                row3[0] = player_marker
                available_slots.remove(1)
                break
            elif slot_selection == 2:
                row3[1] = player_marker
                available_slots.remove(2)
                break
            elif slot_selection == 3:
                row3[2] = player_marker
                available_slots.remove(3)
                break
            elif slot_selection == 4:
                row2[0] = player_marker
                available_slots.remove(4)
                break
            elif slot_selection == 5:
                row2[1] = player_marker
                available_slots.remove(5)
                break
            elif slot_selection == 6:
                row2[2] = player_marker
                available_slots.remove(6)
                break
            elif slot_selection == 7:
                row1[0] = player_marker
                available_slots.remove(7)
                break
            elif slot_selection == 8:
                row1[1] = player_marker
                available_slots.remove(8)
                break
            else:
                row1[2] = player_marker
                available_slots.remove(9)
                break
        else:
            print('\n')
            print("That is not an available slot!")
            print('\n')
            display_board()
            print('\n')
    
            
# Check for win condition

def win_condition():
    
    global Player1
    global Player2
    global player_turn
    global player_marker
    global win
    
    global row1
    global row2
    global row3
    global available_slots

    while win == False:
        if row1[0] == row1[1] == row1[2]:
            win = True
            break
        elif row2[0] == row2[1] == row2[2]:
            win = True
            break
        elif row3[0] == row3[1] == row3[2]:
            win = True
            break
        elif row1[0] == row2[0] == row3[0]:
            win = True
            break
        elif row1[1] == row2[1] == row3[1]:
            win = True
            break
        elif row1[2] == row2[2] == row3[2]:
            win = True
            break
        elif row1[0] == row2[1] == row3[2]:
            win = True
            break
        elif row3[0] == row2[1] == row1[2]:
            win = True
            break
        elif len(available_slots) == 0:
            print('\n')
            print('Draw!!')
            print('\n')
            display_board()
            print('\n')
            print('GAME OVER')
            print('\n')
            quit()
        else:
            break

    if win == True:
        print("\n")
        print(f'{player_turn} is the winner!!!')
        print('\n')
        display_board()
        print('\n')
        print('GAME OVER')
        print('\n')
        quit()
    else:
        return 

game_start()
