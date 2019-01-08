from goody import type_as_str  # Useful in some exceptions

class DictList:

    def __init__(self,*args):
        l = []
        d = dict()
        if len(args) == 0: raise AssertionError
        for x in args:
            if type(x) != dict:   raise AssertionError
            else:
                l.append(x)
                for x,y in x.items():
                    d.update({x:y})
        self.dl = l

    def __len__(self):
        
        d = dict()
        for x in self.dl:
            for y,z in x.items():
                d.update({y:z})
                
        return len(d)
    
    def __repr__(self):
        
        s = ''
        for x in self.dl:
            s += str(x) + ','
        
        return 'DictList(' + s[:-1] + ')'
    
    def __contains__(self,another):

        d = dict()
        
        for x in self.dl:
            for y,z in x.items():
                d.update({y:z})
                
        if another in d: return True
        else: return False
        
    def __getitem__ (self,another):

        d = dict()
        
        for x in self.dl:
            for y,z in x.items():
                d.update({y:z})
                
        if another not in d: raise KeyError
        return d[another]
    
    def __setitem__(self,another,value):

        d = dict()
        
        for x in self.dl:
            for y,z in x.items():
                d.update({y:z})
        
        if another not in d:
            self.dl.append({another:value})
        
        for num in range(len(self.dl)-1,-1,-1):
            if another in self.dl[num]:
                self.dl[num].update({another:value})
                break
    
    def __call__(self,another):

        c = []
        l =[]
        
        for x in self.dl:
            if another in x:
               c.append(x)
        for x in c:
            l.append((self.dl.index(x),x[another]))

        
        return l
    
    def __eq__(self,another):
        
        d = dict()
        for x in self.dl:
            [ d.update({y:z}) for y,z in x.items()]
        
        if type(another) == DictList:
            d2 = dict()
            for x in another.dl:
                [d2.update({y:z}) for y,z in x.items()]
            if d == d2: return True
            else: return False
            
        elif type(another) == dict:
            if d == another: return True
            else: return False

        else: raise TypeError
    
    def __add__(self,another):
 
        d = dict()
        
        for x in self.dl:
            [ d.update({y:z}) for y,z in x.items()]
        
        if type(another) == DictList:
            d2 = dict()
            for x in another.dl:
                [d2.update({y:z}) for y,z in x.items()]
            return DictList(d,d2)
        
        if type(another) == dict: return DictList(d,another)
        else:                     raise TypeError
    

    def __iter__(self):

        d = dict()
        l = []
        c = []
        for num in range(len(self.dl)-1,-1,-1):
            for y,z in (self.dl[num]).items():
                if len(l) == 0: 
                    l .append((y,z))
                    c.append(y)
                else:
                    if y not in c:
                        c.append(y)
                        l.append((y,z))
                    else: pass
            
                
                
        return iter(l)
            
if __name__ == '__main__':


    
    
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
