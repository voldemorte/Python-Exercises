#!/usr/bin/env python

# https://www.hackerrank.com/challenges/baconian-cipher

## Don't know why I did this :P

cypher = {'a': '-----', 'n': '-**-*',
	  'b': '----*', 'o': '-***-',
	  'c': '---*-', 'p': '-****',
	  'd': '---**', 'q': '*----',
	  'e': '--*--', 'r': '*---*',
	  'f': '--*-*', 's': '*--*-',
	  'g': '--**-', 't': '*--**',
	  'h': '--***', 'u': '*-*--',
	  'i': '-*---', 'v': '*-*-*',
	  'j': '-*--*', 'w': '*-**-',
	  'k': '-*-*-', 'x': '*-***',
	  'l': '-*-**', 'y': '**---',
	  'm': '-**--', 'z': '**--*' }
	  
input = str(raw_input())

for i in range(len(input)):
  print cypher[input[i]]