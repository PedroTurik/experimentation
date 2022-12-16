from random import randint
from time import time
matrix = [
    [96, 81, 87, 99, 66, 73, 58, 44, 79, 65, 44, 4, 51, 29, 11], 
    [56, 10, 24, 81, 64, 49, 19, 42, 2, 31, 87, 31, 6, 56, 28], 
    [20, 59, 48, 64, 91, 64, 46, 90, 34, 15, 96, 94, 4, 41, 46], 
    [92, 33, 4, 38, 64, 99, 36, 50, 79, 31, 55, 73, 28, 80, 40], 
    [32, 61, 67, 52, 97, 91, 24, 74, 22, 84, 36, 8, 5, 12, 90], 
    [84, 96, 81, 99, 98, 28, 6, 23, 65, 26, 36, 20, 80, 64, 22], 
    [63, 26, 22, 14, 58, 91, 93, 17, 25, 23, 35, 49, 97, 27, 21], 
    [92, 40, 82, 19, 1, 94, 25, 8, 82, 19, 94, 37, 76, 1, 18], 
    [25, 74, 85, 40, 9, 43, 17, 10, 48, 63, 43, 18, 90, 74, 11], 
    [37, 47, 37, 99, 67, 56, 15, 61, 70, 49, 9, 29, 75, 4, 38], 
    [15, 70, 61, 62, 5, 82, 8, 40, 65, 21, 42, 20, 16, 3, 56], 
    [60, 50, 46, 85, 26, 72, 39, 51, 98, 34, 15, 59, 56, 6, 19], 
    [29, 97, 36, 43, 100, 25, 44, 71, 36, 14, 50, 97, 94, 38, 35], 
    [12, 3, 62, 90, 47, 59, 13, 10, 79, 72, 100, 99, 72, 9, 10], 
    [13, 58, 6, 47, 86, 52, 81, 49, 13, 22, 7, 95, 100, 74, 38]
]

N = int(input("amount of numbers: "))
st = time()
factor = 100//N

possible_pixels = [i for i in range(0, 101, factor)]

for row in matrix:
    for i, number in enumerate(row):
        for p in possible_pixels:
            if abs(number - p) <= factor//2:
                row[i] = p
                break

print(time() - st)
for row in matrix:
    print(row)