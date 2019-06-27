"""
to run the scripts

C:\Python36 py.test ---> To know the how many fun/tests available
C:\Python36 py.test -v -s D:\sdet\Python\letscode
"""
import pytest


# Setup method
@pytest.yield_fixture()
def setup():
    print('Once before every method')
    yield
    print('Once after every method')


def test_methodA(setup):
    print('Running Method A')


def test_methodB(setup):
    print('Running Method B')

