import unittest
import solution

class UnitTests(unittest.TestCase): 
    def test(self):         
        self.assertEqual(solution.multiply(100, 2), 200)
        self.assertEqual(solution.multiply(2, 4), 8)

if __name__ == '__main__': 
    unittest.main() 
