#Importing the Tkinter module library
from tkinter import *

#Importing the random function
import random

#Tic Tac Toe Game
# -Game class to group our functions together
# -Display (x,y)
# -Board (rows and columns)
# -Place pieces ('x', 'o')

#variables
size = 900

class Tic_Tac_Toe():
    def __init__(self):
        #Creating the basic window interface
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.configure(size, height = size)
        self.canvas = Canvas(self.window,width=size , height=size)
        self.canvas.pack()
        self.window.bind('<Button-1>', self.click)
        self.initialize_board()
        self.Turn = True
        self.restart = False
        self.X_Score = 0
        self.O_Score = 0
        
    def main_loop(self):
        self.window.mainloop()

    def create_board(self):
        for i in range(2):
            self.canvas.create_line((i + 1) * size / 3, 0, (i + 1) * size / 3, size)

        for i in range(2):
            self.canvas.create_line(0, (i + 1) * size / 3, size, (i + 1) * size / 3)


    def next_turn():
        pass 

    def check_winner():
        pass

    def empty_spaces():
        pass

    def new_game():
        pass

    #Helps display the users turn
    turn = Label(text =  " turn ", font = ('consolas',40))
    turn.pack(side="top")

    #Restarts the game button
    reset_button = Button(text = "restart", font=('consolas', 20), command = new_game)
    reset_button.pack (side = "top")
    
    
    
Tk = mainloop()
Tk.mainloop()




