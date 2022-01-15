# entries = [[5,3,0,0,7,0,0,0,0],
#            [6,0,0,1,9,5,0,0,0],
#            [0,9,8,0,0,0,0,6,0],
#            [8,0,0,0,6,0,0,0,3],
#            [4,0,0,8,0,3,0,0,1],
#            [7,0,0,0,2,0,0,0,6],
#            [0,6,0,0,0,0,2,8,0],
#            [0,0,0,4,1,9,0,0,5],
#            [0,0,0,0,8,0,0,7,9]]


import numpy as np

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

print("Enter the entries in a single line (separated by space): ")
#the input will be space separated numbers::

# 5 3 0 0 7 0 0 0 0 6 0 0 1 9 5 0 0 0 0 9 8 0 0 0 0 6 0 8 0 0 0 6 0 0 0 3 4 0 0 8 0 3 0 0 1 7 0 0 0 2 0 0 0 6 0 6 0 0 0 0 2 8 0 0 0 0 4 1 9 0 0 5 0 0 0 0 8 0 0 7 9

entries1 = list(map(int, input().split()))

entries = np.array(entries1).reshape(R, C)

def possible(R,C,n) :
    global entries

    for i in range(0,9) : #check in rows
        if entries[R][i] == n:
            return False

    for i in range(0,9) : #check in cols
        if entries[i][C] == n :
            return False

    rows_in_box = (R//3) * 3
    cols_in_box = (C//3) * 3

    for i in range(0,3) : #check in boxs(3*3)
        for j in range(0,3) :
            if entries[rows_in_box+i][cols_in_box+j] == n :
                return False
    return True


def solve() :
    global entries

    for R in range (9) :
        for C in range(9) :
            if entries[R][C] == 0 :
                for n in range(1,10) :
                    if possible(R,C,n) :
                        entries[R][C] = n
                        solve()
                        entries[R][C] = 0
                return
    print("Sudoku Solution is: \n" , np.matrix(entries))


solve()