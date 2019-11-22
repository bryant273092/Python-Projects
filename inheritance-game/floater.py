# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    radius = 5
    def __init__(self, x, y):
        Prey.__init__(self, x, y, self.radius*2, self.radius*2, 0, 5)
        self.randomize_angle()   
    def update(self, model):
        if random()*100 <= 30: 
            self.set_speed(max(3,min(7,self.get_speed()+(random()-.5))))
            self.set_angle(self.get_angle()+(random()-.5))
        self.move()
    def display(self, canvas):
        canvas.create_oval(self._x-Floater.radius, self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill='#FF0000')
        
