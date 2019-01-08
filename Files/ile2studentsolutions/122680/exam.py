from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl =[]
        assert len(args) >= 1
        for x in args:
            assert type(x) is dict, str(x)+ 'is a ' + type_as_str(x) + ',is not a dictionary'
            self.dl.append(x)
    
    def __len__(self):
        return len(set(k for x in self.dl for k in x))
        
    def __repr__(self):
        return 'DictList(' + ','.join(str(x) for x in self.dl) + ')'

    def __contains__(self, item):
        return any(item in d for d in self.dl)
    
    def __getitem__(self, item):
        result = None
        for d in self.dl:
            for k in d:
                if k == item:
                    result = d[k]
        if result == None:
            raise KeyError
        return result
    
    def __setitem__(self, item, value):
        if not self.__contains__(item):
            self.dl.append({item:value})
        else:
            for d in self.dl[::-1]:
                for k in d:
                    if k == item:
                        d[k] = value
                        return
    
    def __call__(self, item):
        return [(self.dl.index(d), d[k]) for d in self.dl for k in d if item == k]
    
    def __iter__(self):
        exist_set = set()
        for d in self.dl[::-1]:
            for k in sorted(d):
                if k not in exist_set:
                    yield(k, d[k])
                    exist_set.add(k)
    
    def __eq__(self, right):
        if type(right) in (dict, DictList):
            return all(k in right for k,v in self) and all([v == right[k] for k, v in self ])
        else:
            raise TypeError
    
    def __add__(self, right):
        if type(right) is DictList:
            return DictList({k:v for k,v in self}, {k:v for k,v in right})
        elif type(right) is dict:
            return DictList(*(d for d in self.dl), dict(right))
        else:
            raise TypeError
    
    def __radd__(self, left):
        if type(left) is dict:
            return DictList(dict(left), *(d for d in self.dl))
        else:
            raise TypeError
            
             
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
#     d2 = DictList(dict(b=2,c=13,d=15,e=25,f=26,g=27))
#     for k,v in d1:
#         print((k,v), end=',')
#     print()
#     for k,v in d2:
#         print((k,v), end=',')
#     print
#     print(d1 == d2)
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
