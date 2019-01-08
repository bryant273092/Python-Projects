from goody import type_as_str  # Useful in some exceptions
from builtins import AssertionError

class DictList:
    def __init__(self,*args):
        self.dl = []
        for arg in args:
            if type(arg) == dict:   
                if type(arg.items()) == dict: 
                    for a in arg:
                        if type(a) == dict:
                            self.dl.append(a)
                        else:
                            raise AssertionError
                else:
                    self.dl.append(arg)
                        
            else:
                raise AssertionError
            
    def __len__(self):
        count = 0
        li = []
        for a in self.dl:
            if type(a) == str:
                if a not in li:
                    count += 1
                    li.append(a)
            else:
                for b in a:
                    if type(b) == str:
                        if b not in li:
                            count += 1
                            li.append(b)
        return count
            
    def __repr__(self):
        return "Dictlist(" + str(self.dl) + ")"  

    
    def __contains__(self,data):
        for a in self.dl:
            if type(a) == str:
                if a == data:
                    return True
            else:
                for b in a:
                    if b == data:
                        return True
                
    def __getitem__(self,data):
        result = []
        for a in self.dl:
            if type(a) == str:
                if a == data:
                    return self.dl[data]
                elif data not in self.dl:
                    raise KeyError
            elif type(a) == dict:
                for b in a:
                    if b == data:
                        result.append(a[data])    
            else:
                raise KeyError
        return result[-1]

    def __setitem(self,data,new):
        for a in self.dl:
            if type(a) == str:
                if a == data:
                    self.dl[data] = new
            elif type(a) == dict:
                for b in a:
                    if b == data:
                        a[data] = new
    

    
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test


    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True

    driver.driver()
