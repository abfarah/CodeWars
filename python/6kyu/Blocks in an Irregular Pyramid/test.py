import unittest
import solution

class UnitTests(unittest.TestCase): 
    def test(self):         

        self.assertEqual(solution.blocks(1, 1, 2), 5)
        self.assertEqual(solution.blocks(2, 4, 3), 47)
        self.assertEqual(solution.blocks(1, 10, 10), 880)
        self.assertEqual(solution.blocks(20, 30, 40), 83540)

if __name__ == '__main__': 
    unittest.main() 
