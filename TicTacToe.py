import tkinter as tk
from gui import Game

import numpy as np
import random
import time


board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

computerTurn = False


def winner(turnMov):
    if turnMov == 1:
        text = "You won"
    else:
        text = "You lose"
    
    label = tk.Label(master = root, text= text, fg="grey", font=("Arial", 20))
    label.place(relx = 0.42, rely = 0.5)
    


def computerMove(board):
    if computerTurn:
        x = [0,1,2]
        y = [0,1,2]

        a = random.choice(x)
        b = random.choice(y)


        if board[1][1] != 0:
            if board[a][b] != 0:
                for a in x:
                    for b in y:
                        if board[a][b] != 0:
                            continue
                        else:
                            board[a][b] = 2
                            break
                    break
            else:
                board[a][b] = 2
        else:
            board[1][1] = 2
        
        app.draw(board)
        logic(board, 2)

def logic(board, turnMov):
    global computerTurn
    
    # Keep y constant and loop over y
    for y in range(3):
        if board[y][0] == turnMov:
            if board[y][1] == turnMov:
                if board[y][2] == turnMov:
                    winner(turnMov)
    
    # Keep x constant and loop over x            
    for x in range(3):
        if board[0][x] == turnMov:
            if board[1][x] == turnMov:
                if board[2][x] == turnMov:
                    winner(turnMov)
    
    # Keep both same and increasing. This creates the sideways check
    if board[0][0] == turnMov:
        if board[1][1] == turnMov:
            if board[2][2] == turnMov:
                winner(turnMov)
                    
    # Keep both different. one increasing and the other decreasing. This creates the reverse-sideways check
    if board[0][2] == turnMov:
        if board[1][1] == turnMov:
            if board[2][0] == turnMov:
                winner(turnMov)
                
    if computerTurn == False:
        computerTurn = True
    else:
        computerTurn = False
    
    computerMove(board)


def all_children (wid) :
    _list = wid.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list



def getPosition(event):
    canvas = [char for char in str(event.widget)]
    canvas_index = canvas[-1]
    if canvas_index == "s":
        canvas_index = 1
    
    global board
    n_board = np.array(board).reshape(1,9)
    n_board = n_board[0]
    
    
    for i in range(len(n_board)):
        if int(canvas_index) == (i+1):
            if n_board[i] == 0:
                n_board[i] = 1
    
    n_board = n_board.reshape(3,3)
    n_board = n_board.tolist()
    
    board = n_board
    
    app.draw(board)
    logic(board, 1)
    
    for canvas in all_children(app.frame):
        canvas.bind("<Button 1>", getPosition)




root = tk.Tk()

root.title("TicTacToe")
root.geometry("500x500")

app = Game(master = root,  title = "TicTacToe")


app.draw(board)

for canvas in all_children(app.frame):
    canvas.bind("<Button 1>", getPosition)




app.mainloop()