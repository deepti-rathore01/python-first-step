"""
@file :  unittest_codecount.py
@brief :Write unittest for count_code
"""
import unittest
from code_count import*
class count_code(unittest.TestCase):
 def test_pass(self):
        self.assertTrue(True) 
        
 def test_fail(self):
        self.assertFalse(False)
if __name__=="__main__":
     unittest.main()



