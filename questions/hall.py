hall = (('.','.','.','.','B','.','.','.','.','.','.'),
        ('#','#','A','#','.','#','C','#','D','#','#'),
        ('#','#','A','#','B','#','C','#','D','#','#'))

def terminal(hall):
    for i in range(1,3):
        if (hall[i][2] != 'A' or hall[i][2] != 'A') or \
           (hall[i][4] != 'B' or hall[i][4] != 'B') or \
           (hall[i][6] != 'C' or hall[i][6] != 'C') or \
           (hall[i][8] != 'D' or hall[i][8] != 'D'):
            return False
    return True

def make_move(hall, action):
    new_hall = list(map(list, hall))
    y1, x1 = action[1]
    y2, x2 = action[2]
    new_hall[y2][x2] = action[0]
    new_hall[y1][x2] = '.'
    return tuple(map(tuple, new_hall))

def find_actions(hall):
    actions = set()
    for y in range(len(hall)):
        for x in range(len(hall[0])):
            if hall[y][x] == '.':
                if y < len(hall)-1:
                    if hall[y+1][x].isalpha():
                        actions.add((hall[y+1][x], (y+1,x), (y,x)))
                if y > 0:
                    if hall[y-1][x].isalpha():
                        actions.add((hall[y-1][x], (y-1,x), (y,x)))
                if x < len(hall[0])-1:
                    if hall[y][x+1].isalpha():
                        actions.add((hall[y][x+1], (y,x+1), (y,x)))
                if x > 0:
                    if hall[y][x-1].isalpha():
                        actions.add((hall[y][x-1], (y,x-1), (y,x)))
    return actions

new_hall = list(map(list,hall))
print(hall)