import unittest
from mycode import *

class MyFirstTests(unittest.TestCase):

  def test_hello(self):

     self.assertEqual(hello_world(), 'hello world')

     minor = 0 - 17
     print(minor)

     youth = 18 - 36
     print(youth)

     elder = 37 - 200
     print(elder)

     