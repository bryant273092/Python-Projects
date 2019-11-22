# Black_Hole is derived from the Simulton: each updates by finding and removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, self.radius*2, self.radius*2)
    def update(self, model):
        matched = model.find(lambda s: isinstance(s, Prey) and self.contains(s.get_location()))
        for i in matched:
            model.remove(i)
        return matched 
            
    def display(self, canvas):
        
        canvas.create_oval(self._x-self.get_dimension()[0]/2, self._y-self.get_dimension()[1]/2,
                                self._x+self.get_dimension()[0]/2, self._y+self.get_dimension()[1]/2,
                                fill='#000000')
        
    def contains(self, xy):
        return self.distance(xy) <= self.radius
        
        
