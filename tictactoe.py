board = [' ']*9
player = 'X'

def print_board():
    print(f"{board[0]}|{board[1]}|{board[2]}\n-+-+-\n{board[3]}|{board[4]}|{board[5]}\n-+-+-\n{board[6]}|{board[7]}|{board[8]}")

def win(p):
    return (board[0]==board[1]==board[2]==p or
            board[3]==board[4]==board[5]==p or
            board[6]==board[7]==board[8]==p or
            board[0]==board[3]==board[6]==p or
            board[1]==board[4]==board[7]==p or
            board[2]==board[5]==board[8]==p or
            board[0]==board[4]==board[8]==p or
            board[2]==board[4]==board[6]==p)

while True:
    print_board()
    pos = int(input(f"{player} move (0-8): "))
    board[pos] = player
    if win(player):
        print_board()
        print(f"{player} wins!")
        break
    player = 'O' if player=='X' else 'X'
    if ' ' not in board:
        print("Draw!")
        break
