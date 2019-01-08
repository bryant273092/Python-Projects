from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self, *args):
        assert len(args), f'DictList.__init__:no dictionaries recived.'
        self.dl = []
        for i in args:
            assert type(i) == dict, f'DictList.__init__:{i} is not a dictionary.'
            self.dl.append(i)
    
    def __len__(self):
        have = set()
        count = 0
        for d in self.dl:
            for i in d:
                if i not in have:
                    count += 1
                    have.add(i)
        return count

    def __repr__(self):
        return f"DictList({str(self.dl)[1:-1]})"
    
    def __contains__(self, key):
        for d in self.dl:
            if key in d:
                return True
        return False
    
    def __getitem__(self, key):
        result = None
        for d in self.dl:
            if key in d:
                result = d[key]
        if not result:
            raise KeyError
        return result
    
    def __setitem__(self, key, value):
        l = len(self.dl)
        do = False
        for i in range(l-1, -1, -1):
            if key in self.dl[i]:
                self.dl[i][key] = value
                do = True
                break
        if not do:
            self.dl.append({key:value})
            
    def __call__(self, key):
        result = []
        for i, d in enumerate(self.dl):
            if key in d:
                result.append((i, d[key]))
        return result
    
    def __iter__(self):
        have = set()
        for i in range(len(self.dl)-1, -1, -1):
            for k,v in self.dl[i].items():
                if k not in have:
                    have.add(k)
                    yield k,v
    
    def __eq__(self, b):
        if type(b) not in [DictList, dict]:
            raise TypeError
        for k,v in self:
            if k not in b or v != b[k]:
                return False
        return True
    
    def __add__(self, b):
        if type(b) not in [DictList, dict]:
            raise TypeError
        k1 = {}
        k2 = {}
        for k,v in self:
            k1[k] = v
        if type(b) == dict:
            k2 = b
        else:
            for k,v in b:
                k2[k] = v
        return eval(f"DictList({k1}, {k2})")
    
    def __radd__(self, b):
        if type(b) not in [DictList, dict]:
            raise TypeError
        k1 = {}
        k2 = {}
        for k,v in self:
            k1[k] = v
        if type(b) == dict:
            k2 = b
        else:
            for k,v in b:
                k2[k] = v
        return eval(f"DictList({k2}, {k1})")
        
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    d2 = DictList(dict(a='one',b='two'), dict(b='twelve',c='thirteen'))
    adict = dict(a='one',b='two')
    d1+adict
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
