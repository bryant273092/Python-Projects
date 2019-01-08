#Submitter: bryanth1(Hernandez, Bryant)
import inspect

class C:
    def __init__(self):
        self.a = 1
        self.b = 2
        
    def add_more_attributes(self): 
        self.c = 3  
         
    def bad_add_more_attributes(self):
        self.private_d = 4 # should raise exception
         
    def bump(self):
        self.a += 1
        self.b += 1
        self.c += 1
        
    def __str__(self):
        return 'a='+str(self.a)+',b='+str(self.b)+',c='+str(self.c)+',d='+str(self.d)

    @staticmethod
    def in_C(calling):
        if calling.function not in C.__dict__:
            return False
        return calling.frame.f_code is C.__dict__[calling.function].__code__
       
    def __setattr__(self,name,value):
        print(self.__dict__)
        calling = inspect.stack()[1]
        print(calling.function)
        if name[0:7] == 'private':
            raise NameError
        elif calling.function == '__init__': 
            name = 'private_'+ str(name)
            self.__dict__[name] = value
            print(self.__dict__)
        elif 'private_' + str(name) in self.__dict__:
            name = 'private_' + str(name)
            self.__dict__[name]= value
        else:
            self.__dict__[name] = value
        
        
        # write remaining code


    def __getattr__(self,name):
        calling = inspect.stack()[1]
        if calling.function != '<module>' and 'private_' + str(name) in self.__dict__:
            name = 'private_' + str(name)
            return(self.__dict__[name])
        else:
            raise NameError
            
        # write remaining code
    
def  f(o):
    return o.a    
        
def  __init__(o):  # Don't confuse this with the __init__ method defined in C
    o.z = 'z'    
        
if __name__ == '__main__':
    # These are all the bsc tests that don't raise exceptions.
    o = C()
    print(o.__dict__)
    
    o.add_more_attributes()
    o.d = 5
    print(o.__dict__)
    
    o.bump()
    print(o.__dict__)
    
    print(o.c,o.d)
    
    __init__(o)
    print(o.__dict__)
    
    print()
    import driver
    
    driver.default_file_name = 'bscq32F18.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()


# The driver prints the following information
# {'private_a': 1, 'private_b': 2}
# {'private_a': 1, 'private_b': 2, 'c': 3, 'd': 5}
# {'private_a': 2, 'private_b': 3, 'c': 4, 'd': 5}
# 4 5
# {'private_a': 2, 'private_b': 3, 'c': 4, 'd': 5, 'z': 'z'}