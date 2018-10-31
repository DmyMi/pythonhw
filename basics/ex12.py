#!/bin/python3.6
from random import randint, choice

HORIZ = 0
VERT = 1

def create_board(n):
	board = list()
	for i in range(n):
		tmp_lst = list()
		for i in range(n):
			tmp_lst.append(0)
		board.append(tmp_lst)
	return board

def try_set(field, l, x, y, position):
	if position == HORIZ:
		i = 0
		while i < l:
			if field[y][x + l - 1] == 1:
				return False
			i += 1
	elif position == VERT:
		i = 0
		while i < l:
			if field[y + l - 1][x] == 1:
				return False
			i += 1
	return True

def find_places(field, l):
	cords = list()
	n = len(field)
	for i in range(n):
		for j in range(n):
			if j + l <= n and try_set(field, l, j, i, HORIZ):
				cords.append((j, i, HORIZ))
			if i + l <= n and try_set(field, l, j, i, VERT):
				cords.append((j, i, VERT))
	return cords


def add_ship(field, l):
	
	cords = find_places(field, l)
	place = choice(cords)
	position = place[2]
	x = place[0]
	y = place[1]
	if position == HORIZ:
		i = 0
		while i < l:
			field[y][x + l - 1] = 1
			i += 1
	elif position == VERT:
		i = 0
		while i < l:
			field[y + l - 1][x] = 1
			i += 1


def game(n):
	arr = create_board(n)
	print(arr)
	add_ship(arr, 3)
	for x in arr:
		print("".join(
	list(map(lambda x: "-".join(str(x)), arr))
n = 3
game(3)
