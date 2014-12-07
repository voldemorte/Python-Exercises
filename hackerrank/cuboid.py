#!/usr/bin/env python

# Lets learn about list comprehensions!. You are given three integers X, Y
# and Z denoting the dimensions of a Cuboid. You have to print a list of
# all possible coordinates on the three dimensional grid, such that at any
# point the sum Xi + Yi + Zi is not equal to N. If X = 2, then possible
# values of Xi can be 0, 1 and 2. The same applies to Y and Z.

x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
n = int(raw_input())

lst = []

for i in range(0,x+1):
  for j in range(0,y+1):
    for k in range(0,z+1):
      lst.append([i, j, k])
      
#print lst

out = [l for l in lst if l[0] + l[1] + l[2] != n ]

print out