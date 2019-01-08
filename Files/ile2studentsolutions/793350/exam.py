from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        assert len(args) >= 1
        
        self.dl = []
        for item in args:
            assert type(item) == dict, f'Dict_list.__init : {item} is not a dictionary'
            self.dl.append(item)
    
    def __len__(self):
        length = []
        for d in self.dl:
            for k in d.keys():
                length.append(k)
        return len(set(length))
    
    def __repr__(self):
        return 'DictList(' + ','.join([str(x) for x in self.dl]) + ')'
                   
    def __contains__(self, key):    
        for d in self.dl:
            if key in d.keys():
                return True
        return False
    
    def __getitem__(self, key):
        keys = []
        for d in self.dl:
            for k in d.keys():
                keys.append(k)
        if key not in keys:
            raise KeyError('Key not in dictionary')
        for d in self.dl:
            for k,v in d.items(): 
                if k == key:
                    temp = v
        return temp
    
    def __setitem__(self, key, value):
        if self.__contains__(key):
            for d in reversed(self.dl):
                if key in  d.keys():
                    d[key] = value       
                    break
        else:
            self.dl.append({key:value})
                
    def __call__(self, key):        
        x = []
        for i, d in enumerate(self.dl):
            if key in d.keys():
                x.append((i, d[key]))
        return sorted(x)
    
    def __iter__(self):
        keys = []
        for d in reversed(self.dl):
            for k, v in sorted(d.items()):
                if k not in keys:
                    keys.append(k)
                    yield (k, v)
                    
    def __eq__(self, right):
        if type(right) not in (DictList, dict):
            raise TypeError(f'right operand not Dict List or dict but is {type(right)}')
        
        elif isinstance(right, DictList):
            for k, v in self:
                if k not in right or self[k] != right[k]:
                    return False
        
        elif isinstance(right, dict):
            for k, v in self:
                if k not in right or self[k] != right[k]:
                    return False
                
        return True
    
    def __add__(self, right):
        if type(right) == DictList:
            return DictList({k:v for k,v in self}, {k:v for k,v  in right})        
        
        elif type(right) == dict:
            x = []
            for d in self.dl:
                x.append(d)
            x.append(right)
            dicts = ','.join([str(d) for d in x])
            return eval(f'DictList({dicts})')
                
        else:
            raise TypeError('Not a dict or DictList')   
                
        
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
