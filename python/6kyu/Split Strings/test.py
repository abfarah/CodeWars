import unittest
import solution

class UnitTests(unittest.TestCase): 
    def test(self):         
        tests = (
            ("asdfadsf", ['as', 'df', 'ad', 'sf']),
            ("asdfads", ['as', 'df', 'ad', 's_']),
            ("", []),
            ("x", ["x_"]),
)
        for inp, exp in tests:
            self.assertEqual(solution.solution(inp), exp)



if __name__ == '__main__': 
    unittest.main() 
