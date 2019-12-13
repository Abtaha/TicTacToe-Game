import tkinter as tk


class Game(tk.Frame):
    def __init__(self, master=None, colorCoded=False, title=""):
        super().__init__(master)
        
        self.title = title
        
        self.master = master
        self.colorCoded = colorCoded
        self["bg"] = "#F3F1E9"
        
        self.place(relwidth=1, relheight=1)
        
    def colorCoding(self,text):
        if text == "2":
            return "#E7DED4", "#7B7269"
        elif text == "4":
            return "#E7DAC3", "#7B7269"
        elif text == "8":
            return "#EBAC76", "#7B7269"
        elif text == "16":
            return "#EE9160","#EEEEEE"
        elif text == "32":
            return "#EF795C","#EEEEEE"
        elif text == "64":
            return "#EC5E35","#EEEEEE"
        elif text == "128":
            return "#EBAC76", "#7B7269"
        elif text == "256":
            return "#E5CA57", "#7B7269"
        elif text == "512":
            return "#E6C34E", "#7B7269"
        else:
            return "#C7BBAF", "#7B7269"
    
    def draw(self, board):
        title = tk.Label(self, text = self.title, fg = "#7B7269")
        title.place(relwidth = 1, relheight = 0.15)
        title.config(font=("Arial", 30))
        
        self.frame = tk.Frame(self)
        self.frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely=0.15)

        a = 1 / len(board)
        for y in range(len(board)):
            for x in range(len(board[y])):
                text = board[y][x]
                
                if self.colorCoded == True:
                    bgcolor, fgcolor = self.colorCoding(str(text))
                else:
                    bgcolor, fgcolor = "#C7BBAF", "#7B7269"
                    
                
                canvas = tk.Canvas(self.frame, bg=bgcolor, highlightthickness=3, highlightbackground="#B5A9A3")
                canvas.place(relwidth = a, relheight = a, relx = a*x, rely = a*y)
                
                canvas.create_text(50, 50, anchor="center", font=("Purisa", 20), text=text, fill=fgcolor)