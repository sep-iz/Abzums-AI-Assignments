#information : Sepeta Zibaei / assignment-4(HW4) / python project-1
#email : sepz821mds@gmail.com
#github-account : github.com/sep-iz

#step 1 : initialize the game board
game_board = ["-" for _ in range(9)]
print(game_board)
#step 2 : display the game board 
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
game_board = ["-" for _ in range(9)]
display_board(game_board)

#step 3 : define the players
def define_players():
    while True :
        player1_Symbol = input("please choose a symbol,player1").upper()
        if player1_Symbol not in ['X', 'O']:
            print("invalid input. please choose either X or O.")
            continue
        else:
            break
    if player1_Symbol == "X":
        player2_symbol = "O"
        print("player1 chose X and player2 chose O.")
    else:
        player2_symbol = "X"
        print("player1 chose O and player2 chose X.")
    current_player_symbol = player1_Symbol
    return player1_Symbol,player2_symbol,current_player_symbol
player1, player2, current_player = define_players()
print(f"Player 1: {player1}")
print(f"Player 2: {player2}")
print(f"Current Player (starter): {current_player}")
#step 4 :creating a player move function
def make_player_move(current_player_symbol, board):
    while True:
        try:
            player_input = input(f"player{current_player_symbol} please choose a number from 1 to 9.")
            if not player_input.isdigit():
                print("invalid input. please choose a number from 1 to 9.")
                continue
            player_choice = int(player_input)
            board_index = player_choice - 1
            if not (0 <= board_index <= 8):
                print("the number should be between 1 to 9")
                continue
            if board[board_index] != '-':
                print("this part has been taken. please choose another part.")
                continue
            board[board_index] = current_player_symbol
            break
        except ValueError:
            print("invalid input. please choose a number from 1 to 9.")
        except Exception as e:
            print(f"an error occured {e}")
#step 5 : checking for a winner
def check_for_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]

     ]
    for combo in winning_combinations:
        pos1 = board[combo[0]]
        pos2 = board[combo[1]]
        pos3 = board[combo[2]]
        if pos1 == pos2 == pos3 and pos1 != '-':
            return pos1 
    if '-' not in board:
        return 'Tie'
    return 'Game On'
#step 6 : flip the current player 
def flip_player(current_player_symbol):
    if current_player_symbol == 'X':
        return 'O'
    else:
        return 'X'
#step 7 : playing the game
def play_game():
    game_board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    player1_symbol, player2_symbol, current_player = define_players()
    print(f"\n the game just started !🙂 player1 :{player1_symbol}, player2:{player2_symbol} ")
    print(f"starter player :{current_player}")
    game_running = True
    while game_running:
        display_board(game_board)
        make_player_move(current_player, game_board)
        game_status = check_for_winner(game_board)
        if game_status == 'X' or game_status == 'O':
            display_board(game_board)
            print(f"congrats!🥳 the {game_status} has win the game!")
            game_running = False
        elif game_status == 'Tie':
            display_board(game_board)
            print("the game is a tie !")
            game_running = False
        else:
            current_player = flip_player(current_player)
if __name__ == "__main__":
    play_game()

            
        

        
        
        










    
        
    
        




    