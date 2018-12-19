class Expression:
    def eval(self, x_value):
        '''変数 x の値が x_value だった時の式の値を返すメソッド'''
        raise NotImplementedError
    
    def diff(self):
        '''式を変数 x で微分した式に対応する Expression オブジェクト
        を返すメソッド'''
        raise NotImplementedError

class Number(Expression):
    '''変更の必要なし'''
    def __init__(self, number):
        self.number = number
    
    def eval(self, x_value):
        return self.number
    
    def diff(self):
        return Number(0)

class Add(Expression):
    pass

class Sub(Expression):
    pass

class Mul(Expression):
    pass

class Div(Expression):
    pass
                   
class X(Expression):
    pass
