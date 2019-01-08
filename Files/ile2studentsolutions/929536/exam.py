from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*dicts):
        self.dl=[]
        assert len(dicts)>0,"there are no dictionaries in the argument"
        for d in dicts:
            assert isinstance(d, dict),f"Dict.__init__: {dict} is not a dictionary"
            self.dl.append(d)
    
    def __len__(self):
        l=[]
        for d in self.dl:
            for i in d.keys():
                if i not in l:
                    l.append(i)
        return len(l)
    
    def keys(self):
        a=set()
        for each in self.dl:
            for k in each:
                a.add(k)
        return a
        
    
    def __repr__(self):
        return f'DictList(*{self.dl})'
    
    def __contains__(self,*args):
        for each in self.dl:
            if args[0] in each.keys():
                return True
        return False
    
    def __getitem__(self,item):
        if item in self:
            a=0
            for each in self.dl:
                if item in each:
                    a=each[item]
            return a
        else:
            raise KeyError(f'{item} appears in no dictionaries')


    def __setitem__(self,item,value):
        if item in self:
            v=self.__getitem__(item)
            self.dl.reverse()
            l=self.dl.copy()
            self.dl.reverse()
            for d in l:
                if item in d and d[item]==v:
                    self.dl[self.dl.index(d)][item]=value
                    break
        else:
            self.dl.append({item:value})
            
    def __call__(self,key):
        if key in self:
            r=[]
            for index,each in enumerate(self.dl):
                if key in each:
                    r.append((index,each[key]))
            return r
                
        else:
            return []

    def __iter__(self):
        self.dl.reverse()
        l=self.dl.copy()
        self.dl.reverse()
        
        used=[]
        
        for d in l:
            for key in sorted(d.keys()):
                if key not in used:
                    used.append(key)
                    yield (key,d[key])
        return 
            
    def __eq__(self,right):
        if isinstance(right, DictList):
            if self.keys()==right.keys():
                return all(self.__getitem__(key)==right.__getitem__(key) for key in self.keys())    
            return False
        elif isinstance(right, dict):
            return all(key in right and self.__getitem__(key)==right[key] for key in self.keys())
        else:
            raise TypeError('Can only compare DickList or Dict')
            
        
    def __add__(self,right):
        if isinstance(right,DictList):
            d1={key:self.__getitem__(key) for key in self.keys()}
            d2={key:right.__getitem__(key) for key in right.keys()}
            return DictList(d1,d2)
        elif isinstance(right, dict):
            l=[d for d in self.dl]+[dict(right)]
            return DictList(*l)
        else:
            raise TypeError('Can only add DictList or Dict')
        
        
    
    
    def __radd__(self,left):
        if isinstance(left,DictList):
            return self+left
        elif isinstance(left, dict):
            l=[left]+self.dl
            return DictList(*l)
        else:
            raise TypeError('Can only add DictList or Dict')































            
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
