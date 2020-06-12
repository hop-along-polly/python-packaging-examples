from unittest import TestCase
from translator.greeter import greet

class GreeterTests(TestCase):
  def test_greet(self):
    self.assertEqual('Hello Derek!', greet('Derek'))

