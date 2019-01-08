from goody import type_as_str  # Useful in some exceptions
from unittest.mock import right

class DictList:
    def __init__(self,*args):
        self.dl = list()
        if len(args) == 0:
            raise AssertionError
        for i in args:
            assert type(i) is dict, 'DicsList.__init__:{} is not a dictionary'.format(i)
            self.dl.append(i)

    def __len__(self):
        L = []
        for i in self.dl:
            for k in i:
                if k not in L:
                    L.append(k)
        return len(L)

    def __repr__(self):
        return 'DictList({})'.format(','.join(str(i) for i in self.dl))      
    
    def __contains__(self,key):
        find = 0
        for i in self.dl:
            for k in i:
                if k == key:
                    find += 1
        return find > 0
    
    def __getitem__(self,key):
        l = []
        for i in self.dl:
            for k in i:
                if k == key:
                    l.append(i[k])
        if l == []:
            raise KeyError
        else:
            return l[-1]
    
    def __setitem__(self,key,value):
        d = {}
        l = []
        a = -1
        for i in self.dl:
            a += 1
            for k in i:
                if k == key:
                    l.append(a)
        if l == []:
            d[key] = value
            self.dl.append(d)
        else:    
            self.dl[l[-1]][key] = value
                    
    def __call__(self,key):
        l = []
        a = -1
        for i in self.dl:
            a += 1
            for k in i:
                if k == key:
                    l.append((a, i[key]))
        return l     
        
    def __iter__(self):
        a = -1
        che = set()
        while a >= -len(self.dl):
            for i in sorted(self.dl[a]):
                if i not in che:
                    che.add(i)
                    yield (i,self.dl[a][i])
            a -= 1        
    def kv(self):
        l = []
        keys = []
        for i in self.dl:
            for key in i:
                if key not in keys:
                    keys.append(key)
        for key in keys:
            value = self.__getitem__(key)
            l.append((key,value))
        return l
            
    def __eq__(self,right):
        if type(right) is DictList:
            l1 = self.kv()
            l2 = right.kv()
            return sorted(l1) == sorted(l2)
        elif type(right) == dict:
            l = []
            for k,v in right.items():
                l.append((k,v))
            l1 = self.kv()
            return sorted(l) == sorted(l1)    
        else:
            raise TypeError  
                        
    def __add__(self,right):
        
        if type(right) is DictList:
            l1 = self.kv()
            l2 = right.kv()
            d = {}
            d1 = {}
            for c,v in l1:
                d[c] = v
            for c,v in l2:
                d[c] = v
            return 'DictList({})'.format(','.join(str(i) for i in [d,d1])) 

        elif type(right) is dict:
            l1 = self.kv()
            d = {c:v for (c,v) in l1}
            d1 = right
            return 'DictList({})'.format(','.join(str(i) for i in [d,d1]))
        
        else:
            raise TypeError
        
    def __radd__(self,left):
        return self.__add__(right)
    
if __name__ == '__main__':
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
