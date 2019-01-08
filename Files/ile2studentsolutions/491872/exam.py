from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self, *args):
        self.dl = []
        assert len(args) != 0
        for arg in args:
            assert type(arg) is dict, f"DictList.__init__: '{arg}' is not a dictionary."
        for arg in args:
            self.dl.append(arg)
    
    def __len__(self):
        #return len(set([d for d in self.dl[x] for x in self.dl]))
        found = set()
        count = 0
        for d in self.dl:
            for key in d:
                if key not in found:
                    count += 1
                    found.add(key)
        return count
    
    def __repr__(self):
        res = 'DictList{args}'
        a = ''
        for d in self.dl:
            a += f'{d}, '
        return res.format(args = f'({a.rstrip(", ")})')

    def __contains__(self, item):
        for d in self.dl:
            if item in d:
                return True
        return False
    
    def __getitem__(self, item):
        cd = []
        for d in self.dl:
            if item in d:
                cd.append(d)
        if cd == []: raise KeyError(f'{item} appears in no dictionaries')
        highest = sorted(cd, key = lambda x: self.dl.index(x))[-1]
        return highest[item]
    
    def __setitem__(self, item, value):
        last = None
        inside = False
        for d in self.dl:
            if item in d:
                last = d
        if last == None:
            self.dl.append({item: value})
        else:
            last[item] = value
            self.dl[self.dl.index(last)] = last
    
    def __call__(self, item):
        res = []
        for d in self.dl:
            if item in d:
                res.append((self.dl.index(d), d[item]))
        return res
            
    def __iter__(self):
        produced = set()
        for d in self.dl[::-1]:
            for key in d:
                if key not in produced:
                    yield (key, d[key])
                    produced.add(key)
    
    def __eq__(self, right):
        if type(right) not in (DictList, dict): raise TypeError(f'right operand is type {type_as_str(type(right))}; must be dict or DictList.')
        self_keys = set()
        for d in self.dl:
            for key in d:
                self_keys.add(key)
        if type(right) is DictList:
            right_keys = set()
            for d in right.dl:
                for key in d:
                    right_keys.add(key)
            return self_keys == right_keys and all([self[key] == right[key] for key in self_keys])
        else: # type is dict
            return self_keys == set(right.keys()) and all([self[key] == right[key] for key in self_keys])
    
    def __add__(self, right):
        if type(right) not in (DictList, dict): raise TypeError(f'right operand is type {type_as_str(type(right))}; must be dict or DictList.')
        if type(right) is DictList:
            return DictList({k:v for k,v in self}, {k:v for k,v in right})
        else:
            return DictList({k:v for k,v in self}, right.copy())
    
    

            
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
