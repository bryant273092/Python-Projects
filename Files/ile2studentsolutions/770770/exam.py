from goody import type_as_str  # Useful in some exceptions
from _ast import arg

class DictList:
    def __init__(self, *args):
        # each argument is a dict
        if len(args) == 0:  
            raise AssertionError("DictList.__init__: 'abc' is not a dictionary")
        
        for arg in args:
            if type(arg) != dict:
                raise AssertionError("DictList.__init__: 'abc' is not a dictionary")
         
        self.dl = []
        
        for arg in args:
            self.dl.append(arg)
            
        
        
    def __len__(self):
        distinctkeys = set()
        
        for d in self.dl:
            for key in d:
                distinctkeys.add(key)
                
        
        return len(distinctkeys)



    def __repr__(self):
        myrepr = "DictList("
        for d in self.dl:
            myrepr += str(d) + ", "
        
        myrepr = myrepr[:-2]
        myrepr += ")"
        
        return myrepr
    

    def __contains__(self, key):
        for d in self.dl:
            if key in d:
                return True
        
        
        return False
    
    
    
    def __getitem__(self, key):
        
        for d in reversed(self.dl):
            if d.get(key) is not None:
                return d[key]
            
            
        raise KeyError("'" + str(key) + "'" + " appears in no dictionaries")
    
    
    def __setitem__(self, key, value):
        for d in reversed(self.dl):
            if d.get(key) is not None:
                d[key] = value
                return
            
            
        newdict = {}
        newdict[key] = value
        self.dl.append(newdict)
        
        return
            

    
    
    
    def __call__(self, key):
        tuplelist = []
        i = 0
        
        for d in self.dl:
            if d.get(key) is not None:
                tuplelist.append((i, d[key]))
            i += 1
        
    
        return tuplelist
    
    def __iter__(self):
        globalkeys = []
        addedkeys = set()
        
        for d in reversed(self.dl):
            curkeys = []
            for key in d:
                curkeys.append(key)
            
            curkeys.sort()
            
            for key in curkeys:
                if key not in addedkeys:
                    globalkeys.append((key, d[key]))
                
                addedkeys.add(key)
            
        return iter(globalkeys)
      
        
        
    def __eq__(self, right):
        
        if type(right) == DictList:            
            keysleft = set()
            keysright = set()
            
            for d in self.dl:
                for key in d:
                    keysleft.add(key)

                    
                    
            for d in right.dl:
                for key in d:
                    keysright.add(key)
                
                    
            for key in keysleft:
                if key not in keysright:
                    return False
                
                if right[key] != self[key]:
                    return False
                
            for key in keysright:
                if key not in keysleft:
                    return False
                if self[key] != right[key]:
                    return False
            
            
            '''
            if len(self.dl) != len(right.dl):
                return False
            
            for i in range(len(self.dl)):
                for key in self.dl[i]:
                    if key not in right.dl[i]:
                        return False
                for key in right.dl[i]:
                    if key not in self.dl[i]:
                        return False
                    
                for key in self.dl[i]:
                    if self.dl[i][key] != right.dl[i][key]:
                        return False
                    
            '''
        
            return True
        
        
        
        
        if type(right) == dict:
            if len(right) != len(self):
                return False
            
            for key in right:
                if key not in self:
                    return False
                if self[key] != right[key]:
                    return False
            for key in right:
                if key not in self:
                    return False
                if self[key] != right[key]:
                    return False
                
            return True
        
        
        
        
        
        raise TypeError("right must be DictList or dict")
    
    
                    
                
    
    def __add__(self, right):
        if type(right) != DictList and type(right) != dict:
            raise TypeError("right must be DictList or dict")
        
        
        if type(right) == DictList:
            keys1 = set()
            d1 = {}
            for key in self:
                keys1.add(key[0])
            
            
            for key in keys1:
                d1[key] = self[key]
            
            keys2 = set()
            d2 = {}
            for key in right:
                keys2.add(key[0])
                
            
            for key in keys2:
                d2[key] = right[key]
                
            
            newdictlist = DictList(d1, d2)
            
            return newdictlist
        
        
        if type(right) == dict:
            newdictlist = eval(repr(self))
            newdictlist.dl.append(right)
        
            return newdictlist
        
   
    def __ladd__(self, left):
        if type(left) != DictList and type(left) != dict:
            raise TypeError("left must be DictList or dict")
        
        
        if type(left) == DictList:
            keys1 = set()
            d1 = {}
            for key in self:
                keys1.add(key[0])
            
            
            for key in keys1:
                d1[key] = self[key]
            
            keys2 = set()
            d2 = {}
            for key in left:
                keys2.add(key[0])
                
            
            for key in keys2:
                d2[key] = left[key]
                
            
            newdictlist = DictList(d2, d1)
            
            return newdictlist
        
        
        if type(left) == dict:
            newdictlist = eval(repr(self))
            newdictlist.dl.append(left)
        
            return newdictlist
    
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d0 = dict(a=1,b=2,c=3)
    d1 = dict(c=13,d=14,e=15)
    da = DictList(d0)
    db = DictList(d1)
    #print(db + da)
    
    #print(d + d0)
    #print(len(drepr))

    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
