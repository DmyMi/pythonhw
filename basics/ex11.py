#!/bin/python3.6

def decToBin(nbr: int):
	BIN_STR = "01"
	nbr_tmp = nbr
	len = 0
	while nbr:
		len += 1
		nbr //= 2
	nbr = nbr_tmp
	num_repr = list()
	i = 0
	while nbr:
		num = BIN_STR[nbr % 2]
		nbr //= 2
		num_repr.append(num)
	print("".join(num_repr[::-1]))
