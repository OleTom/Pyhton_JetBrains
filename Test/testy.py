board = [['8|', '_', '_', '_', '_', '_', '_', '_', '_', '|'],
         ['7|', '_', '_', '_', '_', '_', '_', '_', '_', '|'],
         ['6|', '_', '_', '_', '_', '_', '_', '_', '_', '|'],
         ['5|', '_', '_', '_', '_', '_', '_', '_', '_', '|'],
         ['4|', '_', '_', '_', '_', '_', '_', '_', '_', '|'],
         ['3|', '_', '_', '_', '_', '_', '_', '_', '_', '|'],
         ['2|', '_', '_', '_', '_', '_', '_', '_', '_', '|'],
         ['1|', '_', '_', '_', '_', '_', '_', '_', '_', '|']]


def print_board():
    print("  -------------------")
    for row in board:
        for char in row:
            print(' {}'.format(char), end='')
        print('')
    print("  -------------------")
    print('    1 2 3 4 5 6 7 8')


print_board()
