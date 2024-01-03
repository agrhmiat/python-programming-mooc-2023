# Write your solution here

def play_turn(game_board: list, x: int, y: int, piece: str) -> bool:
    for i in range(len(game_board)):
        if i != y:
            continue
        for j in range(len(game_board[i])):
            if j != x:
                continue
            if game_board[i][j] == "":
                game_board[i][j] = piece
                return True
    return False

if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)
