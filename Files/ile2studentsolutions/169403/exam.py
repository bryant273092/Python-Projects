from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *dicts):
        assert len(dicts) != 0, 'DictList.__init__: must have at least one dictionary argument'
        self.dl = []
        for d in dicts:
            assert type(d) is dict, f'DictList.__init__: {d} is not a dictionary'
            self.dl.append(d)
    
    def keys(self):
        keys = set()
        for d in self.dl:
            for k in d:
                keys.add(k)
        return keys
           
    def __len__(self):
        return len(self.keys())
    
    def __repr__(self):
        return 'DictList(' + ','.join(str(d) for d in self.dl) + ')'
    
    def __contains__(self, key):
        for d in self.dl:
            if key in d:
                return True
        return False
    
    def __getitem__(self, key):
        if key not in self:
            raise KeyError(f'DictList.__getitem__: key \'{key}\' not found in any dictionary')
        for d in self.dl[::-1]:
            if key in d:
                return d[key]
    
    def __setitem__(self, key, value):
        if key in self:
            for d in self.dl[::-1]:
                if key in d:
                    d[key] = value
                    break
        else:
            self.dl.append({key:value})
        
    def __call__(self, key):
        result = []
        for i in range(len(self.dl)):
            if key in self.dl[i]:
                result.append((i,self.dl[i][key]))
        return result
        
    def __iter__(self):
        def gen():
            produced_key = set()
            for d in self.dl[::-1]:
                for k,v in sorted(d.items()):
                    if k not in produced_key:
                        produced_key.add(k)
                        yield (k,v)
        return gen()
                
    def __eq__(self, operand):
        if type(operand) not in (DictList, dict):
            raise TypeError(f'DictList.__eq__: invaild type: {operand} is {type_as_str(operand)}, should be DictList or dict')
        if self.keys() != operand.keys():
            return False
        for k,v in self:
            if k not in operand or operand[k] != v:
                return False
        return True
    
    def __add__(self, operand):
        if type(operand) not in (DictList, dict):
            raise TypeError(f'DictList.__add__: unsupported operand type(s) for +: DictList and {type_as_str(operand)}')
        if type(operand) is DictList:
            return DictList(dict([(x,self[x]) for x in self.keys()]), dict([(x,operand[x]) for x in operand.keys()]))
        elif type(operand) is dict:
            return DictList(*[dict(d) for d in self.dl], dict(operand))
    
    def __radd__(self, operand):
        if type(operand) is not dict:
            raise TypeError(f'DictList.__radd__: unsupported operand type(s) for +: {type_as_str(operand)} and DictList')
        return DictList(dict(operand), *[dict(d) for d in self.dl])
                
            

            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    x = DictList({'a':1},{'a':2,'b':3})
    print(x)
    assert 'b' in x
    assert 'x' not in x
    assert x['a'] == 2
    x['a'] = 2.5
    x['c'] = 4
    assert len(x) == 3
    print(x)
    assert x('a') == [(0,1),(1,2.5)]
    for i in x:
        print(i,end = '')
    assert x == DictList({'c':4},{'a':2.5, 'b':3})
    assert x != {'c':4,'a':2.5, 'd':5, 'b':3} 
    assert x + DictList({1:1}) == DictList({'a':2.5,'b':3,'c':4}, {1:1})
    assert x + {'d':5} == DictList({'a':1},{'a':2.5,'b':3},{'c':4},{'d':5})
    assert {'d':5} + x == DictList({'d':5},{'a':1},{'a':2.5,'b':3},{'c':4})       
    print()
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
