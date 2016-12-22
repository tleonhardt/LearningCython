#!/usr/bin/env python
""" This algorithm stores all of the words in 'wordlist.txt' in a set.
Membership testing in a set is an O(1) operattion.
"""

# This is our dictionary
with open('wordlist.txt', 'r') as f:
    words = set(f.readlines())

# Check this document for incorrect words
with open('document.txt', 'r') as f:
    for word in f:
        if not word in words:
            print('Not found: {}'.format(word.strip()))
