#!/usr/bin/env python

# https://www.hackerrank.com/challenges/map-and-lambda-expression

# You have to generate a list of the first N fibonacci numbers, 0 being the first
# number. Then, apply the map function and a lambda expression to cube each fibonacci
# number and print the list.

ln = int(raw_input())

fibbo = [0, 1]

if ln < 3:
  fibbo = fibbo[0:ln]
else:
  for i in range(0, ln-2):
    fibbo.append(fibbo[-1] + fibbo[-2])

cube = lambda c: c * c * c

print map(cube, fibbo)