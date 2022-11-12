from utils_solver_sudoku import is_valid_cross, is_valid_square



def free_slot(board):
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            if col == ".": return (y,x)

def recur(board):
    try:
        y, x = free_slot(board)
    except:
        return True
    for i in range(9):
        pick = str(i+1)
        if is_valid_cross(board, (y,x), pick) and is_valid_square(board, (y,x), pick):
            board[y][x] = pick
            if recur(board): return True
            board[y][x] = "."
        
def sudoku_printer(board):
    giga_count = 0
    for _ in range(25):
        print("-", end="")
    print()        
    for row in board:
        print("|",end=" ")
        count = 0
        for n in row:
            print(n, end=" ")
            count += 1
            if count == 3:
                count = 0
                print("|",end=" ")
        giga_count += 1
        print()
        if giga_count == 3:
            giga_count = 0
            for _ in range(25):
                print("-", end="")
            print()


if __name__=="__main__":
    board = [
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
    ]
    try:
        y, x = 0, 0
        while True:
            if y == 8 and x == 9:
                raise EOFError
            if x > 8:
                x = 0
                y += 1
            if x < 0:
                x = 8
                y -= 1
            board[y][x] = "_"
            print(chr(27) + "[2J")
            sudoku_printer(board)
            inp = input()
            if inp == "^[[A":
                board[y][x] = "."
                if y > 0:
                    y -= 1
                else:
                    continue
            elif inp == "^[[C":
                board[y][x] = "."
                x += 1
            elif inp == "^[[B":
                board[y][x] = "."
                if y < 8:
                    y += 1
                else:
                    continue
            elif inp == "^[[D":
                board[y][x] = "."
                x -= 1
            elif not inp:
                board[y][x] = "."
                x += 1
            elif inp == "r":
                board[y][x] = "."
                x -= 1
            else:
                board[y][x] = inp
                x += 1
    except EOFError:
        board[y][x]="."
        print("solving.....")

    recur(board)
    sudoku_printer(board)