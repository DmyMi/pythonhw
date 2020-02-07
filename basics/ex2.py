#!/bin/python3.6
def _sum(arr):
	return sum(arr) 

def multiply(arr):
	if not arr:
		return 1
	return arr[0] * multiply(arr[1:])
