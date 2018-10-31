#!/bin/python3.6

def charFreq(str):
	char_map = dict()
	for c in str:
		if c in char_map:
			char_map[c] += 1
		else:
			char_map[c] = 1
	return char_map
