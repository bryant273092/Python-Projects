from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self,*dicts):
        self.dl=[]
        if not dicts:
            raise AssertionError ('DictList.__init__:'+str(dicts)+'is not a dictionary')
        for d in dicts:
            if type(d) is not dict:
                raise AssertionError ('DictList.__init__:'+str(d)+'is not a dictionary')
            else:
                self.dl.append(d)
    
    def __len__(self):
        dkeys=set()
        for d in self.dl:
            for key in d.keys():
                dkeys.add(key)
        return len(dkeys)
    
    def __repr__(self):
        #print( 'DictList('+', '.join(str(d) for d in self.dl)+')' )
        return 'DictList('+', '.join(str(d) for d in self.dl)+')'
    
    def __contains__(self,key):
        for d in self.dl:
            if key in d.keys():
                return True
        return False  
    
    def __getitem__(self,key):
        if key not in self:
            raise KeyError 
        anwser=[]
        for d in self.dl:
            if key in d:
                anwser.append(d[key])
            else:
                pass
        return anwser[-1]
    
    def __setitem__(self,key,value):
        if key in self:
            n=[]
            for d in self.dl:
                if key in d:
                    n.append(self.dl.index(d))
            self.dl[n[-1]][key]=value
        else:
            newd=dict()
            newd[key]=value
            self.dl.append(newd)
                     
    def __call__(self,key):
        result=[]
        if key in self:
            for d in self.dl:
                if key in d:
                    result.append((self.dl.index(d),d[key])) 
        return sorted(result)
    
    def __iter__(self):
        produced=set()
        l=len(self.dl)
        for i in reversed(range(l)):
            for k,v in self.dl[i].items():
                if k not in produced:
                    produced.add(k)
                    yield (k,v)
        
    def __eq__(self,right):
        def _get_keys(dl:[dict]):
            result=set()
            for d in dl:
                for key in d.keys():
                    result.add(key)
            return result
            
        if type(right)==DictList:
            return _get_keys(self.dl)==_get_keys(right.dl) and all(self[i]==right[i] for i in _get_keys(self.dl))
        elif type(right)==dict:
            return _get_keys(self.dl)==set(right.keys()) and all(self[i]==right[i] for i in _get_keys(self.dl))
        else:
            raise TypeError
        
    def get_items(self,dl:[dict]):
            result=dict()
            for d in dl:
                for k,v in d.items():
                    result[k]=v
            return result 
    
    def __add__(self,right):
        if type(right)==DictList:
            return DictList(self.get_items(self.dl),self.get_items(right.dl))
        elif type(right)==dict:
            return DictList(self.get_items(self.dl),right)
        else:
            raise TypeError
        
    
    def __radd__(self,left):
        if type(left)==DictList:
            return DictList(self.get_items(left.dl),self.get_items(self.dl)) 
        elif type(left)==dict:
            return DictList(left,self.get_items(self.dl))
        else:
            raise TypeError
            




            
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
