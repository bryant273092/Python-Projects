# Hunter is derived both from the Mobile_Simulton/Pulsator classes; each updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):
    min_distance = 200
    def __init__(self,x,y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, self.radius*2, self.radius*2, 0, 5)
        self.randomize_angle()
    def update(self, model):
        matched = model.find(lambda s: isinstance(s, Prey) and self.min_distance>=self.distance(s.get_location()))
        Pulsator.update(self, model)
        if matched:
            matched_min = [i for i in sorted(matched, key = lambda i: self.distance(i.get_location()))]
            new_x, new_y = matched_min[0].get_location()
            x, y = self.get_location()
            self.set_angle(atan2( new_y -y, new_x -x))
            print('myangle', self.get_angle())
        self.move()
        return matched 