import requests


class SudokuSolver:
    def create_empty_board(self):
        return [
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '']
        ]

    def print_board(self, board):
        for i in range(len(board)):
            if i % 3 == 0 and i != 0:
                print('------------------------')

            for j in range(len(board[0])):
                if j % 3 == 0 and j != 0:
                    print(' | ', end='')

                if j == 8:
                    print(board[i][j])
                else:
                    print('{} '.format(board[i][j]), end='')

    def find_empty(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return (i, j)

    def is_valid(self, num, pos, board):
        row, col = pos

        # Check row
        for i in range(len(board[0])):
            if board[row][i] == num and col != i:
                return False

        # Check column
        for i in range(len(board)):
            if board[i][col] == num and row != i:
                return False

        # Check box
        box_x = col // 3
        box_y = row // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if board[i][j] == num and (i, j) != (row, col):
                    return False
        return True

    def solve(self, board):
        found = self.find_empty(board)
        if not found:
            return board
        row, col = found

        for i in range(1, 10):
            if self.is_valid(i, (row, col), board):
                board[row][col] = i

                if self.solve(board):
                    return board

                # Backtrack
                board[row][col] = 0

    def multidict_to_board(self, multidict):
        li = []
        for i in range(9):
            li.append(multidict[i * 9: (i + 1) * 9])
        return li

    def new_board(self, level):
        url = f'http://www.cs.utep.edu/cheon/ws/sudoku/new/?size=9&level={level}'
        print(url)

        resp = requests.get(url)
        data = resp.json()

        board_from_data = data['squares']

        if resp:
            def api_board_to_list(api_board):
                new_board = self.create_empty_board()
                for row in api_board:
                    y = row['y']
                    x = row['x']
                    val = row['value']
                    # Insert a value into a specific position
                    new_board[y][x] = val
                return new_board
            new_board = api_board_to_list(board_from_data)
        board = new_board
        return board
