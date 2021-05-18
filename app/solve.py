class SudokuSolver:
  def __init__(self, board):
    self.board = board
    self.solved = None

  def print_board(self):
    for i in range(len(self.board)):
      if i % 3 == 0 and i != 0:
        print('------------------------')
      
      for j in range(len(self.board[0])):
        if j % 3 == 0 and j != 0:
          print(' | ', end='')
        
        if j == 8:
          print(self.board[i][j])
        else:
          print('{} '.format(self.board[i][j]), end='')


  def find_empty(self):
    for i in range(len(self.board)):
      for j in range(len(self.board[0])):
        if self.board[i][j] == 0:
          return (i, j)


  def is_valid(self, num, pos):
    row, col = pos

    # Check row
    for i in range(len(self.board[0])):
      if self.board[row][i] == num and col != i:
        return False
    
    # Check column
    for i in range(len(self.board)):
      if self.board[i][col] == num and row != i:
        return False
    
    # Check box
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
      for j in range(box_x * 3, box_x * 3 + 3):
        if self.board[i][j] == num and (i, j) != (row, col):
          return False
    return True

  def solve(self):
    found = self.find_empty()
    if not found:
      return True
    row, col = found
    
    for i in range(1, 10):
      if self.is_valid(i, (row, col)):
        self.board[row][col] = i
      
        if self.solve():
          return True
          
        # Backtrack
        self.board[row][col] = 0

  @staticmethod
  def multidict_to_board(multidict):
    li = []
    for i in range(9):
        li.append(multidict[i*9 : (i+1)*9])
    return li

  @staticmethod
  def empty_board():
    return  [
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        ['','','','','','','','','']
      ]
  
  @staticmethod
  def samples():
    return [
      [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
      ],
      [
        [5,3,4,6,7,8,9,0,0],
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9]
      ]
    ]