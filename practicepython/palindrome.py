#!/usr/bin/env python

user_in = str(raw_input("String: "))

if user_in == user_in[::-1]:
  print "Palindrome"
else:
  print "Not Palindrome"