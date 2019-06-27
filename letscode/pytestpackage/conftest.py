import pytest
# Setup method


@pytest.yield_fixture()
def setup():
    print('Running conftest method level setup')
    yield
    print('Running conftest method level teardown')


@pytest.yield_fixture(scope='class')
# @pytest.yield_fixture(scope='module')
def onetimesetup(browser,osType):
    print('Running conftest onetime setup')
    if browser == 'firefox':
        print('Running tests on FF')
    else:
        print('Running tests o Chrome')

    yield
    print('Running conftest onetime teardown')

# Command line arguments
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of Operationg System ")


@pytest.fixture(scope = 'session')
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope ='session')
def osType(request):
    return request.config.getoption("--osType")



