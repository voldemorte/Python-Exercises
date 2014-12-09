#!/usr/bin/env python

# You are given 'n' numbers. Store them in a list and find the second largest number.

ln = int(raw_input())

lst = map(int, raw_input().split())
lst.sort(reverse=True)

for i in range(len(lst)):
  if lst[i] != lst[0]:
    break

print lst[i]