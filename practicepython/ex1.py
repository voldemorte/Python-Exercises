#!/usr/bin/env python

from datetime import datetime

name = raw_input('Name: ')
age = int(raw_input('Age: '))

yr = datetime.now().year + 100 - age

print "Dear " + name + ", You will turn 100 in the year " + str(yr)

num = int(raw_input("Enter a number: "))
for i in range(num):
  print "Dear " + name + ", You will turn 100 in the year " + str(yr)