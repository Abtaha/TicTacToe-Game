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
gameEnded = False

canvasId = []


def all_children (wid) :
    _list = wid.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list


def reset():
    global board 
    global computerTurn
    global gameEnded
    
    board = [[0,0,0],[0,0,0],[0,0,0]]
    computerTurn = False
    gameEnded = False
    
    
    app.draw(board)
    
    for canvas in all_children(app.frame):
        canvas.bind("<Button 1>", getPosition)


def winner(turnMov):
    if turnMov == 1:
        text = "You won"
    else:
        text = "You lose"
    
    for canvas in all_children(app.frame):
        canvas.unbind('<<Button 1>>')
    
    label = tk.Label(master = app.frame, text= text, fg="grey", font=("Arial", 20))
    label.place(relx = 0.4, rely = 0.5)
    
    button = tk.Button(master = app.frame, text= "Play Again", fg="grey", font=("Arial", 12), command= reset)
    button.place(relx = 0.43, rely = 0.6)
    
    global gameEnded
    gameEnded = True


def computerMove(board):
    if computerTurn:
        a = random.randrange(0,3)
        b = random.randrange(0,3)
        
        if board[1][1] != 0:
            if board[a][b] != 0:
                for y in range(len(board)):
                    for x in range(len(board)):
                        if board[y][x] != 0:
                            continue
                        else:
                            board[y][x] = 2
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
    
    global gameEnded
    if gameEnded != True:         
        if computerTurn == False:
            computerTurn = True
            computerMove(board)
        else:
            computerTurn = False



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
            else:
                return
    
    n_board = n_board.reshape(3,3)
    n_board = n_board.tolist()
    
    board = n_board
    
    app.draw(board)
    logic(board, 1)
    
    global gameEnded
    if gameEnded != True:
        for canvas in all_children(app.frame):
            canvas.bind("<Button 1>", getPosition)
        




root = tk.Tk()

root.title("TicTacToe")
root.geometry("500x500")

app = Game(master = root,  title = "TicTacToe", changeText = True)


app.draw(board)

for canvas in all_children(app.frame):
    canvas.bind("<Button 1>", getPosition)




app.mainloop()