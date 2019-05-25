class Board:
  num_objects = 0  # Boardオブジェクトがいくつ作られたかトラッキングするクラス変数

  def __init__(self, data, allowed_digits=None):
    '''インスタンス変数self.dataは各マスに置かれた数字を要素とする9x9のリスト、
    self.allowed_digitsは各マスに置ける数字の集合を要素とする9x9のリスト'''
    Board.num_objects += 1
    self.data = data
    if allowed_digits is None:
      self.precompute_allowed_digits()
    else:
      self.allowed_digits = allowed_digits

  @classmethod
  def get_row(cls, obj, x):
    '''9x9の2次元リストobjからx行目を取り出す。objとしてはself.dataまたは
    self.allowed_digitsに準ずる2次元リストが渡されることを想定。'''
    return obj[x]

  @classmethod
  def get_column(cls, obj, y):
    '''9x9の2次元リストobjからy列目を取り出す'''
    return [obj[x][y] for x in range(9)]

  @classmethod
  def get_block(cls, obj, x, y):
    '''9x9の2次元リストobjから(x, y)が属する3x3ブロックを取り出す'''
    base_x = x // 3 * 3
    base_y = y // 3 * 3
    return [obj[x][y] for x in range(base_x, base_x + 3)
                      for y in range(base_y, base_y + 3)]

  def filled(self):
    return all(0 not in self.data[x] for x in range(9))

  def verify(self):
    def check(xs):
      '''リストxsが0~9の数からなり、1~9については重複がないことを
      チェックするヘルパー関数'''
      xs = [x for x in xs if x != 0]
      return (len(set(xs)) == len(xs) and all(1 <= x <= 9 for x in xs))

    return (all(check(Board.get_row(self.data, x)) for x in range(9))
        and all(check(Board.get_column(self.data, y)) for y in range(9))
        and all(check(Board.get_block(self.data, x, y)) for x in (0, 3, 6)
                                                        for y in (0, 3, 6)))

  def get_allowed_digits(self, x, y):
    return list(self.allowed_digits[x][y])

  def update_allowed_digits(self, allowed_digits, x, y, d):
    if d > 0:
      allowed_digits[x][y] = set()
      for obj in Board.get_row(allowed_digits, x):
        # 同じ行のマスの候補リストからdを除外
        obj.discard(d)
      for obj in Board.get_column(allowed_digits, y):
        # 同じ列のマスの候補リストからdを除外
        obj.discard(d)
      for obj in Board.get_block(allowed_digits, x, y):
        # 同じ3x3ブロックのマスの候補リストからdを除外
        obj.discard(d)

  def precompute_allowed_digits(self):
    self.allowed_digits = [
      [{1, 2, 3, 4, 5, 6, 7, 8, 9} for y in range(9)] for x in range(9)
    ]
    for x in range(9):
      for y in range(9):
        d = self.data[x][y]
        self.update_allowed_digits(self.allowed_digits, x, y, d)

  def move(self, x, y, d):
    assert self.data[x][y] == 0
    data = []
    for i, row in enumerate(self.data):
      if i != x:
        data.append(row)
      else:
        new_row = list(row)
        new_row[y] = d
        data.append(new_row)
    allowed_digits = [
      [set(self.allowed_digits[x][y]) for y in range(9)] for x in range(9)
    ]  # set()をつけることによりdeep copyを行う
    self.update_allowed_digits(allowed_digits, x, y, d)
    return Board(data, allowed_digits)

  def __str__(self):
    separator = '+---+---+---+'
    lines = [separator]
    for i in range(0, 9, 3):
      for j in range(i, i + 3):
        lines.append('|%d%d%d|%d%d%d|%d%d%d|' % tuple(self.data[j]))
      lines.append(separator)
    return '\n'.join(lines).replace('0', ' ')


if __name__ == '__main__':
  import sudoku as su
  problem = Board(su.text_to_data(su.PROBLEM))
  solution = Board(su.text_to_data(su.SOLUTION))
  board = problem
  print(board.move(0, 1, 1))