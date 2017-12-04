def mat(matrix):

  m = len(matrix)

  n = len(matrix[0])

  rows = []

  cols = []

  for i in range(m):

    for j in range(n):

      if matrix[i][j]==0:

        rows.append(i)

        cols.append(j)

  for row in rows:
      
    nullify_row(matrix,row)

  for col in cols:

    nullify_col(matrix,col)

  
def nullify_row(matrix,row):

  for i in range(len(matrix[0])):

    matrix[row][i]=0


def nullify_col(matrix,col):

  for i in range(len(matrix)):

    matrix[i][col]=0

    
    
matrix = [[1,4,3,6],[5,7,6,8],[9,9,9,8],[1,1,2,3],[1,2,1,0]]

mat(matrix)

print(matrix)



from copy import deepcopy


def matrix_rotate(matrix):

  n = len(matrix)

  res = deepcopy(matrix)

  for x in range(n):

    for y in range(n-1,-1,-1):

      res[x][n-1-y] = matrix[y][x]

  return res



rmatrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

print(matrix_rotate(rmatrix))