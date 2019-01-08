import controller, sys
import model   # Pass a reference to this module to each update call in update_all

#Use the reference to this module to pass it to update methods

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running           = False
cycle_count        = 0
prey             = set()
select_object_str = ''


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, prey, select_object_str
    running           = False
    cycle_count       = 0
    prey             = set()
    select_object_str = ''


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#tep just one update in the simulation
def step ():
    global cycle_count
    global running
    if not running:
        running = True
    cycle_count += 1
    for p in prey:
        p.update(model)
    running = False 
        
        
        


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global select_object_str
    select_object_str = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    
    if select_object_str == 'Remove':
        for obj in {i for i in prey}:
            if obj.contains((x,y)):
                prey.remove(obj)
    elif select_object_str:
        prey.add(eval(select_object_str+'(x,y)'.format(x = x, y = y)))       


#add simulton s to the simulation
def add(s):
    global prey
    print('adding this', s)
    prey.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global prey
    prey.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    findings = set()
    for simulton in prey:
        if p(simulton):
            findings.add(simulton)
    return findings 
    


#call update for each simulton in the simulation (pass the model as an argument)
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        for p in {s for s in prey}:
            p.update(model)


#delete from the canvas every simulton being simulated; next call display on every
#  simulton being simulated to add it back to the canvas, possibly in a new location, to
#  animate it; also, update the progress label defined in the controller
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    print(prey)
    for p in prey:
        p.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(cycle_count)+'cycles/'+str(len(prey))+'simultons')
