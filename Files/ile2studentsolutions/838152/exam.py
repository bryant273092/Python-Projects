class DictList:
    def __init__(self, *arg):
        if arg == ():
            raise AssertionError("DictList.__init__: expected dictionary arguments")
        for d in arg:
            if type(d) is not dict:
                raise AssertionError(f"DictList.__init__: {d} is not a dictionary")
        self.dl = list(arg)

    def __len__(self):
        temp_set = set()
        for d in self.dl:
            for k in d.keys():
                temp_set.add(k)
        return len(temp_set)
    
    def __repr__(self):
        return f"DictList({', '.join(str(i) for i in self.dl)})"

    def __contains__(self, value):
        return any([value in d for d in self.dl])
    
    def __getitem__(self, index):
        if index not in self: raise KeyError(f"DictList.__getitem__: {index} is not in DictList")
        for i in range(len(self.dl)):
            if index in self.dl[-(i+1)]:
                return self.dl[-(i+1)][index]
    
    def __setitem__(self, index, value):
        if index not in self:
            self.dl.append({index: value})
        else:
            for i in range(len(self.dl)):
                if index in self.dl[-(i+1)]:
                    self.dl[-(i+1)][index] = value
                    return
    
    def __call__(self, key):
        return [(i, self.dl[i][key]) for i in range(len(self.dl)) if key in self.dl[i]]
    
    def __iter__(self):
        class DL_iter:
            def __init__(self, dl):
                self.dl = dl
                self.produced = []
            def __next__(self):
                for i in range(len(self.dl)):
                    for k,v in sorted(self.dl[-(i+1)].items(), key=lambda x: x[0]):
                        if k not in self.produced:
                            self.produced.append(k)
                            return (k,v)
                raise StopIteration
            def __iter__(self):
                return self
        
        return DL_iter(self.dl)
    
    def __eq__(self, right):
        if type(right) is not DictList and type(right) is not dict:
            raise TypeError(f"DictList.__eq__: {right} is not a DictList or dict")
        d = {i[0]:i[1] for i in self}
        if type(right) is DictList:
            r_d = {i[0]:i[1] for i in right}
            return d == r_d
        elif type(right) is dict:
            return d == right
    
    def __add__(self, right):
        if type(right) is not DictList and type(right) is not dict:
            raise TypeError(f"DictList.__add__: {right} is not a DictList or dict")
        if type(right) is DictList:
            return DictList({i[0]:i[1] for i in self} , {i[0]:i[1] for i in right})
        elif type(right) is dict:
            return DictList(*([d.copy() for d in self.dl]+[right.copy()]))
    
    def __radd__(self, left):
        if type(left) is not DictList and type(left) is not dict:
            raise TypeError(f"DictList.__add__: {left} is not a DictList or dict")
        if type(left) is DictList:
            return left+self
        elif type(left) is dict:
            return DictList(*([left.copy()]+[d.copy() for d in self.dl]))
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
