import copy

class Board:
  def __init__(self, data):
    self.data = data

  def filled(self):
    for line in self.data:
      for number in line:
        if number == 0:
          return False
    return True

  def verify(self):   
    for x in range(0, 9):
      for i in range(1, 9):
        if self.data[x].count(i) > 1:
          return False
      vertical = []
      for y in range(0, 9):
        vertical.append(self.data[y][x])
      for i in range(1, 9):
        if vertical.count(i) > 1:
          return False
    for init_x in range(0, 9, 3):
      for init_y in range(0, 9, 3):
        block = []
        for x in range(init_x, init_x + 3):
          for y in range(init_y, init_y + 3):
            block.append(self.data[x][y])
        for i in range(1, 9):
          if block.count(i) > 1:
            return False
    return True
        
  def get_allowed_digits(self, x, y):
    if self.data[x][y] != 0:
      return []
    digits = [i for i in range(1, 10)]
    for i in range(0, 9):
      if self.data[x][i] in digits:
        digits.remove(self.data[x][i])
      if self.data[i][y] in digits:
        digits.remove(self.data[i][y])
    init_x = int(x/3) * 3
    init_y = int(y/3) * 3
    for i in range(init_x, init_x + 3):
      for j in range(init_y, init_y + 3):
        if self.data[i][j] in digits:
          digits.remove(self.data[i][j])
    return digits

  def move(self, x, y, d):
    assert self.data[x][y] == 0
    new_board = copy.deepcopy(Board(self.data))
    new_board.data[x][y] = d
    return new_board

  def __str__(self):
    separator = '+---+---+---+'
    lines = [separator]
    for i in range(0, 9, 3):
      for j in range(i, i + 3):
        lines.append('|%d%d%d|%d%d%d|%d%d%d|' % tuple(self.data[j]))
        lines.append(separator)
    return '\n'.join(lines).replace('0', ' ')