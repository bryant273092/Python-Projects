from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        if len(args) == 0:
            raise AssertionError("DictList.__init__: argument must be a dictionary")
        for i in args:
            if type(i) != dict:
                raise AssertionError("DictList.__init__: {} is not a dictionary".format(i))
            else:
                self.dl.append(i)
    
    def __len__(self):
        keys = set()
        for i in self.dl:
            for k in i.keys():
                keys.add(k)
        return len(keys)
    
    def __repr__(self):
        return "DictList({})".format(", ".join(str(x) for x in self.dl))
    
    def __contains__(self,left):
        if type(left) != str:
            return False
        for i in self.dl:
            for k in i.keys():
                if left in k:
                    return True
    
    def __getitem__(self,key):
        keylist = []
        for i in self.dl:
            for k in i.items():
                if key == k[0]:
                    keylist.append(k[1])
        if len(keylist) == 0:
            raise KeyError("{} appears in no dictionary".format(key))
        return keylist[-1]
    
    def __setitem__(self,key,value):
        for i in reversed(self.dl):
            for k in i.keys():
                if key in k:
                    self.dl[self.dl.index(i)][key] = value
    
    def __call__(self, key):
        indexlist = []
        for i in self.dl:
            for k in i.items():
                if key in k:
                    indexlist.append((self.dl.index(i), k[1]))
        return indexlist
    
    def __iter__(self):
        pass
    
    def __eq__(self, right):
        if type(right) not in (DictList, dict):
            raise TypeError("DictList.__eq__: {} must be of type DictList or Dict".format(right))
        keylist1 = []
        keylist2 = []
        for i in reversed(self.dl):
            for k in i.items():
                if k not in keylist1:
                    keylist1.append(k)
        if type(right) == DictList:
            for i in reversed(right.dl):
                for k in i.items():
                    if k not in keylist2:
                        keylist2.append(k)
        else:
            for k in right.items():
                if k not in keylist2:
                    keylist2.append(k)
                    
        return sorted(keylist1) == sorted(keylist2)
                




            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d = DictList({'a':1, 'b':2, "c":9}, {"c":3, "d":4}, {"e":2, "f":6, "g":2})
    e = DictList({'a':1, 'b':2, "c":9}, {"c":3, "d":4}, {"e":2, "f":6, "g":2})
    f = DictList({"a":1, "b":2, "c":9})
    print(len(d))
    print(repr(d))
    print("v" in d)
    print(d['c'])
    print(d("l"))
    d1 = DictList(dict(b=2,c=13,d=14,e=25,f=26,g=27))
    d3 = DictList(dict(b=2,c=3),dict(c=13,d=14,e=15),dict(e=25,f=26,g=27))
    print(d1==d3)
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
