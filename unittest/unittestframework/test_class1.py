import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from unittestframework.test_class2 import TestClass2

class TestClass1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Class 1 --> Class Level Setup ')

    def setUp(self):
         print("Class-1 --> Setup  ")

    def test_methodA(self):
        print('Class-1 --> RUNNING METHOD A')

    def test_methodB(self):
        print('Class -1 --> RUNNING METHOD B')

    def tearDown(self):
        print("Class 1 --> teardown")

    @classmethod
    def tearDownClass(cls):
        print('Class -1 ---> Class level  teardown  ')


if __name__ == '__main__':
    unittest.main(verbosity=2)

