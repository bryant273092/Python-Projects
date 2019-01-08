from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args): # DONE
        assert len(args)>0,"You must supply at least one argument"
        self.dl = []
        for a in args:
            assert type(a) is dict,"DictList.__init__:{} is not a dictionary".format(str(a))
            self.dl.append(a)
    
    def __len__(self): # DONE
        len_set = set()
        for a in self.dl:
            for k in a.keys():
                len_set.add(k)
        return len(len_set)
    
    def __repr__(self): # DONE
        return "DictList("+", ".join(str(a) for a in self.dl)+")"
    
    def __contains__(self,item): # DONE
        for a in self.dl:
            for k in a.keys():
                if k == item:
                    return True
        return False

    def __getitem__(self, item): # DONE
        for a in self.dl[::-1]:
            for k in a.keys():
                if k == item:
                    return a[k]
        raise KeyError("{} appears in no dictionaries".format(item))

    def __setitem__(self, nkey, nvalue): # DONE
        for a in self.dl[::-1]:
            for k in a.keys():
                if k == nkey:
                    a[k] = nvalue
                    return
        self.dl.append({nkey : nvalue})
        
    def __call__(self, item): # DONE
        call_list = []
        for a in range(len(self.dl)):
            for k in self.dl[a].keys():
                if k == item:
                    call_list.append((a, self.dl[a][k]))
        return call_list
    
    def __iter__(self): # DONe
        used = set()
        for a in self.dl[::-1]:
            for k in sorted(a.keys(), key = lambda x:x[0]):
                if k in used:
                    pass
                else:
                    used.add(k)
                    yield (k,a[k])
                    
    def __eq__(self, other): # DONe
        if isinstance(other, DictList) or type(other) is dict:
            unique = set()
            for a in self.dl:
                for k in a.keys():
                    unique.add(k)
            if type(other) is dict:
                other_keys = {a for a in other.keys()}
                for x in unique:
                    if x in other_keys:
                        if self[x] == other[x]:
                            other_keys.remove(x)
                    else:
                        return False                       
            else:
                other_keys = set()
                for a in other.dl:
                    for k in a.keys():
                        other_keys.add(k)
                for x in unique:
                    if self[x] == other[x]:
                        other_keys.remove(x)
                    else:
                        return False
        else:
            raise TypeError("Right operand must be a dict or DictList was:{}".format(type_as_str(other)))
        
        if len(other_keys) !=0:
            return False
        else:
            return True
        
    def __add__(self,other):
        new = dict()
        new2 = dict()
        if (not isinstance(other, DictList)) or type(other) is dict:
            raise TypeError("{} must be a DictList or dict".format(str(other)))
        if type(other) is dict and isinstance(self, DictList):
            for a in self.dl:
                for k,v in a.items():
                    new[k] = v
            return DictList(new, copy(other))
        elif isinstance(other, DictList) and type(self) is dict:
            for a in other.dl:
                for k,v in a.items():
                    new2[k] = v
            return DictList(copy(self), new2)
        else:
            for a in self.dl:
                for k,v in a.items():
                    new[k] = v
            for a in other.dl:
                for k,v in a.items():
                    new2[k] = v
            return DictList(new, new2)
       
       
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d = DictList(dict(a=1,b=2,c=3),dict(d=4,e=5,f=6),dict(f=9,h=5))
    #d2 = DictList() AssertionError
    
    print("len(d):",len(d))
    
    print("repr(d):",repr(d))
    
    print("a in d", ('a' in d))
    print("z in d", 'z' in d)
    
    print("d[f]:",d['f'])
    #print("d[k]:", d['k']) Key Error
    
    d['a'] = 2
    d['f'] = 1111 # changes highest index
    d['y'] = 50 # adds new dict
    print(repr(d))
    
    print("d('f'):", d('f')) # should return 2 tuples
    print("d('k'):",d('k')) # returns empty list
    
    #print(iter(d)) # kinda works
    
    #print(d==[]) TypeError
    print(d == dict(a=2,b=2,c=3,d=4,e=5,f=9,h=5))
    print(d == dict(a=2,b=2,c=2))
    print(d==d)
    d3 = d
    d3['l'] = 9
    print(d==d3)
    
    
    

    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
