#!/usr/bin/env python

import os

def compare(u1, u2):
  if u1 == u2:
    print "It's a tie!"
  elif ( ( u1 == 'rock')  & ( u2 == 'scissors' ) ) | ( ( u1 == 'scissors' ) & ( u2 == 'paper' ) ) | ( ( u1 == 'paper' ) & ( u2 == 'rock' ) ):
    print "User 1 won with %s" % u1
  elif ( ( u2 == 'rock')  & ( u1 == 'scissors' ) ) | ( ( u2 == 'scissors' ) & ( u1 == 'paper' ) ) | ( ( u2 == 'paper' ) & ( u1 == 'rock' ) ):
    print "User 2 won with %s" % u2
  else:
    print "Someone entered wrong input :P"

answer = 'yes'

while answer.lower() != 'no':
  user1 = str(raw_input('Rock, Paper, Scissors? '))
  user2 = str(raw_input('Rock, Paper, Scissors? '))
  compare( user1.lower(), user2.lower() )

  answer = str( raw_input('Continue? ') )

  os.system('clear')
