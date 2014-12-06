#!/usr/bin/env python

# https://www.hackerrank.com/challenges/basic-calculator

# Lets build a calculator! You are given two real numbers and your task is
# to print the
#
#    Addition
#    Subtraction
#    Multiplication
#    Divison
#    Integer Divison
#
# of the two numbers in 5 separate lines. Keep a precision of two digits
# after decimal.

num1 = float(raw_input())
num2 = float(raw_input())

print "%.2f" % (num1 + num2)
print "%.2f" % (num1 - num2)
print "%.2f" % (num1 * num2)
print "%.2f" % (num1 / num2)
print "%.2f" % (num1 // num2)