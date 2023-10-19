import pytest
def test_name():
  assert True

from example_package.example import monte_carlo_integration


def func(x):
    return x

@pytest.mark.parametrize("func,a,b,n,expected", [(func, 0,1,100, 0.5), (func, 0,2,100,2)])
def test_mcint(func,a,b,n, expected):

    assert abs(monte_carlo_integration(func, a, b, n) - expected) < 0.1 
            