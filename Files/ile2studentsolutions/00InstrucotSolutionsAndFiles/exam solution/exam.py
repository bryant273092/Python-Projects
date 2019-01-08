from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        assert len(args) > 0, 'DictList.__init__: #args 0: must be >= 1'
        for d in args:
            assert isinstance(d,dict), "DictList.__init__: "+type_as_str(d)+" is not a dictionary"
        self.dl = list(args)
        

    def _all_keys(self):
        return {k for d in self.dl for k in d}
    
    def __len__(self):
        return len(self._all_keys())
    

    def __repr__(self):
        return 'DictList('+', '.join([str(d) for d in self.dl])+')'
    
    
    def __contains__(self,key):
        return any(key in d for d in self.dl)
#             for d in self.dl:
#                 if key in d:
#                     return True
#             return False
    

    def __getitem__(self,item):
        for d in reversed(self.dl):
            if item in d:
                return d[item]
        raise KeyError("DictionaryList.__getitem__: item("+str(item)+") is in no dictionary")
    

    def __setitem__(self,key,value):
        for d in reversed(self.dl):
            if key in d:
                d[key] = value
                return
        self.dl.append({key: value})
    

    def __call__(self,key):
        return [(i,self.dl[i][key]) for i in range(len(self.dl)) if key in self.dl[i]]

  
    def __iter__(self):
        keys_seen = set()
        for d in reversed(self.dl):
            for k,v in sorted(d.items()):
                if k not in keys_seen:
                    keys_seen.add(k)
                    yield k,v
                    
 
    def __eq__(self,right):
        keys_self  = self._all_keys()
        if type(right) is DictList:
            keys_right = self._all_keys()
        elif type(right) is dict:
            keys_right = {k for k in right}
        else:
            raise TypeError('DictList.__eq__: incompatible type for left('+type_as_str(self)+') and right('+type_as_str(right)+')')
        return keys_self == keys_right and all((self[a]==right[a] for a in keys_self))
        

    def __add__(self,right):
        def compress(dl):
            return {k:dl[k] for k in self._all_keys()}
        if type(right) is DictList:
            return DictList(compress(self), compress(right))
        elif type(right) is dict:
            return DictList(*[dict(d) for d in self.dl], dict(right.items()))
        else:
            raise TypeError('DictList.__add__: incompatible type for left('+str(self)+' and right('+str(right)+')')
        
    def __radd__(self,left):
        if type(left) is dict:
            return DictList(dict(left.items()), *[dict(d) for d in self.dl])
        else:
            raise TypeError('DictList.__radd__: incompatible type for left('+str(left)+' and right('+str(self)+')')
        

    
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test

    d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    d2 = DictList(dict(a='one',b='two'), dict(b='twelve',c='thirteen'))
    adict = dict(a='one',b='two')
    print(d1+d2)
    print(d2+d1)
    print(d1+adict)
    print(adict+d1)
    
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
