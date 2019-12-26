import unittest
import solution

arr = [['a1', 'c1', 2], ['a1', 'f1', 3], ['a1', 'f3', 3], ['a1', 'f4', 4], ['a1', 'f7', 5]]

class UnitTests(unittest.TestCase):
    def test(self):
        for x in arr:
            z = solution.knight(x[0], x[1])
            self.assertEqual(z, x[2])

if __name__ == '__main__':
    unittest.main()
