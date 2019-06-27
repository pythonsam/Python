import unittest


class TestCaseDemo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('I Will Run before All the Tests ')

    def setUp(self):
         print(" Setup Method Will run once before every test")

    def test_methodA(self):
        print('RUNNING METHOD A')

    def test_methodB(self):
        print('RUNNING METHOD B')

    def tearDown(self):
        print("Method Teardown  will Run After Every Test")

    @classmethod
    def tearDownClass(cls):
        print('I Will Run After All the Tests ')


if __name__ == '__main__':
    unittest.main(verbosity=2)

