from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl = list()
        
        try:
            l = len(args)
        except:
            raise AssertionError
        
        if l == 0:
            raise AssertionError
        else:
            for d in args:
                if not type(d) is dict:
                    raise AssertionError
                self.dl.append(d)

    def __len__(self):
        d_key = set()
        
        for d in self.dl:
            for k in d.keys():
                d_key.add(k)
                
        return len(d_key)
    
    def __repr__(self):
        s = "DictList("
        for d in self.dl:
            s += str(d)
            s += ", "
        
        s = s[:-2] + ")"
        
        return s
    
    def __contains__(self,key):
        for d in self.dl:
            for k in d.keys():
                if key == k:
                    return True
        
        return False
            
    def __getitem__(self,key):
        if not key in self:
            raise KeyError
        
        unique_d = dict()
        
        for d in self.dl:
            for k,v in d.items():
                unique_d[k] = v
                
        return unique_d[key]
    
    def __setitem__(self,key,value):
        if not key in self:
            self.dl.append({key:value})
            return
        
        self.dl.reverse()
        
        for d in self.dl:
            if key in d.keys():
                d[key] = value
                self.dl.reverse()
                return
            
    def __call__(self,key):
        if not key in self:
            return list()
        
        l = list()
        counter = 0
        
        for d in self.dl:
            if key in d.keys():
                l.append((counter,d[key]))
            counter += 1
                
        return l
    
    def __iter__(self):
        def contain(l,k):
            for i in l:
                if i[0] == k:
                    return True
                
            return False
        
        l = list()
        
        for d in reversed(self.dl):
            for k,v in d.items():
                if not contain(l,k):
                    l.append((k,v))

        i = iter(l)
        Stop = False
        
        while not Stop:
            try:
                v = next(i)
            except StopIteration:
                Stop = True
            
            if not Stop:
                yield v
                
    def __eq__(self,other):
        if type(other) is dict or type(other) is type(self):
            pass
        else:
            raise TypeError
        
        d_key = set()
        
        for d in self.dl:
            for k in d.keys():
                d_key.add(k)
        
        if type(other) == type(self):                           
            other_key = set()
            
            for d in other.dl:
                for k in d.keys():
                    other_key.add(k)
        else:
            other_key = set(other.keys())
                
        if d_key == other_key:
            for k in d_key:
                if self[k] != other[k]:
                    return False
                
            return True
        else:
            return False

    def __add__(self,RHS):
        if type(RHS) is dict or type(RHS) is type(self):
            pass
        else:
            raise TypeError
        
        d_self = dict([i for i in self])
        if type(RHS) is type(self):
            d_RHS = dict([i for i in RHS])
        else:
            d_RHS = dict(RHS)
        
        return DictList(d_self,d_RHS)
    
    def __radd__(self,LHS):
        if type(LHS) is dict or type(LHS) is type(self):
            pass
        else:
            raise TypeError
        
        d_self = dict([i for i in self])
        if type(LHS) is type(self):
            d_LHS = dict([i for i in LHS])
        else:
            d_LHS = dict(LHS)
        
        return DictList(d_LHS,d_self)
             
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d1 = dict(c=13,d=14,e=15)
    d0 = dict(a=1,b=2,c=3)
    d2 = dict(e=25,f=26,g=27)
    d  = DictList(d0,d1)
    produced = [i for i in d]
    print(produced)

    d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    d2 = DictList(dict(a='one',b='two'), dict(b='twelve',c='thirteen'))
    adict = dict(a='one',b='two')
    d = d1+adict
    print(d)
    d1['b'] = 'x'
    print(d['b'])
    adict['b'] = 'x'
    print(d['b'])


    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
