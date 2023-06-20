import random

player_score = 0
computer_score = 0

 # create board
def create_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("________")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("________")
    print(board[6] + "|" + board[7] + "|" + board[8])


# take player input
def player_input(board):
    while True:
        choice = int(input("pick a position from cell 1 to 9: "))
        if choice  >=1 and choice <= 9 and board[choice-1]=="-":
            board[choice-1] = current_player
            break

        else:
            print('Oops, that spot has been taken')






# check if player win or a tie
def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return  True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True

def check_winner():
    global game_running , player_score, computer_score
    if check_horizontal(board) or check_vertical(board) or check_diagonal(board):
        print(f"The winner is {winner}")
        if winner == 'x':
            player_score += 1
        elif winner == 'o':
            computer_score +=1

        print(f"player score {player_score}")
        print(f'Computer score {computer_score}')

        create_board(board)
        game_running = False






def check_tie(board):
    global game_running
    if "-" not in board:
        print("It is a tie .Game Over")
        create_board(board)
        game_running = False

# switch player
def switch_player():
    global current_player
    if current_player == "x":
        current_player = "o"
    else:
        current_player = 'x'


def computer_play(board):
    while current_player =='o':
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = 'o'
            switch_player()
            break




while True:
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    current_player = "x"
    winner = None
    game_running = True

    while game_running:
        create_board(board)
        player_input(board)
        check_winner()
        check_tie(board)

        if game_running:
            switch_player()
            computer_play(board)
            check_winner()
            check_tie(board)

    play_again = input('do you want play again? yes/no')
    if play_again.lower() != 'yes':
        break
    print('FINAL SCORES')
    print(f"player score{player_score}")
    print(f'Computer score{computer_score}')


