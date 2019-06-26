import os
import unittest
from Library.HTMLTestRunner import HTMLTestRunner

from Testscripts.test_testCaseNo1001 import TestcaseNo1001

dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path = os.path.abspath(os.path.join(dir_path, os.pardir))


# importing individual test scripts
""" Note: Reason for making individual test scripts - 
As per standard framework guidelines - Each test script should be independent one
"""
suite = unittest.TestSuite()

suite.addTest(TestcaseNo1001('test_TestcaseNo1001'))

outfile = open(folder_path + '\Regressionreport\Regressionreport.html', 'w+')
runner = HTMLTestRunner(stream=outfile, verbosity=1, title='           Lets Kode IT', description='Regressionreport', dirTestScreenshots =folder_path + '\\Screenshots')
runner.run(suite)
outfile.close()
