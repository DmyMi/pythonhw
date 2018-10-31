#!/bin/python3.6
def	check(str):
	i = 0
	for char in str:
		if char == "[":
			i += 1
		elif char == "]":
			i -= 1
		if i < 0:
			print("NOT OK")
			return
	if i != 0:
		print("NOT OK")
	else:
		print("OK")
