#!/usr/bin/env python

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

## Main problem
for i in a:
  if i < 5:
    print i


## Extras 1,2
less_than_5 = [i for i in a if i < 5]
print less_than_5

## Extras 3
num = int(raw_input())
print [i for i in a if i < num]