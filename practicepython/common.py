#!/usr/bin/python

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
out = []

for i in a:
  if i in out:
    None
  elif i in b:
    out.append(i)
    
print "The common elements are " + str(out)
