from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *dicts):
        self.dl = []
        if len(dicts) > 0:
            for d in dicts:
                assert type(d) is dict, f'DictList.__init__: {d} is not a dictionary'
                self.dl.append(d)
        else:
            assert False, 'DictList.__itit__: cannot be empty'
            
    def __len__(self):
        result = set()
        for d in self.dl:
            for k in d:
                result.add(k)
        return len(result)
    
    def __repr__(self):
        return f'DictList({", ".join([str(d) for d in self.dl])})'
    
    def __contains__(self, item):
        for d in self.dl:
            if item in d:
                return True
        return False
    
    def __getitem__(self, item):
        result = None
        for d in self.dl:
            for k, v in d.items():
                if k == item:
                    result = v
        if result is None:
            raise KeyError(f'DictList.__getitem__: {item} is not valid key')
        return result
    
    def __setitem__(self, item, value):
        index = None
        if item in self:
            for n, d in enumerate(self.dl):
                if item in d:
                    index = n
            self.dl[index][item] = value
        else:
            self.dl.append({item : value})
            
    def __call__(self, item):
        result = []
        for i, d in enumerate(self.dl):
            if item in d:
                result.append((i, d[item]))
        return result
    
    def __iter__(self):
        def gen(dict_list):
            produced = set()
            for d in reversed(dict_list):
                for item in sorted(d):
                    if item not in produced:
                        yield (item, d[item])
                        produced.add(item)
        return gen(list(self.dl))
    
    def __eq__(self, right):
        if type(right) in (DictList, dict):
            for k, v in self:
                if (k not in right) or v != right[k]:
                    return False
            return True
        else:
            raise TypeError(f'DictList.__eq__: {type_as_str(right)} is not a DictList or dict')
        
    def __add__(self, right):
        if type(right) is DictList:
            return DictList({k : v for k, v in self}, {k : v for k, v in right})
        elif type(right) is dict:
            return DictList(*tuple(self.dl), dict(right))
        else:
            raise TypeError(f'DictList.__add__: {type_as_str(right)} is not supported for adding')
        
    def __radd__(self, left):
        if type(left) is dict:
            return DictList(dict(left), *tuple(self.dl))
        else:
            raise TypeError(f'DictList.__radd__: {type_as_str(left)} is not supported for adding')
                    
            




            
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
