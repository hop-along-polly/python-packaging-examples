from unittest import TestCase
from translator.greeter import greet

class GreeterTests(TestCase):
  def test_greet_in_english(self):
    self.assertEqual('Hello Derek!', greet('Derek', 'EN'))

  def test_greet_in_spanish(self):
    self.assertEqual('Hola Derek!', greet('Derek', 'ES'))
