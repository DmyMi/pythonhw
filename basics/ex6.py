#!/bin/python3.6

def caesarCipher(str, number):
	return list(map(lambda x: chr(ord(x) + number), str))
