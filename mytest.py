import unittest
from mycode import *

class MyFirstTests(unittest.TestCase):

  def test_hello(self):

     self.assertEqual(hello_world(), 'hello world')

age = int(input("yeat of birth: "))
human = 2019 - (age -0)*1
print()
if age < 18:
	print("You are a minor!")
elif age == 36:
	print("You are a Youth")
elif age > 37:
	print("An Elder")
     