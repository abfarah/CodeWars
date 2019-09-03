import unittest
import solution


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
a1 = ["WEST"]
b = ["NORTH", "WEST", "SOUTH", "EAST"]
b1 = ["NORTH", "WEST", "SOUTH", "EAST"] 
c = ["NORTH", "SOUTH", "SOUTH", "NORTH", "EAST", "WEST", "NORTH", "WEST", "WEST"]
c1 = ["NORTH", "WEST", "WEST"]
d = ["NORTH", "SOUTH", "SOUTH", "NORTH", "EAST", "WEST"]
d1 = []

class UnitTests(unittest.TestCase): 
    def test_basic(self):         
        self.assertEqual(solution.dirReduc(a), a1)

    def test_No_Change(self):
        self.assertEqual(solution.dirReduc(b), b1)

    def test_double_direction(self):
        self.assertEqual(solution.dirReduc(c), c1)

    def test_No_direction_change(self):
        self.assertEqual(solution.dirReduc(d), d1)


if __name__ == '__main__': 
    unittest.main() 
