#!/usr/bin/env python
""" Calculate taxable income of 11 million people
"""

import numpy
taxable_incomes = numpy.random.uniform(
        5e3, 3e5, int(11e6))

# Calculate the tax table.

import taxcode

total_tax = 0
for income in taxable_incomes:
    total_tax += taxcode.tax_table(income)

print("""
    Australian Tax due for 2015/2016
    ================================

    AUD {:.2f} BN
""".format(total_tax/1e9))
