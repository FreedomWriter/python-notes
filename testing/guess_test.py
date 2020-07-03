import unittest
import guess

class TestGame(unittest.TestCase):
    def test_input(self):
        result = guess.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = guess.run_guess(0, 55)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = guess.run_guess(11, 5)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = guess.run_guess(5,'11')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()