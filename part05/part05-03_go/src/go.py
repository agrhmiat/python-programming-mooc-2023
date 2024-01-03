# Write your solution here

def who_won(game_board: list) -> int:
    player1_piece = 0
    player2_piece = 0
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 1:
                player1_piece += 1
            elif game_board[i][j] == 2:
                player2_piece += 1
    if player1_piece > player2_piece:
        return 1
    elif player2_piece > player1_piece:
        return 2
    else:
        return 0
