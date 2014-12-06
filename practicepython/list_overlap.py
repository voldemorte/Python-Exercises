#!/usr/bin/env python

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#lst = [ i for i in a if i in b && i in lst ]

out = []

for i in a:
  if i in b:
    if i in out:
      o = i
    else:
      out.append(i)

print out

lst = [ i for i in a if i in b and i not in lst ]

print lst