import os
import time


game_board = [[], []]
height = 20
width = 10


def initialize_board():
    global game_board
    game_board = [[' .' for i in range(width)] for j in range(height)]


def clear():
    os.system('cls')


def print_board():
    for row in range(0, height):
        print("<!", end="")
        for column in range(0, width):
            print(game_board[row][column], end="")
        print("!>\n", end="")
    print(f"<!{'=' * width * 2}!>")
    last_line = '\/' * width
    print(f"  {last_line}  ")


x = 2
y = 0
def frame():
    global x
    global y
    game_board[y-1][x] = " ."
    game_board[y][x] = "[]"
    print_board()
    y += 1
    time.sleep(1)


initialize_board()
while True:
    clear()
    frame()
