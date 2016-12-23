
""" Taxable income of 11 million people.

This is a refactored version of main.py which is more suitable for testing.
"""

import numpy
from numpy.random import RandomState
# Ensure the same set of random numbers are generated each time
prng = RandomState(1)
taxable_incomes = prng.uniform(
        5e3, 3e5, int(11e6))
# taxable_incomes = numpy.random.uniform(
#         5e3, 3e5, int(11e6))

# Calculate the tax table.

import taxcode

def tot():
    """ Compute the total tax """
    total_tax = 0
    for income in taxable_incomes:
        total_tax += taxcode.tax_table(income)
    return total_tax

def run():
    """ main() runner """
    total_tax = tot()
    print("""
        Australian Tax due for 2015/2016
        ================================

        AUD {:.2f} BN
    """.format(total_tax/1e9))

if __name__ == '__main__':
    run()
