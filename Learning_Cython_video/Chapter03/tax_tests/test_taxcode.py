""" Pytest test file.

To run these tests, at the command line, run:
    pytest
or
    py.test
"""
from taxcode import tax_table
import numpy
import pytest

def test_notax():
    """ Test when a low income is provided - calculated tax should be zero """
    ans = tax_table(500)
    # Check that the tax is very close to zero to deal with floating-point precision issues
    numpy.testing.assert_allclose(ans, 0)

def test_notax_edge():
    """ Check edge case on low tax, from below """
    ans = tax_table(18200)
    numpy.testing.assert_allclose(ans, 0)

def test_notax_over_edge():
    """ Check edge case on low tax, from above """
    ans = tax_table(18201)
    numpy.testing.assert_allclose(ans, 0.19)

def test_str():
    """ Ensure TypeError gets raised if someone passes a string in """
    with pytest.raises(TypeError) as excinfo:
        ans = tax_table('nonsense')

def test_nothing():
    """ Verify that TypeError gets raised if function called with no arguments """
    with pytest.raises(TypeError) as excinfo:
        ans = tax_table()

def test_negative():
    """ Make sure negative input values are dealt with appropriately """
    ans = tax_table(-1e6)
    numpy.testing.assert_allclose(ans, 0)

def test_main():
    """ Verify the final tax result is correct """
    import main2
    ans = main2.tot()
    numpy.testing.assert_allclose(
            ans, 517474750456.53094)
