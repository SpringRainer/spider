import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_something_01(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
