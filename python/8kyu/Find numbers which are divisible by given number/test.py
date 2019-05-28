import unittest
import solution

class UnitTests(unittest.TestCase): 
    def test(self):         
        self.assertEqual(solution.divisible_by([1,2,3,4,5,6], 2), [2,4,6])
        self.assertEqual(solution.divisible_by([1,2,3,4,5,6], 3), [3,6])
        self.assertEqual(solution.divisible_by([0,1,2,3,4,5,6], 4), [0,4])
        self.assertEqual(solution.divisible_by([0], 4), [0])
        self.assertEqual(solution.divisible_by([1,3,5], 2), [])


if __name__ == '__main__': 
    unittest.main() 
