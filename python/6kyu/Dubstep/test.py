import unittest
import solution

class UnitTests(unittest.TestCase): 
    def test(self):         
        self.assertEqual(solution.song_decoder("AWUBBWUBC"), "A B C","WUB should be replaced by 1 space")
        self.assertEqual(solution.song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C","multiples WUB should be replaced by only 1 space")
        self.assertEqual(solution.song_decoder("WUBAWUBBWUBCWUB"), "A B C","heading or trailing spaces should be removed")


if __name__ == '__main__': 
    unittest.main() 
