"""
@file   : unittest_doublechar.py
@brief  :Write unittest for double_char.
"""
import unittest
from double_char import* 
class double_char(unittest.TestCase):
    def test_case1(self):
        word = fun("ab")
        self.assertEqual(word,"aabb")
    def test_numb(self):
        word =fun("123")
        self.assertEqual(word,"112233")
    def test_symbol(self):
        word = fun("@#$%")
        self.assertEqual(word,"@@##$$%%")

if __name__=="__main__":

   unittest.main()


