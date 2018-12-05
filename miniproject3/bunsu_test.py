import unittest
import bunsu

class BunsuTest(unittest.TestCase):
  def test_gcd_1(self):
    self.assertEqual(bunsu.gcd(12, 18), 6)

  def test_gcd_2(self):
    self.assertEqual(bunsu.gcd(18, 12), 6)

  def test_gcd_3(self):
    self.assertEqual(bunsu.gcd(24, 12), 12)

  def test_gcd_4(self):
    self.assertEqual(bunsu.gcd(12, 24), 12)

  def test_gcd_5(self):
    self.assertEqual(bunsu.gcd(3, 5), 1)

  def test_gcd_6(self):
    self.assertEqual(bunsu.gcd(91, 32), 1)

  # ref. https://sugaku.fun/calculation-of-mixed-fraction/
  def test_add_1(self):
    self.assertEqual(bunsu.add((1, 1, 1, 2), (1, 2, 2, 3)), (1, 4, 1, 6))

  def test_add_2(self):
    self.assertEqual(bunsu.add((-1, 1, 1, 2), (-1, 2, 2, 3)), (-1, 4, 1, 6))

  def test_add_3(self):
    self.assertEqual(bunsu.add((1, 3, 1, 6), (-1, 1, 1, 4)), (1, 1, 11, 12))

  def test_add_4(self):
    self.assertEqual(bunsu.add((-1, 3, 1, 6), (1, 1, 1, 4)), (-1, 1, 11, 12))

  def test_add_5(self):
    self.assertEqual(bunsu.add((1, 1, 2, 3), (1, 1, 1, 3)), (1, 3, 0, 1))

  def test_sub_1(self):
    self.assertEqual(bunsu.sub((1, 3, 1, 6), (1, 1, 1, 4)), (1, 1, 11, 12))

  def test_sub_2(self):
    self.assertEqual(bunsu.sub((1, 1, 1, 5), (1, 1, 1, 5)), (1, 0, 0, 1))

  def test_mul_1(self):
    self.assertEqual(bunsu.mul((1, 3, 1, 2), (1, 1, 1, 4)), (1, 4, 3, 8))

  def test_mul_2(self):
    self.assertEqual(bunsu.mul((-1, 3, 1, 2), (1, 1, 1, 4)), (-1, 4, 3, 8))

  def test_mul_3(self):
    self.assertEqual(bunsu.mul((1, 3, 1, 2), (-1, 1, 1, 4)), (-1, 4, 3, 8))

  def test_mul_4(self):
    self.assertEqual(bunsu.mul((-1, 3, 1, 2), (-1, 1, 1, 4)), (1, 4, 3, 8))

  def test_mul_5(self):
    self.assertEqual(bunsu.mul((1, 5, 3, 7), (1, 0, 0, 1)), (1, 0, 0, 1))
    
  def test_div_1(self):
    # error in the referenced site!
    self.assertEqual(bunsu.div((1, 4, 2, 3), (1, 2, 4, 9)), (1, 1, 10, 11))

  def test_div_2(self):
    self.assertEqual(bunsu.div((1, 1, 1, 4), (-1, 1, 7, 8)), (-1, 0, 2, 3))


if __name__ == '__main__':
  unittest.main(verbosity=2)
