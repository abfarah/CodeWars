import unittest
import solution

class UnitTests(unittest.TestCase): 
    def test_one_step(self):         
        self.assertEqual(solution.josephus([1,2,3,4,5,6,7,8,9,10],1),[1,2,3,4,5,6,7,8,9,10])

    def test_two_step(self):
        self.assertEqual(solution.josephus([1,2,3,4,5,6,7,8,9,10],2),[2, 4, 6, 8, 10, 3, 7, 1, 9, 5])

    def test_non_integer(self):
        self.assertEqual(solution.josephus(["C","o","d","e","W","a","r","s"],4),['e', 's', 'W', 'o', 'C', 'd', 'r', 'a'])

    def test_shorter_array(self):
        self.assertEqual(solution.josephus([1,2,3,4,5,6,7],3),[3, 6, 2, 7, 5, 1, 4])

    def test_empty_array(self):
        self.assertEqual(solution.josephus([],3),[])


if __name__ == '__main__': 
    unittest.main() 
