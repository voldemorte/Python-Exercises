#!/usr/bin/env python

num = int(raw_input())

print [ n for n in range(2, (num + 1) / 2) if num % n == 0 ]