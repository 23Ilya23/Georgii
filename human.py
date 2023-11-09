from tkinter import Tk, Canvas, ARC, SE, W



class Human():


    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        
    def display(self):
      #  self.__drawHead()
     #   self.__drawBody()
        
      #  self.__drawName()
      
      
      
      
      
     #   self.__drawBodyXY()
        
        self.__drawLeggsXY()
        
        self.__drawArmLeftXY()
        
        self.__drawArmRghtXY()
        
        self.__drawHeadXY()
        
        self.__drawFaceXY()
        
        self.__drawNameXy()
        
        
 
    
   
   
   
   
     
    def __drawLeggsXY(self):
        self.canvas.create_line(self.x, self.y, self.x+50, self.y-50, self.x+100, self.y, width=2)
        
    def __drawBodyXY(self):
        self.canvas.create_line(self.x, self.y, self.x+50, self.y-50, self.x+50, self.y-180, width=2)
        
        
    def __drawArmLeftXY(self):
        self.canvas.create_line(self.x, self.y, self.x+50, self.y-50, self.x+50, self.y-150, self.x+90, self.y-100, width=2)
        
    def __drawArmRghtXY(self):
        self.canvas.create_line(self.x, self.y, self.x+50, self.y-50, self.x+50, self.y-150, self.x+10, self.y-100, width=2)
   
   
    def __drawHeadXY(self):
        self.canvas.create_oval(self.x+90, self.y-220, self.x+5, self.y-150, width=2)
        
        
    def __drawFaceXY(self):
        self.canvas.create_arc(self.x+70, self.y-195, self.x+20, self.y-160, start=0, extent=-180,
             style=ARC, outline="red", width = 3)
             
        self.canvas.create_oval(self.x+30, self.y-195, self.x+20, self.y-180, width=0, fill="blue")
        self.canvas.create_oval(self.x+70, self.y-195, self.x+60, self.y-180, width=0, fill="blue")  

    def __drawNameXy(self):
        self.canvas.create_text(self.x+50, self.y-250, fill="black", font="Times 20 italic bold", text ="Георгий")
  
   
   
   
    
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#


    def __drawHead(self):
        self.canvas.create_oval(20, 400, 80, 460, width=2)
        self.canvas.create_arc(30, 420, 70, 450, start=0, extent=-180,
             style=ARC, outline="red", width = 3)
        self.canvas.create_oval(35, 421, 43, 429, width=0, fill="blue")
        self.canvas.create_oval(65, 420, 57, 428, width=0, fill="blue")

    def __drawName(self):
        self.canvas.create_text(50, 380, fill="black", font="Times 20 italic bold", text ="Георгий")
  
  
    def __drawBody(self):
    
        #body
    
        self.canvas.create_line(50, 460, 50, 550, width=2)
        
        
                #armLeft
        
        self.canvas.create_line(50, 490, 100, 430, width=2,)
        
        
                        #armRight
        
        self.canvas.create_line(50, 490, 0, 430, width=2,)
        
        
                        #legLeft
        
        self.canvas.create_line(50, 550, 80, 600, width=2,)
        
        
                        #legRight
        
        self.canvas.create_line(50, 550, 20, 600, width=2,)
        
        
       
