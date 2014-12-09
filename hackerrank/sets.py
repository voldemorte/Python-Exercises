#!/usr/bin/env python

# https://www.hackerrank.com/challenges/sets

# You are given two set of integers M and N and you have to print their
# symmetric difference in ascending order. The first line of input contains
# value of M followed by M integers, then value of N followed by N integers.

l1 = int(raw_input())
s1 = set(map(int, raw_input().split()))
l2 = int(raw_input())
s2 = set(map(int, raw_input().split()))

un = s1.union(s2)
inter = s1.intersection(s2)

ans = sorted(un.difference(inter))

for i in ans:
  print i