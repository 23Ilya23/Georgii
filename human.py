from tkinter import Tk, Canvas, ARC, SE, W



class Human():


    def __init__(self, canvas):
        self.canvas = canvas
        
    def display(self):
        self.__drawHead()
        self.__drawBody()
        
        self.__drawName()
        
        
    def __drawHead(self):
        self.canvas.create_oval(20, 400, 80, 460, width=2)
        self.canvas.create_arc(30, 420, 70, 450, start=0, extent=-180,
             style=ARC, outline="red", width = 3)
        self.canvas.create_oval(35, 421, 43, 429, width=0, fill="blue")
        self.canvas.create_oval(65, 420, 57, 428, width=0, fill="blue")
    


    def __drawName(self):
        self.canvas.create_text(50, 380, fill="black", font="Times 20 italic bold", text ="Георгий")
  
    def __drawBody(self):
        self.canvas.create_line(50, 460, 50, 550, width=2)
        
        
                #armLeft
        
        self.canvas.create_line(50, 490, 100, 430, width=2,)
        
        
                        #armRight
        
        self.canvas.create_line(50, 490, 0, 430, width=2,)
        
        
                        #legLeft
        
        self.canvas.create_line(50, 550, 80, 600, width=2,)
        
        
                        #legRight
        
        self.canvas.create_line(50, 550, 20, 600, width=2,)
        
        
