import unittest
from datetime import date
from human import Person, Student

class TestExp(unittest.TestCase):  
  def test_Person(self):
    tom = Person('Tom', 'Anderson', date(1980, 10, 10))
    self.assertEqual(tom.get_age(), 38)
  
  def test_greet(self):
    tom = Person('Tom', 'Anderson', date(1980, 10, 10))
    self.assertEqual(tom.greet(), 'Hello, I am Tom Anderson.')

  def james_Person(self):
    james = Student('James', 'Tuck', date(1998, 12, 20), 'Mathematics')
    self.assertEqual(james.get_age(), 19)

  def james_greet(self):
    james = Student('James', 'Tuck', date(1998, 12, 20), 'Mathematics')
    self.assertEqual(james.greet(), 'Hello, I am Tom Anderson.')

unittest.main(verbosity=2)