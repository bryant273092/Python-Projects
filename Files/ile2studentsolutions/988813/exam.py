from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        assert len(args) > 0, "should have at least one arguments"
        self.dl = []
        for i in args:
            assert type(i) is dict, "{} is not a dictionary".format(i)
            self.dl.append(i)
            
    def __len__(self):
        kl = list()
        for d in self.dl:
            for k in d:
                kl.append(k)
        return len(set(kl))
        
    def __repr__(self):
        return "DictList({})".format(",".join([repr(d) for d in self.dl]))
    
    def __contains__(self, item):
        return any(item in d for d in self.dl)
    
    def __getitem__(self, index):
        if index not in self:
            raise KeyError
        for i in range(len(self.dl)):
            if index in self.dl[len(self.dl)-(i+1)]:
                return self.dl[len(self.dl)-(i+1)][index]
            
    def __setitem__(self, index, value):
        if index not in self:
            d = dict()
            d[index] = value
            self.dl.append(d)
        else:
            for i in range(len(self.dl)):
                if index in self.dl[len(self.dl)-(i+1)]:
                    self.dl[len(self.dl)-(i+1)][index] = value
                    break
            
    def __call__(self, key):
        result = []
        for i in range(len(self.dl)):
            if key in self.dl[i]:
                result.append((i, self.dl[i][key]))
        return result

    def __iter__(self):
        old = set()
        for i in range(len(self.dl)):
            for k in sorted(self.dl[len(self.dl)-(i+1)]):
                if k not in old:
                    yield (k, self.dl[len(self.dl)-(i+1)][k])
                    old.add(k)
    
    def __eq__(self, right):
        if type(right) == type(self) or type(right) is dict:
            if len(self) != len(right):
                return False
            else:
                for d in self.dl:
                    for k in d:
                        if k not in right:
                            return False
                        elif self[k] != right[k]:
                            return False
                return True
        else:
            raise TypeError("the right operand should be a DictList or a dict")
        
    def __add__(self, right):
        if type(right) == type(self):
            return DictList(dict(iter(self)), dict(iter(right)))
        elif type(right) is dict:
            return eval(repr(self)[:-1]+","+repr(right)+")")
        else:
            raise TypeError
    
    def __radd__(self, left):
        if type(left) == type(self):
            return DictList(dict(iter(left)), dict(iter(self)))
        elif type(left) is dict:
            return eval("DictList({d},{dl})".format(d = repr(left), dl = repr(self)[9:-1]))
        else:
            raise TypeError
                
            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    adict = dict(a='one',b='two')
    d2 = d1+adict

    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
