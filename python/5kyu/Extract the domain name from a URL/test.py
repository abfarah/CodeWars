import unittest
import solution

class UnitTests(unittest.TestCase): 
    def test(self):         
        self.assertEqual(solution.domain_name("http://google.com"), "google")
        self.assertEqual(solution.domain_name("http://google.co.jp"), "google")
        self.assertEqual(solution.domain_name("www.xakep.ru"), "xakep")
        self.assertEqual(solution.domain_name("https://youtube.com"), "youtube")


if __name__ == '__main__': 
    unittest.main() 
