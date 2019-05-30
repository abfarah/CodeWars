import unittest
import solution

class UnitTests(unittest.TestCase): 
    def test_basic(self):         
        self.assertEqual(solution.first_non_repeating_letter('a'), 'a')
        self.assertEqual(solution.first_non_repeating_letter('stress'), 't')
        self.assertEqual(solution.first_non_repeating_letter('moonmen'), 'e')

    def test_empty_string(self):
        self.assertEqual(solution.first_non_repeating_letter(''), '')

    def test_repeating_characters(self):
        self.assertEqual(solution.first_non_repeating_letter('abba'), '')
        self.assertEqual(solution.first_non_repeating_letter('aa'), '')

    def test_odd_characters(self):
        self.assertEqual(solution.first_non_repeating_letter('~><#~><'), '#')
        self.assertEqual(solution.first_non_repeating_letter('hello world, eh?'), 'w')

    def test_upper_case_letters(self):
        self.assertEqual(solution.first_non_repeating_letter('sTreSS'), 'T')
        self.assertEqual(solution.first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')


if __name__ == '__main__': 
    unittest.main() 
