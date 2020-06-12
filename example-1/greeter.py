from unittest import TestCase

def greet(name):
  return f'Hello {name}!'

class GreeterTests(TestCase):
  def test_greet(self):
    self.assertEqual('Hello Derek!', greet('Derek'))

