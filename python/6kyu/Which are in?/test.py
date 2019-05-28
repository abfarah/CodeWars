import unittest
import solution

class UnitTests(unittest.TestCase): 
    def test(self):         
        a1 = ["live", "arp", "strong"] 
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        r = ['arp', 'live', 'strong']    
        self.assertEqual(solution.in_array(a1, a2), r)


if __name__ == '__main__': 
    unittest.main() 
