import unittest


class AssertDemo(unittest.TestCase):
    def test_assertTrueFalse(self):
        a = True
        self.assertFalse(a, 'a is Not True')
        b = False
        self.assertFalse(b, 'b is Not False')

    def test_assertEqual(self):
        a = 'Test'
        b = 'test'
        self.assertEqual(a, b, msg="a is not equal to b ")


if __name__ == '__main__':
    unittest.main(verbosity=2)




