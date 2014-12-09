#!/usr/bin/env python

# https://www.hackerrank.com/challenges/finding-the-percentage

#There is a record of 'n' students, each record having name of student, percent marks
# obtained in Maths, Physics and Chemistry. Marks can be floating values. The user
# enters an integer 'n' followed by names and marks for the 'n' students. You are
# required to save the record in a dictionary data type. The user then enters name of a
# student and you are required to print the average percentage marks obtained by that
# student, correct to two decimal places.

len = int(raw_input())

records = {}

for i in range(len):
  s = raw_input().split()
  marks = map(float, s[1::])
  records[str(s[0])] = marks

search = str(raw_input())

add = 0.0

for i in records[search]:
  add += i

print "%.2f" % float(add/3.0)