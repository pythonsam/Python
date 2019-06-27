"""
pre conditions
1.pip3 install pytest-ordering

Generator
@pytest.mark.run(order =1)

"""

import pytest


@pytest.mark.run(order=2)
def test_run_order_methoA(onetimesetup, setup):
    print('Running Method A')


@pytest.mark.run(order=1)
def test_run_order_methoB(onetimesetup, setup):
    print('Running Method B')


@pytest.mark.run(order=4)
def test_run_order_methoC(onetimesetup, setup):
    print('Running Method C')


@pytest.mark.run(order=5)
def test_run_order_methoD(onetimesetup, setup):
    print('Running Method D')


def test_run_order_methoE(onetimesetup, setup):
    print('Running Method E')






