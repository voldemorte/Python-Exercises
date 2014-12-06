#!/usr/bin/env python

import random

answer = 'yes'

count = 0

while answer.lower() != 'no':
  a = random.randint(1,9)
  guess = int(raw_input('Try to guess the number in my mind. '))
  if a > guess:
    print "You guessed too low.\n%d was right" % a
  elif a < guess:
    print "You guessed too high.\n%d was right" % a
  else:
    print "You guessed right!"

  count += 1
  answer = str(raw_input('Continue?? '))

print "You guessed %d times" % count
