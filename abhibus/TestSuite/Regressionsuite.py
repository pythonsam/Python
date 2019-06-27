import unittest
import os
import HtmlTestRunner
from Library.HTMLTestRunner import HTMLTestRunner

# Current Working Folder
dir_path = os.path.dirname(os.path.realpath(__file__))

# Parent Folder
folder_path = os.path.abspath(os.path.join(dir_path, os.pardir))

from TestScripts.testCaseNo100001 import TestCaseNo100001

suite = unittest.TestSuite()
# Collecting as a Suite
suite.addTest(TestCaseNo100001('test_TestcaseNo100001'))

outfile = file(folder_path + '\RegressionReport\Regressionreport.html', 'w+')
runner = HTMLTestRunner(stream=outfile, verbosity=1, title='  Abhibus', description='  Regression Report', dirTestScreenshots =folder_path + '\Screenshots')
runner.run(suite)
outfile.close()