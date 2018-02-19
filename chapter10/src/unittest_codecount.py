"""
@file :  unittest_codecount.py
@brief :Write unittest for count_code
"""
import unittest
from code_count import*
class count_code(unittest.TestCase):
     def test_case1(self):
         sub_string = my_sub_string_count(string ="code")
         self.assertEqual(sub_string,1)  
     def test_case2(self):
         sub_string = my_sub_string_count(string = "cozecore") 
         self.assertEqual(sub_string,2)
     def test_case3(self):  
         sub_string = my_sub_string_count(string ="12345$#")
         self.assertEqual(sub_string,0)
if __name__=="__main__":
       unittest.main()


