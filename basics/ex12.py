#!/bin/python3.6
from random import randint, choice

HORIZ = 0
VERT = 1


def init_field(n):
    return [[0 for y in range(n)] for x in range(n)]


def try_set(field, l, x, y, position):
    if position == HORIZ:
        i = 0
        if x - 1 >= 0 and field[y][x - 1] == 1:
            return False
        if x + l < n and field[y][x + l] == 1:
            return False
        while i < l:
            if y + 1 < n and field[y + 1][x + i] == 1:
                return False
            if y - 1 >= 0 and field[y - 1][x + i] == 1:
                return False
            if field[y][x + i] == 1:
                return False
            i += 1
    elif position == VERT:
        i = 0
        if y - 1 >= 0 and field[y - 1][x] == 1:
            return False
        if y + l < n and field[y + l][x] == 1:
            return False
        while i < l:
            if x + 1 < n and field[y + i][x + 1] == 1:
                return False
            if x - 1 >= 0 and field[y + i][x - 1] == 1:
                return False
            if field[y + i][x] == 1:
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
    if not cords:
        return
    place = choice(cords)
    position = place[2]
    x = place[0]
    y = place[1]
    if position == HORIZ:
        i = 0
        while i < l:
            field[y][x + i] = 1
            i += 1
    elif position == VERT:
        i = 0
        while i < l:
            field[y + i][x] = 1
            i += 1

def print_map(arr):
    i = 1
    print('  ' + ' '.join([str(x) for x in range(1, len(arr) + 1)]))
    for line in arr:
        print(f"{i} ", end="")
        i += 1
        for char in line:
            char = str(char)
            if char == "0":
                c = "~"
            elif char == "1":
                c = "~"
            elif char == "2":
                c = "X"
            print(c + " ", end="")
        print()

def game(n):
    arr = init_field(n)
    add_ship(arr, 3)
    add_ship(arr, 1)
    add_ship(arr, 2)
    add_ship(arr, 3)
    add_ship(arr, 4)
    add_ship(arr, 5)
    print_map(arr)
    while True:
        try:
            cords = [int(x) for x in input("Enter x, y: ").split()]
        except ValueError:
            continue
        if len(cords) != 2 or not (n > cords[0] - 1 >= 0) or not (n > cords[1] - 1 >= 0):
            continue
        x, y = cords[0] - 1, cords[1] - 1
        if (arr[y][x] == 1):
            msg = "You hit in ship!"
            arr[y][x] = 2
        else:
            msg = "You missed!"
        print_map(arr)
        print(msg)

try:
    n = int(input("Enter size of sea: "))
except ValueError:
    print("Error")
    exit()
game(n)
