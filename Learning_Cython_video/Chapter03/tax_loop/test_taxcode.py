from taxcode import tax_table, tot
import numpy
import pytest

def test_notax():
    ans = tax_table(500)
    numpy.testing.assert_allclose(ans, 0)

def test_notax_edge():
    ans = tax_table(18200)
    numpy.testing.assert_allclose(ans, 0)

def test_notax_over_edge():
    ans = tax_table(18201)
    numpy.testing.assert_allclose(ans, 0.19)

def test_str():
    with pytest.raises(TypeError) as excinfo:
        ans = tax_table('nonsense')

def test_nothing():
    with pytest.raises(TypeError) as excinfo:
        ans = tax_table()

def test_negative():
    ans = tax_table(-1e6)
    numpy.testing.assert_allclose(ans, 0)

def test_main():
    import main
    ans = tot(main.taxable_incomes)
    numpy.testing.assert_allclose(
            ans, 517474750456.53094)

