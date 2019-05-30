import unittest
import solution

class UnitTests(unittest.TestCase): 
    def test(self):         
        self.assertEqual(solution.likes([]), 'no one likes this')
        self.assertEqual(solution.likes(['Peter']), 'Peter likes this')
        self.assertEqual(solution.likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
        self.assertEqual(solution.likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
        self.assertEqual(solution.likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')


if __name__ == '__main__': 
    unittest.main() 
