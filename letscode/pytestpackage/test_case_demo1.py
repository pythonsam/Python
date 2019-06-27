
"""
to run the scripts

C:\Python36 py.test ---> To know the how many fun/tests available
"""

import pytest

#@pytest.mark.flaky(rerun=5)
@pytest.fixture()
def setup():
    print('Once before every method')


def test_methodA(setup):
    print ("Running Method A")


def test_methodB(setup):
    print("Running Method B")