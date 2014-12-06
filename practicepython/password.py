#!/usr/bin/env python

#Write a password generator in Python. Be creative with how you generate
#passwords - strong passwords have a mix of lowercase letters, uppercase
#letters, numbers, and symbols. The passwords should be random, generating
#a new password every time the user asks for a new password. Include your
#code in a main method.

import random

s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=[]\\;\',./"!@#$%^&*()_+{}|:"<>?'

passlen = 9

print "".join(random.sample(s, passlen))