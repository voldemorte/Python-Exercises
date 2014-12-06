#!/usr/bin/env python

# Ask user for even or odd number
# 
# Extras 
# 1. If the number is a multiple of 4, print out a different message.
# 2. Ask the user for two numbers: one number to check (call it num) and one
# number to divide by (check). If check divides evenly into num, tell that
# to the user. If not, print a different appropriate message.

num = int(raw_input("Number: "))

if num % 4 == 0:
  print "%d is a multiple of 4." % num
elif num % 2 == 0:
  print "%d is even." % num
else:
  print "%d is odd." % num

# Part 2
num = int(raw_input("Number: "))
check = int(raw_input("Check: "))

if num % check == 0:
  print "%d divides evenly in %d." % (check, num)
else:
  print "%d does not divide evenly in %d." % (check, num)