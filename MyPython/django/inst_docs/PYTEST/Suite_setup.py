import pytest

def setup_module():   # It will execute before all test cases
    print('\n Suite Setup ')

def teardown_module():   # It will execute after all test cases
    print('\n Suite Teardown')

def test_add():
    print('\n Add fun')

def test_mul():
    print('\n Mul fun')

def setup_function():   # It will execute before each test casessetup_function
    print('\n Setup function')

def teardown_function():   # It will execute after each test cases
    print('\n Teardown function')
