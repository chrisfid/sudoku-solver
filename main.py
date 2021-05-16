board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(bo):
  for i in range(len(bo)):
    if i % 3 == 0 and i != 0:
      print('------------------------')
    
    for j in range(len(bo[0])):
      if j % 3 == 0 and j != 0:
        print(' | ', end='')
      
      if j == 8:
        print(bo[i][j])
      else:
        print('{} '.format(bo[i][j]), end='')


def find_empty(bo):
  for i in range(len(bo)):
    for j in range(len(bo[0])):
      if bo[i][j] == 0:
        return (i, j)


def is_valid(bo, num, pos):
  row, col = pos

  # Check row
  for i in range(len(bo[0])):
    if bo[row][i] == num and col != i:
      return False
  
  # Check column
  for i in range(len(bo)):
    if bo[i][col] == num and row != i:
      return False
  
  # Check box
  box_x = col // 3
  box_y = row // 3

  for i in range(box_y * 3, box_y * 3 + 3):
    for j in range(box_x * 3, box_x * 3 + 3):
      if bo[i][j] == num and (i, j) != (row, col):
        return False
  return True


def solve(bo):
  found = find_empty(board)
  if not found:
    return True
  row, col = found
  
  for i in range(1, 10):
    if is_valid(bo, i, (row, col)):
      bo[row][col] = i
    
      if solve(bo):
        return True
        
      # Backtrack
      bo[row][col] = 0

print_board(board)
solve(board)
print()
print_board(board)