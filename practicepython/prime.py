#!/usr/bin/env python

from sys import exit

num = int( raw_input('Enter a number: ') )

for i in range( 2, num/2 + 1 ):
  if num % i == 0:
    print "%d is not a prime number" % num
    exit()

print "%d is a Prime number!" % num
