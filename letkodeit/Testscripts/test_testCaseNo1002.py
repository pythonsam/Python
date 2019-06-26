from selenium import webdriver
import unittest
import os
import traceback
import time

from Syslibrary.datadriver import readjson
jsonread1 =readjson()

from Library.Launchapplication import launchapplication
application = launchapplication()

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

folder_path = os.path.abspath(os.path.join(dir_path, os.pardir))
print(folder_path)

tf = 'test_TestcaseNo1002'

class TestcaseNo1002(unittest.TestCase):
    def test_TestcaseNo1002(self):
        try:
