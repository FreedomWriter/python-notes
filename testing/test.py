import unittest
import main

# python3 test.py to run tests in this file
# python3 -m unittest to run all unit test files
# python3 -m unittest -v to get verbose test results
# can add -v to python3 test.py -v

class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')

    def test_do_stuff(self):
        '''doc strings can be added so that explainations can be added to verbose testing'''
        test_param = 10
        test = main.do_stuff(test_param)
        self.assertEqual(test, 15)

    def test_do_stuff_value(self):
        test_param = "TypeError fail"
        test = main.do_stuff(test_param)
        self.assertTrue(isinstance(test, ValueError))
        self.assertIsInstance(test, ValueError)

    def test_do_stuff_float(self):
        test_param = 10.5
        test = main.do_stuff(test_param)
        self.assertEqual(test, 15.5)

    def test_do_stuff_none(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def test_do_stuff_empty_string(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def test_do_stuff_zero(self):
        test_param = 0
        test = main.do_stuff(test_param)
        self.assertEqual(test, 5)
    
    def tearDown(self):
        print('cleaning up!!')

if __name__ == '__main__':
    unittest.main()

# Method                        Checks that           New in

# assertEqual(a, b)             a == b

# assertNotEqual(a, b)          a != b

# assertTrue(x)                 bool(x) is True

# assertFalse(x)                bool(x) is False

# assertIs(a, b)                a is b                  3.1

# assertIsNot(a, b)             a is not b              3.1

# assertIsNone(x)               x is None               3.1

# assertIsNotNone(x)            x is not None           3.1

# assertIn(a, b)                a in b                  3.1

# assertNotIn(a, b)             a not in b              3.1

# assertIsInstance(a, b)        isinstance(a, b)        3.2

# assertNotIsInstance(a, b)     not isinstance(a, b)    3.2