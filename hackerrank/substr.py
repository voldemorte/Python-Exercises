#!/usr/bin/env python

# https://www.hackerrank.com/challenges/find-a-string

# The user enters a string and a substring and you have to print the number of times
# that substring occurs in that string.
# NOTE : Letters of string are case-sensitive.

strin = str(raw_input())
substr = str(raw_input())

count = 0
for i in range(len(strin)):
  if substr[0] == strin[i] and not cmp(substr, strin[i:i + len(substr)]):
    count += 1

print count