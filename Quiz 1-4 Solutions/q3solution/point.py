import prompt,re
import math
from goody import type_as_str

class Point:
    
    def __init__(self,x,y,z):
        assert type(x) is int and type(y) is int and type(z) is int,'Point.__init__ parameters must be of type int'
        self.x, self.y, self.z = x, y, z
#         assert type(x) is int,'Point.__init__: x('+str(x)+') is not an int('+type_as_str(x)+')'
#         assert type(y) is int,'Point.__init__: y('+str(y)+') is not an int('+type_as_str(y)+')'
#         assert type(z) is int,'Point.__init__: z('+str(z)+') is not an int('+type_as_str(z)+')'
#         self.x, self.y, self.z = x, y, z
        
    def __repr__(self):
        return 'Point'+'('+str(self.x)+','+str(self.y)+','+str(self.z)+')'
#         return 'Point('+str(self.x)+','+str(self.y)+','+str(self.z)+')'

    def __str__(self):
        return '(x='+str(self.x)+',y='+str(self.y)+',z='+str(self.z)+')'
#         return '(x='+str(self.x)+',y='+str(self.y)+',z='+str(self.z)+')'
    
    def __bool__(self):
        return  not (self.x,self.y,self.z) == (0,0,0)
  #       return self.x != 0 or self.y != 0 or self.z != 0
        
    def __add__(self,right):
        if type(right) is not Point:
            raise TypeError
        else:
            return Point(self.x+right.x, self.y + right.y, self.z + right.z)
#         if type(right) is Point:
#             return Point(self.x+right.x,self.y+right.y,self.z+right.z)
#         else:
#             raise TypeError('Point.__add__: right('+str(right)+') not Point('+type_as_str(right)+')')

    def __mul__(self,right):
        if type(right) is not int:
            raise TypeError
        else:
                
            return Point(self.x*right, self.y * right, self.z * right)
#         if type(right) is int:
#             return Point(self.x*right,self.y*right,self.z*right)
#         else:
#             raise TypeError('Point.__mul__: right('+str(right)+') not Point('+type_as_str(right)+')')

    def __rmul__(self,left):
        if type(left) is not int:
            raise TypeError
        else:
                
            return Point(self.x*left, self.y * left, self.z * left)
#         if type(left) is int:
#             return Point(left*self.x,left*self.y,left*self.z)
#             # return self*left # works by commutivity 
#         else:
#             raise TypeError('Point.__rmul__: left('+str(left)+') not int('+type_as_str(left)+')')

    def __lt__(self,right):
        if type(right) not in [Point,int]:
            raise TypeError
        elif type(right) is Point:
            return math.sqrt(self.x**2+self.y**2+self.z**2)< math.sqrt(right.x**2+right.y**2+right.z**2)
        elif type(right) in [int,float]:
            return math.sqrt(self.x**2+self.y**2+self.z**2)< right
            
#         if type(right) is Point:
#             return math.sqrt(self.x**2 + self.y**2 + self.z**2) < math.sqrt(right.x**2+right.y**2+right.z**2)
#         if type(right) is int or type(right) is float:
#             return math.sqrt(self.x**2 + self.y**2 + self.z**2) < right
#         else:
#             raise TypeError('Point.__lt__: right('+str(right)+') int or float('+type_as_str(right)+')')

    def __getitem__(self,index):
        if type(index) not in [int,str]:
            raise IndexError('Point.__getitem__: index('+str(index)+') must be str or int('+type_as_str(index)+')')
        if type(index) is str: 
            if index in ['x','y','z']: 
                return self.__dict__[index]
            else:
                raise IndexError('Point.__getitem__: index('+str(index)+') must be x or y or z)')
        if type(index) is int: 
            if 0<=index<=2 :
                return self.x if index==0 else self.y if index==1 else self.z
            else:
                 raise IndexError('Point.__getitem__: index('+str(index)+') must be 0 or 2')
        
    def __call__(self,x,y,z):
        assert type(x) is int,'Point.__call__: x('+str(x)+') is not an int('+type_as_str(x)+')'
        assert type(y) is int,'Point.__call__: y('+str(y)+') is not an int('+type_as_str(y)+')'
        assert type(z) is int,'Point.__call__: z('+str(z)+') is not an int('+type_as_str(z)+')'
        self.x, self.y, self.z = x, y, z
        

if __name__ == '__main__':
    #Simple tests before running driver
    #Put your own test code here to test Point before doing bsc tests
    
    print()
    import driver
    
    driver.default_file_name = 'bscq31F18.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
