from goody import type_as_str  # Useful in some exceptions
from _operator import itemgetter

class DictList:
    def __init__(self, *args):
        self.dl = []
        
        
        for n in args:  
            assert  isinstance(n,dict), 'DictList.__init__: ' + str(n) + ' is not a dictionary.'
        assert len(args) > 0, 'DictList.__init__: must have 1 or more arguments'
        
        for d in args:
            self.dl.append(d)
            
       
            
    

    def __len__(self):
            
        total = []
        for dict in self.dl:
            for k in dict:   
                if k not in total:
                    total.append(k)
            
        return len(total)
    
    def __repr__(self):
        
        return 'DictList(' + ','.join(str(n) for n in self.dl) + ')'

    
    
    def __contains__(self, item):
        
        for d in self.dl:
            if item in d:
                return True
        
        return False
        
        
    def __getitem__(self, item):
        
        
        for x in self.dl[-1::-1]:
            
            
            if item in x:
                return x[item]
            
        raise KeyError('DictList.__getitem__: ' + str(item) + ' is not in the DictList')
    
    def __setitem__(self, item, value):
        
        check = True
        for x in range(len(self.dl) -1 , -1, -1):
            if check and item in self.dl[x]:
                check = False
                self.dl[x][item] = value
                
        if check:
            self.dl.append({item: value})
    
    
    def __call__(self, item):
        
        final = []
        for x in range(len(self.dl)):
            
            if item in self.dl[x]:
                final.append((x, self.dl[x][item]))
                
        return final
            
        
    def __iter__(self):
        
        check = []
        for i in range(len(self.dl)-1, -1, -1):
            
            for k in sorted(self.dl[i]):
                
                if k not in check:
                    check.append(k)
                    yield ((k, self.dl[i][k]))
                
        
        
    
    
    def __eq__(self, other):
        
        if isinstance(other, DictList):
            
            for d in  self.dl:
                for k in d:
                    try:
                        
                        if other[k] != self[k]:
                            return False
                    
                    except KeyError:
                        return False
                
            return True
                
            
        elif isinstance(other, dict):
            
            
            for d in self.dl:
                
                for k in d:
                    
                    if k not in other:
                        return False
                        
                    if self[k] != other[k]:
                        return False
                    
            return True
        else:
            
            raise TypeError('DictList.__eq__: ' + str(other) + ' is type ' + '(' + type_as_str(other) + ')' + ' and must be type DictList or dict')
    
    
    
    def __add__(self, other):
        if isinstance(other, DictList):
            f = {}
            s = {}
            for d in self.dl:
                for k in d:
                    f[k] = self[k]
            
            for d in other.dl:
                for k in d:
                    s[k] = other[k]
            
            return DictList(f,s)
                
                
            
        elif isinstance(other, dict):
            
            
            return self + DictList(other)
        else:
            
            raise TypeError('DictList.__add__: ' + str(other) + ' is type ' + '(' + type_as_str(other) + ')' + ' and must be type DictList or dict')
    
        
    
    def __radd__(self, other):
        
        if isinstance(other, DictList):
            f = {}
            s = {}
            for d in self.dl:
                for k in d:
                    f[k] = self[k]
            
            for d in other.dl:
                for k in d:
                    s[k] = other[k]
            
            return DictList(s,f)
                
                
            
        elif isinstance(other, dict):
            
            
            return DictList(other) + self
        else:
            
            raise TypeError('DictList.__add__: ' + str(other) + ' is type ' + '(' + type_as_str(other) + ')' + ' and must be type DictList or dict')
    
        
        
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    
    
    d = DictList({'a':1}, {'a': 3, 'c': 4}, {'f': 0, 'p': 9})
    x = DictList({'b':2}, {'a': 3, 'c': 4},{'a': 4}, {'b': 5})
    
    c = {'a': 2, 'f': 90}
    print(c + x + d)
    
    
    for x in d:
        print(x)
    #print(d['a'])
   
        
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
    driver.default_show_exception=True
    driver.default_show_exception_message=True
    driver.default_show_traceback=True
    driver.driver()
