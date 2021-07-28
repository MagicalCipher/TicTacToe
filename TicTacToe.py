#creating board using dict so we can easily put stuff on the board
#credit to https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874
#tutorial followed by Magical Cipher
print("Board goes with keypad- youknow the 3by3 one going 12345... and so on\nAnyways this is 2 player- not with a bot, with other irl people")
theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys= []
for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


#actually playing the game
def game():
    while True:
        turn = 'X' #this when you r x
        count = 0
        for i in range(10):
            printBoard(theBoard) #prints board

            print("It's your turn," + turn + ".Move to which place?")

            move=input() #insert your move

            if theBoard[move] == ' ': #is there a space?
                theBoard[move]= turn #your turn is what you just inputted
                count +=1
            else:
                print("That place is already filled. Move to which other place?")
                if turn == 'X':
                    turn = 'O'  # changing turns
                else:
                    turn = 'X'

    # Now we will check if player X or O has won,for every move after 5 moves.
            if count > 1: #why if count is greater than 5??
                if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # ughh implementing every possible winnigng position
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                    printBoard(theBoard)
                    print("\nGame Over.\n")
                    print(" **** " + turn + " won. ****")
                    break
            if count==9: #all moves have been made but nobody won sooooo
                print("\nGame Over.\n")
                print("It's a Tie")
                break

            if turn=='X':
                turn='O' #changing turns
            else:
                turn='X'

        restart = input("Do you want to play again? y/n: ")
        if restart.lower() == "y":
            for key in board_keys:
                theBoard[key]= " "
        else:
            print("Well bye then :(")
            break

if __name__ == "__main__":
    game()