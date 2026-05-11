from unittest import TestCase

import py_bank

class TestValidateEmail(TestCase):

       def test_that_validate_email_function_exists(self):
           py_bank.validate_email("nmaa.baby@.com")

       def test_that_the_email_has_at_least_8_characters(self):

           is_valid = py_bank.validate_email("nmaa.baby@.com")

           self.assertTrue(is_valid)

       def test_that_invalid_email_is_less_than_8_characters_return_false(self):
              
           is_invalid = py_bank.validate_email("nmaa")   
              
           self.assertFalse(is_invalid) 

       def test_that_valid_email_must_have_special_characters(self):
               
           actual = py_bank.validate_email("nmaa.baby@.com")
           expected = "valid email"   
           self.assertEqual(actual,expected)   


       def test_that_
