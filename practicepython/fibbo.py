#!/usr/bin/env python

def fibbo(len):
  if len == 1:
    return [1]
  elif len == 2:
    return [1, 1]
  else:
    start = [1, 1]
    for i in range(0,len-2):
      start.append( start[-1] + start [-2] )

  return start

len = int(raw_input('Enter the length of the series: '))

print fibbo(len)
