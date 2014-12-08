#!/usr/bin/env python

# https://www.hackerrank.com/challenges/nested-list/submissions/code/10515785

# There is a classroom of 'n' students and you are given their names and marks in
# physics. Store them in a nested list and print the name of each student who got the
# second lowest marks in physics.

count = int(raw_input())

db = []

for i in range(count):
  name = str(raw_input())
  marks = float(raw_input())
  db.append([marks, name])

s = sorted(db)

index = []                    # This loop keeps indices of all the least marks persons
for i in range(count):
  if s[i][0] == s[0][0]:
    index.append(i)

for i in range(index[-1]+1, count): # This loop keeps all the indices of second lowest 
  if s[i][0] == s[index[-1]+1][0]:  # persons
    print s[i][1]