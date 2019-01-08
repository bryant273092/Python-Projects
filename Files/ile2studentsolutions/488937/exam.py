from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        if len(args) == 0:
            raise AssertionError
        else:
            for i in args:
                if type(i) is not dict:
                    raise AssertionError
                else:
                    self.dl.append(i)
    def __len__(self):
        d = dict()
        for i in self.dl:
            d.update(i)
        return len(d)
    
    def __repr__(self):
        return "DictList{}".format(tuple([i for i in self.dl]))
    
    def __contains__(self,item):
        for i in self.dl:
            if item in i:
                return True
        return False
    
    def __getitem__(self,item):
        d = dict()
        for i in self.dl:
            d.update(i)
        if item not in d:
            raise KeyError("{} not in DictList".format(item))
        
        else:
            return d[item]
        
    def __setitem__(self,item,value):
        d = dict()
        try:
            self[item]
        except:
            d[item] = value
            self.dl.append(d)
        else:
            for i in range(len(self.dl)-1,-1,-1):
                if item in self.dl[i]:
                    self.dl[i][item] = value
                    break
            
    def __call__(self,item):
        l = []
        d = dict()
        for i in self.dl:
            d.update(i)
        if item in d:
            for i in self.dl:
                if item in i:
                    l.append((self.dl.index(i),i[item]))
            return l
        else:
            return []
    
    def __iter__(self):
        d = dict()
        for i in range(len(self.dl)-1,-1,-1):
            for m in sorted(self.dl[i].items(),key = lambda x:x[0]):
                if m[0] not in d:
                    yield(m)
            d.update(self.dl[i])
    
    def __eq__(self,dl):
        if type(dl) is dict:
            
            d = dict()
            for i in self.dl:
                d.update(i)
            return d == dl
                            
        elif type(dl) is DictList:
            d1 = dict()
            d2 = dict()
            for i in self.dl:
                d1.update(i)
            for o in dl.dl:
                d2.update(o)
            return d1 == d2
        
        else:
            raise TypeError("{} is not a dict nor a DictList".format(dl))
        
    def __add__(self,right):
        if type(right) is DictList:
            d1 = dict()
            d2 = dict()
            for a in self.dl:
                d1.update(a)
            for b in right.dl:
                d2.update(b)
            return DictList(d1,d2)
        elif type(right) is dict:
            l = []
            c = self.dl.copy()
            r_c = right.copy()
            for i in c:
                l.append(i)
            l.append(r_c)
            return DictList(*l)
        else:
            raise TypeError()
            
        
    
    def __radd__(self,left):
        if type(left) is DictList:
            d1 = dict()
            d2 = dict()
            for a in self.dl:
                d1.update(a)
            for b in left.dl:
                d2.update(b)
            return DictList(d2,d1)
        elif type(left) is dict:
            l = []
            c = self.dl.copy()
            l_c = left.copy()
            l.append(l_c)
            for i in c:
                l.append(i)
            return DictList(*l)
        else:
            raise TypeError()
            
        
        
           
        
        



            
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
