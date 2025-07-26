import unittest

def max_of_two(a, b):
    return a if a > b else b


class TestMaxOfTwo(unittest.TestCase):
    def test_two_positive_numbers(self):
        self.assertEqual(max_of_two(10, 20), 20)
        self.assertEqual(max_of_two(25, 25), 25)  
        self.assertGreater(max_of_two(30, 25), 25)
        self.assertLess(max_of_two(15, 40), 40)
    def test_two_negative_numbers(self):
        self.assertEqual(max_of_two(-10, -20), -10)
        self.assertEqual(max_of_two(-15, -15), -15)  
        self.assertGreater(max_of_two(-5, -10), -10)
        self.assertLess(max_of_two(-15, -5), -5)
    def test_positive_and_negative_number(self):
        self.assertEqual(max_of_two(-10, 10), 10)
        
        self.assertEqual(max_of_two(0, -5), 0)  
        self.assertGreater(max_of_two(15, -5), -5)
        self.assertLess(max_of_two(-15, 5), 5)
        
if __name__ == '__main__':
    unittest.main()
