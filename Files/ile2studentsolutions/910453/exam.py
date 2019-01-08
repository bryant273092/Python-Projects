from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        if len(args) == 0: assert False, "DictList.__init__: there must be at least one argument to define DictList"
        self.dl = []
        for d in args:
            if type(d) is not dict: assert False, f"DictList.__init__: {d} is not a dictionary"
            self.dl.append(d)
            
    def __len__(self):
        unique = set()
        for d in self.dl:
            for k in d:
                unique.add(k)
        return len(unique)

    def __repr__(self):
        return 'DictList' + str(tuple(self.dl))

    def __contains__(self, item):
        for d in self.dl:
            if item in d: return True
        return False
    
    def __getitem__(self, item):
        for i in range(len(self.dl)-1, -1, -1):
            if item in self.dl[i]: return self.dl[i][item]
        raise KeyError(f'DictList.__getitem__: {item} not in {self}')
    
    def __setitem__(self, item, v):
        if item in self:
            for i in range(len(self.dl)-1, -1, -1):
                if item in self.dl[i]: 
                    self.dl[i][item] = v
                    break
        else:
            self.dl.append({item:v})
            
    def __call__(self, item):
        result = []
        for i in range(len(self.dl)):
            if item in self.dl[i]: result.append((i, self.dl[i][item]))
        return result
    
    def __iter__(self):
        def gen(d):
            produced = set()
            for i in range(len(d)-1, -1, -1):
                for key in sorted(list(d[i].keys())):
                    if key in produced: continue
                    else:
                        produced.add(key)
                        yield (key, d[i][key])
        return gen(self.dl.copy())
    
    def __eq__(self, right):
        if type(right) is dict:
            for x in self:
                if x[0] not in right: return False
            for k in right:
                if k not in self: return False
                if self[k] != right[k]: return False
            return True
        elif type(right) is DictList:
            return {x for x in self} == {y for y in right}
        else: raise TypeError(f'DictList.__eq__: {type_as_str(right)} is not comparable to a DictList')
        
    def __add__(self, right):
        if type(right) is DictList:
            return DictList(dict([x for x in self]), dict([y for y in right]))
        elif type(right) is dict:
            return DictList(*self.dl, right.copy())
        else: raise TypeError(f'DictList.__add__: {type_as_str(right)} cannot be added to DictList')
    
    def __radd__(self, left):
        if type(left) is not dict: 
            raise TypeError(f'DictList.__radd__: {type_as_str(left)} cannot be added to DictList')
        return DictList(left.copy(), *self.dl)
    
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
