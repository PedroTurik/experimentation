# Interview graph problem from 
# https://www.youtube.com/watch?v=4tYoVx0QoN0&ab_channel=Cl%C3%A9mentMihailescu

# It clean a matrix (in-place) from all its islands. 
# An island is a cluster of 1s that has no connection with a border.

# The code work by first running a DFS algorithm that marks every cell that it touches,
# and it can only keep searching through a connection of 1s.

# mark_land() is run at every border index, and then we clean the unmarked 1s

matrix= [
    [1, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 0]
]


Y = len(matrix)
X = len(matrix[0])


def mark_land(y, x):
    if matrix[y][x] == 1:
        matrix[y][x] = 2
        if y > 0: mark_land(y-1, x)
        if y < Y-1: mark_land(y+1, x)
        if x > 0: mark_land(y, x-1)
        if x < X-1: mark_land(y, x+1)

def remove_islands(matrix):
    for y in range(Y):
        for x in range(X):
            if y == Y-1 or x == X-1 or y == 0 or x == 0:
                mark_land(y, x)

    for y in range(Y):
        for x in range(X):
            matrix[y][x] = 1 if matrix[y][x] == 2 else 0

    return matrix

if __name__=="__main__":
    remove_islands(matrix)
    print(matrix)

