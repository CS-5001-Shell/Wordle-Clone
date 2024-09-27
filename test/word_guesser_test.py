import unittest
from unittest import mock
from word_guesser import check_guess

class TestWordGuesser(unittest.TestCase):

    def test_check_guess_example1(self):
        expected = ['G', 'G', 'Y', '-', '-']
        self.assertEqual(check_guess('heart', 'herds'), expected)

    def test_check_guess_example2(self):
        expected = ['G', 'G', '-', '-', '-']
        self.assertEqual(check_guess('trust', 'train'), expected)

    def test_check_guess_example3(self):
        expected = ['-', 'Y', 'Y', '-', '-']
        self.assertEqual(check_guess('train', 'strut'), expected)

    def test_check_guess_example4(self):
        expected = ['G', 'G', '-', 'Y', '-']
        self.assertEqual(check_guess('strut', 'stats'), expected)

    def test_check_guess_no_matches(self):
        expected = ['-', '-', '-', '-', '-']
        self.assertEqual(check_guess('funky', 'spoil'), expected)

    def test_check_guess_all_green(self):
        expected = ['G', 'G', 'G', 'G', 'G']
        self.assertEqual(check_guess('funky', 'funky'), expected)

    def test_check_guess_greens(self):
        expected = ['-', 'G', '-', 'G', '-']
        self.assertEqual(check_guess('funky', 'sucks'), expected)

    def test_check_guess_yellows1(self):
        expected = ['-', 'Y', '-', '-', '-']
        self.assertEqual(check_guess('funky', 'after'), expected)

    def test_check_guess_yellows2(self):
        expected = ['-', 'Y', '-', 'Y', '-']
        self.assertEqual(check_guess('funky', 'afoul'), expected)

    def test_check_guess_error1(self):
        expected = []
        self.assertEqual(check_guess('funky', 'strikes'), expected)

    def test_check_guess_error2(self):
        expected = []
        self.assertEqual(check_guess('strikes', 'heart'), expected)

    def test_check_guess_error3(self):
        expected = []
        self.assertEqual(check_guess('strikes', 'classes'), expected)

if __name__ == '__main__':
    unittest.main()
