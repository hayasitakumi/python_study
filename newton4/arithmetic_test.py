import unittest
from arithmetic import Expression, Number, Add, Sub, Mul, Div

class TestExp(unittest.TestCase):
    def test_number(self):
        self.assertEqual(Number(42).eval(), 42)

    def test_number_is_expression(self):
        self.assertIsInstance(Number(0), Expression)

    def test_add_is_expression(self):
        self.assertIsInstance(Add(Number(1), Number(2)), Expression)

    def test_add(self):
        self.assertEqual(Add(Number(2), Number(3)).eval(), 5)

    def test_sub(self):
        self.assertEqual(Sub(Number(2), Number(5)).eval(), -3)

    def test_mul(self):
        self.assertEqual(Mul(Number(3), Number(4)).eval(), 12)

    def test_div(self):
        self.assertEqual(Div(Number(3), Number(4)).eval(), 0.75)

    def test_nested_1(self):
        self.assertEqual(Mul(Number(3), Add(Number(2), Number(4))).eval(), 18)

    def test_nested_2(self):
        self.assertEqual(Div(Add(Number(2), Number(3)), Number(2)).eval(), 2.5)

    def test_nested_3(self):
        self.assertEqual(Div(Add(Number(2), Number(3)), Sub(Number(7), Number(2))).eval(), 1.0)

unittest.main(verbosity=2)