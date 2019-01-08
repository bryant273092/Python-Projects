  
from hunter import Hunter
from random import *
from blackhole import Black_Hole
from math import atan2
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from simulton import Simulton
#this class changes colors every cylce and chases after everything 
class Special(Pulsator, Mobile_Simulton):
    min_distance = 300
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, 20*2, 20*2, 0, 15)
        self.randomize_angle()
    def update(self, model):
        matched = model.find(lambda s: isinstance(s,Simulton ) and type(s) is not Special and self.min_distance>=self.distance(s.get_location()))
        Pulsator.update(self, model)
        if matched:
            matched_min = [i for i in sorted(matched, key = lambda i: self.distance(i.get_location()))]
            new_x, new_y = matched_min[0].get_location()
            x, y = self.get_location()
            self.set_angle(atan2( new_y -y, new_x -x))
            print('myangle', self.get_angle())
        self.move()
        return matched 
    def display(self, canvas):
        canvas.create_oval(self._x-self.get_dimension()[0]/2, self._y-self.get_dimension()[1]/2,
                                self._x+self.get_dimension()[0]/2, self._y+self.get_dimension()[1]/2,
                                fill=self.random_color())
     
    def random_color(self):
        rgbl = ['red','blue','pink','orange','yellow','white','black', 'silver', 'magenta']
        return rgbl[randint(0, len(rgbl)-1)]   

