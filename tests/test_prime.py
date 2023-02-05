import pytest

from prime.check_prime import is_prime
from prime.check_prime import get_primes_from_list

# test is_prime
@pytest.mark.parametrize("num, result", [
    # xfail test to proof the test_is_prime(num, result) function can catch expected failure
    pytest.param(3, False, marks=pytest.mark.xfail),
    (2, True),
    (4, False),
    (1991, False),
    (2999, True)
    ])
def test_is_prime(num, result):
    assert is_prime(num) == result

# test get_primes_from_list
@pytest.mark.parametrize("num_list, result", [
    # xfail test to proof the test_get_primes_from_list() function can catch expected failure
    pytest.param([2], [3], marks=pytest.mark.xfail),
    ([2], [2]),
    ([-2,3,4,5], [3,5]),
    ([10,23,35,47], [23, 47])
    ])
def test_get_primes_from_list(num_list, result):
    assert list(get_primes_from_list(num_list)) == result
