#Importing the Tkinter module library
from tkinter import *

#Importing the random function
import random

#Tic Tac Toe Game
# -Game class to group our functions together
# -Display (x,y)
# -Board (rows and columns)
# -Place pieces ('x', 'o')

#Defining the functions that we will need
def next_turn():
    pass 

def check_winner():
    pass

def empty_spaces():
    pass

def new_game():
    pass

#Creating the basic window interface
window = Tk()
window.title("Tic-Tac-Toe")
window.configure(width = 600, height = 400)

#Creating a list of players
list_players = ["player_1 (O)","player_2 (X)"]

#Selecting a random player by passing our list of players
player = random.choice(list_players)

#Creating a 2D list of tiles
tiles = []
rows, cols = 3,3
for i in range (rows):
    col = []
    for j in range (cols):
        col.append(0)
    tiles.append(col)
print(tiles)

#2D list of tiles
# tiles = [[0, 0, 0],
#          [0, 0, 0],
#          [0, 0, 0]]

#Helps display the users turn
turn = Label(text = player + " turn ", font = ('consolas',40))
turn.pack(side="top")

#Restarts the game button
reset_button = Button(text = "restart", font=('consolas', 20), command = new_game)
reset_button.pack (side = "top")

#A frame is used as the foundation class to implement complex widgets
frame = Frame(window)
#Makes the program fill in the window
frame.pack()

#Nested for loop to diplsay the grid and the text
for x in range(rows):
    col = []
    for y in range (cols):
        tiles [x][y] = Button(frame, text="",font = ('consolas', 40), width = 5, height =2, command = lambda row=x, column=y: next_turn(rows))
        tiles[x][y].grid(row=x, column=y)
window.mainloop()
