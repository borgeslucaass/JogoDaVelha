from random import randrange


def show_board():
    print("""
    +-------+-------+-------+
    |       |       |       |
    |   {}   |   {}   |   {}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {}   |   {}   |   {}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {}   |   {}   |   {}   |
    |       |       |       |
    +-------+-------+-------+ """ .format(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]))


def jogo(jogada):
    global board
    board = [1, 2, 3, \
             4, 'x', 6, \
             7, 8, 9]
    vitoria = check_victory()
    while vitoria is False:
        while jogada not in board:
            jogada = int(input('Qual quadrante deseja jogar?'))
        else:
            board[jogada - 1] = 'o'

        vitoria = check_victory()
        if vitoria is True:
            show_board()
            show_victory()
            break

        velha = check_velha()
        if velha is True:
            show_board()
            print('DEU VELHA!!!')
            break

        pc = randrange(1, 9)
        while pc not in board:
            pc = randrange(1, 9)
        else:
            board[pc - 1] = 'x'

        velha = check_velha()
        if velha is True:
            show_board()
            print('DEU VELHA!!!')
            break
        else:
            vitoria = check_victory()
            if vitoria is True:
                show_board()
                show_victory()
                break
            else:
                show_board()
                jogada = int(input('Qual quadrante deseja jogar?'))

    # show_board()
    # check_victory()


def check_victory():

    if board[0] == 'o' and board[1] == 'o' and board[2] == 'o' or \
            board[2] == 'o' and board[5] == 'o' and board[8] == 'o' or \
            board[6] == 'o' and board[7] == 'o' and board[8] == 'o' or \
            board[0] == 'o' and board[3] == 'o' and board[6] == 'o':
        return True

    if board[0] == 'x' and board[1] == 'x' and board[2] == 'x' or \
            board[2] == 'x' and board[5] == 'x' and board[8] == 'x' or \
            board[6] == 'x' and board[7] == 'x' and board[8] == 'x' or \
            board[0] == 'x' and board[3] == 'x' and board[6] == 'x' or \
            board[2] == 'x' and board[4] == 'x' and board[6] == 'x' or \
            board[0] == 'x' and board[4] == 'x' and board[8] == 'x' or \
            board[1] == 'x' and board[4] == 'x' and board[7] == 'x' or \
            board[3] == 'x' and board[4] == 'x' and board[5] == 'x':
        return True
    else:
        return False


def show_victory():
    if board[0] == 'o' and board[1] == 'o' and board[2] == 'o' or \
            board[2] == 'o' and board[5] == 'o' and board[8] == 'o' or \
            board[6] == 'o' and board[7] == 'o' and board[8] == 'o' or \
            board[0] == 'o' and board[3] == 'o' and board[6] == 'o':
        print('VOCÊ VENCEU!!!')

    if board[0] == 'x' and board[1] == 'x' and board[2] == 'x' or \
            board[2] == 'x' and board[5] == 'x' and board[8] == 'x' or \
            board[6] == 'x' and board[7] == 'x' and board[8] == 'x' or \
            board[0] == 'x' and board[3] == 'x' and board[6] == 'x' or \
            board[2] == 'x' and board[4] == 'x' and board[6] == 'x' or \
            board[0] == 'x' and board[4] == 'x' and board[8] == 'x' or \
            board[1] == 'x' and board[4] == 'x' and board[7] == 'x' or \
            board[3] == 'x' and board[4] == 'x' and board[5] == 'x':
        print('VOCÊ PERDEU!!!')


def check_velha():

    if 1 not in board and 2 not in board and 3 not in board and 4 not in board and 5 not in board and 6 not in board and 7 not in board and 8 not in board and 9 not in board:
        return True
    else:
        return False


print("""
    +-------+-------+-------+
    |       |       |       |
    |   1   |   2   |   3   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   4   |   x   |   6   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   7   |   8   |   9   |
    |       |       |       |
    +-------+-------+-------+ """)
jogo(int(input("Qual quadrante deseja jogar? ")))

print("A casa caiu!!")

