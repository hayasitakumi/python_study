import unittest
from util import diff
 
class TestDiff(unittest.TestCase):
    def test_5_2(self):
        self.assertEqual(diff(5, 2), 3)
                      
    def test_2_5(self):
        self.assertEqual(diff(2, 5), 3)
                                       
    def test_10_10(self):
        self.assertEqual(diff(10, 10), 0)
                                                        
    def test__5_5(self):
        self.assertEqual(diff(-5, 5), 10)
                                                                         
if __name__ == '__main__':
    unittest.main(verbosity=2)
