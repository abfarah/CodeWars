import unittest
import solution

class UnitTests(unittest.TestCase): 
    def test_encrypt(self):         
        self.assertEqual(solution.encrypt("This is a test!", 0), "This is a test!")
        self.assertEqual(solution.encrypt("This is a test!", 1), "hsi  etTi sats!")
        self.assertEqual(solution.encrypt("This is a test!", 2), "s eT ashi tist!")
        self.assertEqual(solution.encrypt("This is a test!", 3), " Tah itse sits!")
        self.assertEqual(solution.encrypt("This is a test!", 4), "This is a test!")
        self.assertEqual(solution.encrypt("This is a test!", -1), "This is a test!")
        self.assertEqual(solution.encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")

    def test_decrypt(self):
        self.assertEqual(solution.decrypt("This is a test!", 0), "This is a test!")
        self.assertEqual(solution.decrypt("hsi  etTi sats!", 1), "This is a test!")
        self.assertEqual(solution.decrypt("s eT ashi tist!", 2), "This is a test!")
        self.assertEqual(solution.decrypt(" Tah itse sits!", 3), "This is a test!")
        self.assertEqual(solution.decrypt("This is a test!", 4), "This is a test!")
        self.assertEqual(solution.decrypt("This is a test!", -1), "This is a test!")
        self.assertEqual(solution.decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")

    def test_null(self):
        self.assertEqual(solution.encrypt("", 0), "")
        self.assertEqual(solution.decrypt("", 0), "")
        self.assertEqual(solution.encrypt(None, 0), None)
        self.assertEqual(solution.decrypt(None, 0), None)

if __name__ == '__main__': 
    unittest.main() 
