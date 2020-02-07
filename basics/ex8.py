#!/bin/python3.6

import random

def game(start, end):
	random_int = random.randint(start, end)
	if int(input("Enter int: ")) == random_int:
		pass
	else
		print("Try again!")
