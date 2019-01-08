from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        assert len(args) > 0, "DictList.__init__: {} is not a dictionary ".format(args) 
        for item in args:
            assert isinstance(item, dict), "DictList.__init__: {} is not a dictionary ".format(item) 
        
        self.dl = []
        for item in args:
            self.dl.append(item)
    
    def __len__(self):
        unique = set()
        for dct in self.dl:
            for value in dct:
                unique.add(value)
        return len(unique)
    
    def __repr__(self):
        
        #print('{}'.format(str([x for x in self.dl])))
        return 'DictList({})'.format(str([x for x in self.dl]).strip('[]'))


    def __contains__(self, key):
        for dct in self.dl:
            for ky in dct.keys():
                if key == ky:
                    return True
        return False
        
        
    def __getitem__(self,key):
        
        value = 0
        unique = set()
        
        for dicts in self.dl:
            for k in dicts:
                unique.add(k)
        
        if key not in unique:
            raise KeyError
        
        for dct in self.dl:
            for ky, val in dct.items():
                if key == ky:
                    if val > value:
                        value = val
          
        return value
        
    def __setitem__(self, key, val):
        
        unique = set()
        
        for dicts in self.dl:
            for k in dicts:
                unique.add(k)
                
        if key not in unique:
            self.dl.append({key: val})
        
        for ind in reversed(range(len(self.dl))):
            #print(ind)
            for ky, vl in self.dl[ind].items():
               #print(self.dl[ind])
                #print((key, val), ky, vl)
                if ky == key:
                   #print(self.dl[ind])
                    self.dl[ind][key] = val
                    
                    
                    
            
    def __call__(self, key):
        
        retval = []
        #print(self.dl)
        for ind in range(len(self.dl)):
            #print(ind)
            for ky, val in self.dl[ind].items():
                #print(ky, val)
                if key == ky:
                    retval.append((ind,val))
                    
        return retval
                    
    def __iter__(self):
        unique = set()
        for i in reversed(range(len(self.dl))):
            for key, val in self.dl[i].items():
                if key not in unique:
                    unique.add(key)
                    yield (key, val)
    
    
    def __eq__(self, right):
         
        if isinstance(right, DictList):
            unique_self = set()
            unique_right = set()
            
            for x in self.dl:
                for y in x:
                    unique_self.add(y)
                    
            for i in right.dl:
                for j in i:
                    unique_right.add(j)
                    
            if unique_self != unique_right:
                return False
            
            for a in unique_self:
                if self.__getitem__(a) != right.__getitem__(a):
                    return False
                    
            
                 
        elif isinstance(right, dict):
            unique_self = set()
            unique_right = set()
            
            for x in self.dl:
                for y in x:
                    unique_self.add(y)
                    
            for i in right:
                unique_right.add(i)
                
            if unique_self != unique_right:
                return False
            
            for a in unique_self:
                if self.__getitem__(a) != right.__getitem__(a):
                    return False
        else:
            raise TypeError( 'Operand is neither DictList nor Dict')
        
        return True
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
