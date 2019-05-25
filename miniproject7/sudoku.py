from board import Board
from dfs import dfs

# https://en.wikipedia.org/wiki/Sudoku
PROBLEM = (
    '53  7    \n'
    '6  195   \n'
    ' 98    6 \n'
    '8   6   3\n'
    '4  8 3  1\n'
    '7   2   6\n'
    ' 6    28 \n'
    '   419  5\n'
    '    8  79')
SOLUTION = (
    '534678912\n'
    '672195348\n'
    '198342567\n'
    '859761423\n'
    '426853791\n'
    '713924856\n'
    '961537284\n'
    '287419635\n'
    '345286179')

# https://www.websudoku.com/
EASY = (
    '7   91 35\n'
    ' 1   3   \n'
    '9 3 67   \n'
    '845 3 61 \n'
    '         \n'
    ' 36 5 487\n'
    '   47 9 8\n'
    '   9   6 \n'
    '65 31   4')
MEDIUM = (
    '12735    \n'
    '    7    \n'
    '  8 6  7 \n'
    '81 5    4\n'
    '2  7 4  1\n'
    '4    3 95\n'
    ' 9  2 6  \n'
    '    4    \n'
    '    31259')
HARD = (
    '  26  5  \n'
    '        3\n'
    '8  1  92 \n'
    ' 3  7   9\n'
    '27     54\n'
    '9   8  6 \n'
    ' 24  6  7\n'
    '3        \n'
    '  5  26  ')
EVIL = (
    ' 18 6    \n'
    '3    9   \n'
    '  9  34  \n'
    ' 9 1    5\n'
    ' 42   71 \n'
    '5    2 8 \n'
    '  45  6  \n'
    '   8    7\n'
    '    7 84 ')


class SearchProblem:
  '''探索問題を定義する抽象クラス'''
  def get_start_state(self):
    '''初期状態を返す関数'''
    raise NotImplementedError

  def next_states(self, state):
    '''与えられた状態 state から遷移できる状態のリストを返す関数'''
    raise NotImplementedError

  def is_goal(self, state):
    '''与えられた状態 state がゴールかどうかを True/False で返す関数'''
    raise NotImplementedError


class Sudoku(SearchProblem):
  def __init__(self, board):
    self.board = board

  def get_start_state(self):
    return self.board

  def is_goal(self, board):
    if board.filled() and board.verify():
      return True
    return False

  def next_states(self, board):
    board_list = []
    for x in range(0, 9):
      for y in range(0, 9):
        if board.data[x][y] == 0:
          for candidate in board.get_allowed_digits(x, y):
            board_list.append(board.move(x, y, candidate))
          return board_list
          

def text_to_data(text):
  data = []
  for line in text.splitlines():
    assert len(line) == 9
    data.append(list(map(int, line.replace(' ', '0'))))
  return data

def test(title, problem):
  print('\nTesting %s problem...' % title)
  board = Board(text_to_data(problem))
  sudoku = Sudoku(board)
  boards = dfs(sudoku)
  print('%d Board objects instantiated' % Board.num_objects)
  assert boards[-1].verify()

if __name__ == '__main__':
    board = Board(text_to_data(PROBLEM))
    sudoku = Sudoku(board)
    boards = dfs(sudoku)
    for i, board in enumerate(boards):
        print('\nSTEP %d' % i)
        print(board)
    # print('%d Board objects instantiated' % Board.num_objects)
    # assert boards[-1].data == text_to_data(SOLUTION)

    # test('easy', EASY)
    # test('medium', MEDIUM)
    # test('hard', HARD)
    # test('evil', EVIL)