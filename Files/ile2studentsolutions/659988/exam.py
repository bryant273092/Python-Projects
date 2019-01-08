from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl = []
        assert len(args) > 0, 'DictList.__init__: must specify at least one dictionary'
        for d in args:
            assert type(d) is dict, 'DictList.__init__: '+repr(d)+\
                ' is not a dictionary.'
            self.dl.append(d) 
            
    def __len__(self):
        unique = set() 
        for d in self.dl:
            for k in d.keys():
                unique.add(k)
        return len(unique)
    
    def __repr__(self):
        return 'DictList('+','.join(str(d) for d in self.dl)+')'
    
    def __contains__(self,item):
        for d in self.dl:
            for k in d.keys():
                if k == item:
                    return True 
        return False
    
    def __getitem__(self,item):
        rlist = list(self.dl) 
        rlist.reverse()
        if not item in self:
            raise KeyError()
        for d in rlist:
            if item in d.keys():
                return d[item]
    
    def __setitem__(self,item,value): 
        rlist = list(self.dl) 
        rlist.reverse()
        if item in self:
            for d in rlist:
                if item in d.keys():
                    d[item] = value
                    break
                
        else:
            self.dl.append({item:value})
            
    def __call__(self,item):
        tl = [] 
        i = 0
        for d in self.dl:
            if item in d.keys():
                tl.append((i,d[item]))
            i += 1
        return tl
    
    def __iter__(self):
        def gen(iterable):
            unique = [] 
            for i in iterable:
                for k in sorted(i.keys()):
                    if k not in unique:
                        unique.append(k)
            for i in iterable:
                for u in list(unique):
                    if u in i:
                        yield (u,i[u])
                        unique.remove(u)
        rlist = list(self.dl) 
        rlist.reverse() 
        return gen(rlist)
    
    def __eq__(self,right):
        rlist = list(self.dl) 
        rlist.reverse() 
        if type(right) is DictList:
            if len(self) == len(right):
                for d in rlist:
                    for k in d.keys():
                        if self[k] == right[k]:
                            return True 
                return False
        elif type(right) is dict:
            if len(self) == len(right.keys()):
                for d in rlist:
                    for k in d.keys():
                        if k in right.keys():
                            return d[k] == right[k]
            return False
        else:
            raise TypeError('DictList.__eq__: operand is not a DictList')
        
                    
                    



            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d = DictList(dict(a=1,b=2,c=3),dict(c=13,d=14,e=15),dict(e=25,f=26,g=27))
    print('b' in d)
    print(d['a'])
    print(d['d'])
    print(d['c'])
    print(d['e'])
    #print(d['x'])
    d['c'] = 'new'
    #d['x'] = 'new5'
    print(d)
    print(d('a')) 
    print(d('e')) 
    print(d('x'))
    d1 = DictList(dict(b=2,c=13,d=14,e=25,f=26,g=27))
    d2 = DictList(dict(b=2,c=13,d=15,e=25,f=26,g=27))
    print(d1==d2)
    
    for i in d:
        print(i)
        
    print(d1 == dict(a=1,c=13))
    print(d1 == dict(a=1,b=2,c=13))
    


    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
#    driver.driver()
