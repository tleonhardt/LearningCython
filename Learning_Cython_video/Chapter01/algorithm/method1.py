#!/usr/bin/env python
""" This algorithm stores all of the words in 'wordlist.txt' in a list.
Membership testing in a list is an O(N) operattion.
"""

# This is our dictionary
with open('wordlist.txt', 'r') as f:
    words = f.readlines()

# Check this document for incorrect words
with open('document.txt', 'r') as f:
    for word in f:
        if not word in words:
            print('Not found: {}'.format(word.strip()))
