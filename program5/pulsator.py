# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    counter1 = 30 
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self.counter2 = 0
         
    def update(self, model):
        self.counter2 +=1
        matched = Black_Hole.update(self, model)
        if not matched: 
            if self.counter2 == self.counter1:
                self.change_dimension(-1, -1)
                if self.get_dimension()[0] == 0 or self.get_dimension()[1]==0:
                    model.remove(self)
                self.counter2 = 0
        else: 
            for i in matched:
                self.change_dimension(1, 1)
            self.counter2 = 0
        return matched
