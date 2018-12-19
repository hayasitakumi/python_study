import unittest
from expr import Expression, Number, X, Add, Sub, Mul, Div

class TestExpr(unittest.TestCase):
    def test_x_is_expression(self):
        self.assertIsInstance(X(), Expression)
    
    def test_x_eval_10(self):
        self.assertEqual(X().eval(10), 10)
    
    def test_x_diff_is_a_number(self):
        self.assertIsInstance(X().diff(), Number)
    
    def test_x_diff(self):
        self.assertEqual(X().diff().eval(0), 1)
    
    def test_2x_3_eval(self):
        f = Add(Mul(Number(2), X()), Number(3))  # f(x) = 2x + 3
        self.assertEqual(f.eval(10), 23)
    
    def test_2x_3_diff(self):
        f = Add(Mul(Number(2), X()), Number(3))  # f(x) = 2x + 3
        self.assertEqual(f.diff().eval(100), 2)
    
    def test_xx_3x_2_eval(self):
        x = X()
        f = Add(Add(Mul(x, x), Mul(Number(3), x)), Number(2))
        # f(x) = x**2 + 3x + 2
        self.assertEqual(f.eval(10), 132)

    def test_xx_3x_2_diff(self):
        x = X()
        f = Add(Add(Mul(x, x), Mul(Number(3), x)), Number(2))
        # f(x) = x**2 + 3x + 2
        self.assertEqual(f.diff().eval(10), 23)

    def test_sub(self):
        x = X()
        f = Sub(Mul(x, x), Mul(Number(2), x))  # f(x) = x**2 - 2x
        self.assertEqual(f.eval(2), 0)

    def test_sub_diff(self):
        x = X()
        f = Sub(Mul(x, x), Mul(Number(2), x))  # f(x) = x**2 - 2x
        self.assertEqual(f.diff().eval(2), 2)

    def test_div(self):
        x = X()
        f = Div(x, Add(Mul(x, x), Number(1)))  # f(x) = x / (x**2 + 1)
        self.assertAlmostEqual(f.eval(2), 0.4)
    
    def test_div_diff(self):
        x = X()
        f = Div(x, Add(Mul(x, x), Number(1)))  # f(x) = x / (x**2 + 1)
        self.assertAlmostEqual(f.diff().eval(1), 0)
        self.assertAlmostEqual(f.diff().eval(2), -3/25)

if __name__ == '__main__':
    unittest.main(verbosity=2)