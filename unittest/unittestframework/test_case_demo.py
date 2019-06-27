import unittest


class TestCaseDemo(unittest.TestCase):

    def setUp(self):
         print(" Setup Method Will run once before every test")

    def test_methodA(self):
        print('RUNNING METHOD A')

    def test_methodB(self):
        print('RUNNING METHOD B')

    def tearDown(self):
        print("Method Teardown  will Run After Every Test")


if __name__ == '__main__':
    unittest.main(verbosity=2)

