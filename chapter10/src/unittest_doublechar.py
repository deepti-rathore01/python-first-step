"""
@file   : unittest_doublechar.py
@brief  :Write unittest for double_char.
"""
import unittest
from double_char import* 
class double_char(unittest.TestCase):
 def test_pass(self):
     self.assertTrue(True)
 def test_fail(self):
    self.assertFalse(False)
if __name__=="__main__":

   unittest.main()


