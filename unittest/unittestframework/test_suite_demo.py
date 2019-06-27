"""
Get all the Test from TestClass1 and TestClass2
Create a Test suite to combilne all the Testclass1 and TestClass2
"""

import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


from unittestframework.test_class2 import TestClass2
from unittestframework.test_class1 import TestClass1

# Get all the Test from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)

# Create a Test suite to combine all the Test class1 and TestClass2
reg_test = unittest.TestSuite([tc1, tc2])

# RUn the TestSuite
unittest.TextTestRunner(verbosity= 2).run(reg_test)
