from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self,*args):
        self.dl = []
        if len(args) == 0:
            raise AssertionError()
        for d in args:
            assert type(d) is dict, 'DictList.__init__: ' + repr(d) + 'is not a dictionary'
            self.dl.append(d)
            
    def __len__(self):
        keys = []
        for d in self.dl:
            for k in d.keys():
                if k not in keys:
                    keys.append(k)
        return len(keys)
    
    def __repr__(self):
        return 'DictList(' + ', '.join([str(d) for d in self.dl]) + ')'
    
    def __contains__(self, key):
        for d in self.dl:
            for k in d.keys():
                if key == k:
                    return True
        return False
    
    def __getitem__(self, key):
        temp = reversed(self.dl)
        if self.__contains__(key):
            for t in temp:
                if key in t:
                    return t[key]
        else:
            raise KeyError(repr(key) + 'does not appear in any dictionary')
            
    def __setitem__(self, key, v):
        if self.__contains__(key):
            for t in range(1, len(self.dl) + 1):
                if key in self.dl[-t]:
                    self.dl[-t][key] = v
                    break
        else:
            self.dl.append({key:v})
            
    def __call__(self, key):
        answer = []
        for d in range(len(self.dl)):
            if key in self.dl[d]:
                answer.append((d,self.dl[d][key]))
        return answer
    
    def __iter__(self):
        keys = []
        answer = []
        for t in range(1, len(self.dl) + 1):
            temp = []
            for key in self.dl[-t]:
                if key not in keys:
                    keys.append(key)
                    temp.append((key,self.dl[-t][key]))
            new = sorted(temp)
            for v in new:
                answer.append(v)
        for a in answer:
            yield a
        
    def __eq__(self,right):
        if type(right) not in (DictList,dict):
            raise TypeError(repr(right) + 'is the wrong type')
        else:
            if type(right) == DictList:
                for d in self.dl:
                    for key in d:
                        if not right.__contains__(key):
                            return False
                        if self.__getitem__(key) != right.__getitem__(key):
                            return False
                return True
            else:
                temp = DictList(right)
                for d in self.dl:
                    for key in d:
                        if not temp.__contains__(key):
                            return False
                        if self.__getitem__(key) != temp.__getitem__(key):
                            return False
                return True

            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d = DictList({'a':1, 'b':2, 'c':3}, {'c':13, 'd':14, 'e':15}, {'e':25, 'f':26, 'g':27})
    print(len(d))
    print(repr(d))
    print('c' in d)
    print(d['c'])
    print(d)
    print(d('a'))
    print(d('e'))
    print(d('x'))
    for a in d:
        print(a)
    v = DictList({'a':1, 'b':2, 'c':3}, {'c':13, 'd':14, 'e':15}, {'e':25, 'f':26, 'g':27})
    print(d == v)
    a = {'d':1}
    b = DictList({'d':1})
    print(a == b)
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
