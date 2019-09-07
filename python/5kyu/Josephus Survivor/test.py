import unittest
import solution

class UnitTests(unittest.TestCase): 
    def test_basic(self):         
        self.assertEqual(solution.josephus_survivor(7,3),4)
        self.assertEqual(solution.josephus_survivor(11,19),10)
        self.assertEqual(solution.josephus_survivor(1,300),1)
        self.assertEqual(solution.josephus_survivor(14,2),13)
        self.assertEqual(solution.josephus_survivor(100,1),100)

if __name__ == '__main__': 
    unittest.main() 
