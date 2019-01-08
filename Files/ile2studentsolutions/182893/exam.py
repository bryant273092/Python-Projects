from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        assert len(args) > 0
        assert all([type(item) == dict for item in args])
        self.dl = [*args]
        
    def __len__(self):
        result = set()
        for dict_ in self.dl:
            result = result | set(dict_.keys())
        return len(result) 
    
    def __repr__(self):
        return "DictList({})".format(", ".join([str(item) for item in self.dl]))

    def __contains__(self, value):
        for dict_ in self.dl:
            if value in dict_.keys():
                return True
        return False
    
    def __getitem__(self, value):
        if value not in self:
            raise KeyError
        result = []
        for dict_ in self.dl:
            result.append(dict_.get(value, None))
        for item in reversed(result):
            if item is not None:
                return item
    
    def __setitem__(self, key, value):
        if key in self:
            to_change = None
            for i in range(len(self.dl)):
                if key in self.dl[i]:
                    to_change = i
            self.dl[to_change][key] = value
        else:
            self.dl.append({key: value})
            
    def __call__(self, key):
        result = []
        for i, dict_ in enumerate(self.dl):
            if key in dict_:
                result.append((i, dict_[key]))
        return result
    
    def __iter__(self):
        def generator():
            already_yield = set()
            for dict_ in reversed(self.dl):
                for key in sorted(list(dict_.keys())):
                    if key not in already_yield:
                        already_yield.add(key)
                        yield (key, dict_[key])
                
        return generator()
    
    def __eq__(self, other):
        if type(other) not in [dict, DictList]:
            raise TypeError
        keys = []
        for dict_ in self.dl:
            keys.extend(dict_.keys())
        keys = list(set(keys))
        for key in keys:
            if key not in other or self[key] != other[key]:
                return False
        return True
    
    def __add__(self, other):
        if type(other) == dict:
            copy = {}
            for key, value in other.items():
                copy[key] = value
            return DictList(*self.dl, copy)
        if type(other) == DictList:
            return DictList({key: value for key, value in self}, {key: value for key, value in other})
        else:
            return NotImplemented
    
    def __radd__(self, other):
        if type(other) == dict:
            copy = {}
            for key, value in other.items():
                copy[key] = value
            return DictList(copy, *self.dl)
        else:
            return NotImplemented
    
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    adict = dict(a='one',b='two')
    print(str(adict))
    d = d1 + adict
    print(d)
    d1['b'] = 'x'
    print(d)
    
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
    driver.default_show_traceback=True
    driver.driver()
