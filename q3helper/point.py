#Submitter: bryanth1(Hernandez, Bryant)
import prompt,re
import math
from goody import type_as_str

class Point:
    def __init__(self, x: int, y: int, z: int):
        assert type(x) == int, str('Class name: ' + '__init__' + ' arguments must be of int type. Invalid argument: ' +str(x)+ ' of type: ' +str(type(x))) 
        assert type(y) == int, str('Class name: ' + '__init__' + ' arguments must be of int type. Invalid argument: ' +str(y)+ ' of type: ' +str(type(y))) 
        assert type(z) == int, str('Class name: ' + '__init__' + ' arguments must be of int type. Invalid argument: ' +str(z)+ ' of type: ' +str(type(z))) 
        self.x = x
        self.y = y
        self.z = z
        self.coords = [x, y, z]
        self.dict1 = {'x':x,'y':y, 'z':z}
             
    def __repr__(self)->str:
        return 'Point'  + '(' + str(self.x)+','+ str(self.y)+ ',' + str(self.z)+')'
    def __str__(self)->str:
        return str('('+ 'x=' + str(self.x) + ',y=' + str(self.y) + ',z=' + str(self.z) + ')')
    def __bool__(self)->bool:
        if self.x == 0 and self.y== 0 and self.z == 0: return False
        return True
    def __add__(self, point2)->object:
        if type(point2) is not Point:
            raise TypeError('illegal arguments made during concatenation between'+str(Point)+ 'and' +str(type(point2)))    
        
        return Point(self.x+point2.x,self.y + point2.y,self.z + point2.z)
        
    def __mul__(self,point2)->object: 
        if type(point2) not in (Point, int):
            raise TypeError('illegal arguments made during multiplication between'+str(Point)+ 'and' +str(type(point2)))
        elif type(point2) is Point:
            raise TypeError('illegal arguments made during multiplication between'+str(Point)+ 'and' +str(type(point2)))
        else: 
            return Point(self.x*point2, self.y*point2, self.z*point2)
    def __rmul__(self,point2)->object:
        if type(point2) not in (Point, int):
            raise TypeError('illegal arguments made during multiplication between'+str(Point)+ 'and' +str(type(point2)))
        elif type(point2) is Point:
            raise TypeError('illegal arguments made during multiplication between'+str(Point)+ 'and' +str(type(point2)))
        else: 
            return Point(self.x*point2, self.y*point2, self.z*point2)   
    
    def distance(self)->int: 
        return math.sqrt(sum(x**2 for x in self.coords))
    
    def __lt__(self, r_s)->object:
        if type(r_s) not in (Point, int, float):
            raise TypeError('illegal arguments made during comparison between'+str(Point)+ 'and' +str(type(r_s)))
        elif type(r_s) is Point:
            return self.distance() < r_s.distance()
        else:
            if self.x<r_s and self.y<r_s and self.z<r_s:
                return True
            else:
                return False
    def __getitem__(self, index1):
        if type(index1) not in (str, int):
            raise IndexError('illegal arguments made during index between'+str(Point)+ 'and' +str(type(index1)))
        elif type(index1) is str:
            try: 
                return self.dict1[index1]
            except:
                raise IndexError
        elif type(index1) is int:
            if index1 >= 0:
                return self.coords[index1]
            else: 
                raise IndexError
            
    def __call__(self, x, y, z):
        if type(x) is not int or type(y) is not int or type(z) is not int:
            raise AssertionError('arguments must be of int class when calling object')
        self.x = x
        self.y = y
        self.z = z
        
if __name__ == '__main__':
    #Smple tests before running driver
    #Put your own test code here to test Point before doing bsc tests
    print('Start simple testing')
    import driver
    
    
    driver.default_file_name = 'bscq31F18.txt'
#     driver.default_show_traceback = True3
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
