import unittest


class TestClass2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Class 2 --> Class Level Setup ')

    def setUp(self):
         print("Class-2 --> Setup  ")

    def test_methodA(self):
        print('Class-2 --> RUNNING METHOD A')

    def test_methodB(self):
        print('Class -2 --> RUNNING METHOD B')

    def tearDown(self):
        print("Class 2 --> teardown")

    @classmethod
    def tearDownClass(cls):
        print('Class -2 ---> Class level  teardown  ')


if __name__ == '__main__':
    unittest.main(verbosity=2)

