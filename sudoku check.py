# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
def wholeno(a):
    z = 1
    num = []
    n = len(a)
    while z <= n:
        num.append(z)
        z += 1
    return num

def check_sudoku(a):
    p = 0
    n = len(a)
    #check in rows=
    while p < n:
        q = 0
        while q < n:
            if wholeno(a)[q] not in a[p]:
                return False
            q += 1
        p += 1
    #check in column=
    y = 0
    k = []
    while y < n:
        x = 0
        while x < n:
            if wholeno(a)[y] == a[x][y]:
                k.append(wholeno(a)[y])
            x += 1
        y += 1
    if k == wholeno(a):
        return True
    else:
        return False

print (check_sudoku(incorrect))
#>>> False

print (check_sudoku(correct))
#>>> True

print (check_sudoku(incorrect2))
#>>> False

print (check_sudoku(incorrect3))
#>>> False

print (check_sudoku(incorrect4))
#>>> False

print (check_sudoku(incorrect5))
#>>> False
