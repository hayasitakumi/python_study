class Expression:
  '''基底クラス: 変更不可'''
  def eval(self):
    '''Expression のサブクラスは必ずこのメソッドを実装すること'''
    raise NotImplementedError


class Number(Expression):
  '''定数を表すクラス'''
  def __init__(self, number):
    self.number = number

  def eval(self):
    return self.number


class Add(Expression):
  '''二つの式の和に対応する式を表すクラス'''
  def __init__(self, formula0, formula1):
    self.formula0 = formula0.eval()
    self.formula1 = formula1.eval()
  def eval(self):
    return self.formula0 + self.formula1

class Sub(Expression):
  '''二つの式の差に対応する式を表すクラス'''
  def __init__(self, formula0, formula1):
    self.formula0 = formula0.eval()
    self.formula1 = formula1.eval()
  def eval(self):
    return self.formula0 - self.formula1

class Mul(Expression):
  '''二つの式の積に対応する式を表すクラス'''
  def __init__(self, formula0, formula1):
    self.formula0 = formula0.eval()
    self.formula1 = formula1.eval()
  def eval(self):
    return self.formula0 * self.formula1

class Div(Expression):
  '''二つの式の商に対応する式を表すクラス'''
  def __init__(self, formula0, formula1):
    self.formula0 = formula0.eval()
    self.formula1 = formula1.eval()
  def eval(self):
    return self.formula0 / self.formula1
