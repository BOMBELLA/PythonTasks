import unittest
import cuber

class Testcuber(unittest.TestCase):
       def test_that_cube_cuber_exists(self):
            cuber.cube(3)
       def test_that_cube_cuber_return_correct_result(self):
           actual = cuber.cube(3)
           expected = 27
           self.assertEqual(actual, expected)         

      
