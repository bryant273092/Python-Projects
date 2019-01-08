from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *arg):
        assert len(arg) != 0 and all(isinstance(x, dict) for x in arg), f'Assertions for init FAIL!'
        self.dl = [x for x in arg]
      
    def __len__(self):
        result = set()
        for d in self.dl:
            result = result.union(set(d))
        return len(result)
    
    def __repr__(self):
        return f'DictList(*{self.dl})'

    def __contains__(self,item):
        return any(item in d for d in self.dl)
    
    def __getitem__(self,item):
        if item in self:
            for d in reversed(self.dl):
                if item in d:
                    return d[item]
        else:
            raise KeyError(f'{item} is not a key here!!!')

    def __setitem__(self,item,value):
        if item in self:
            for d in reversed(self.dl):
                if item in d:
                    d[item] = value 
                    return
        else:
            self.dl.append({item:value})

    def __call__(self, key):
        return [(i, d[key]) for i,d in enumerate(self.dl) if key in d]
    
    def __iter__(self):
        used = set()
        for d in reversed(self.dl):
            for key, value in sorted(d.items()):
                if key not in used:
                    yield key, value 
                    used.add(key)
                
    def __eq__(self, right):
        if isinstance(right, (DictList, dict)):
            return len(right) == len(self) and all(key in right and value == right[key] for key, value in self)
        else:
            raise TypeError("Can't compare!!!")
                
    def __add__(self, right):
        if isinstance(right, dict):
            return DictList(*[d.copy() for d in self.dl], right.copy()) 
        elif isinstance(right, DictList):
            d1 = {key:value for key, value in self}
            d2 = {key:value for key, value in right}
            return DictList(d1,d2)      
        else:
            raise TypeError("Undefined type to add")
    
    def __radd__(self, left):
        if isinstance(left, dict):
            return DictList(left.copy(), *[d.copy() for d in self.dl]) 
        elif isinstance(left, DictList):
            d1 = {key:value for key, value in left}
            d2 = {key:value for key, value in self}
            return DictList(d1,d2)  
        else:
            raise TypeError("Undefined type to add")
        
        
            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
#     d1 = DictList(dict(a={1,4,5},b=2), dict(b=12,c=13))
#     d2 = dict(a=[1,4,5],b=2)
#     d = d1 + d2
#     print(d)
#     d2['a'] = 5
#     print(d)
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
