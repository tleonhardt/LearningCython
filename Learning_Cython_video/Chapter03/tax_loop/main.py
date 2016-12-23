#!/usr/bin/env python

# Taxable income of 11 million people

import numpy
from numpy.random import RandomState
prng = RandomState(1)
taxable_incomes = prng.uniform(
        5e3, 3e5, int(11e6))
# taxable_incomes = numpy.random.uniform(
#         5e3, 3e5, int(11e6))

# Calculate the tax table.

import taxcode

def run():
    total_tax = taxcode.tot(taxable_incomes)
    print("""
        Australian Tax due for 2015/2016
        ================================

        AUD {:.2f} BN
    """.format(total_tax/1e9))

if __name__ == '__main__':
    run()
