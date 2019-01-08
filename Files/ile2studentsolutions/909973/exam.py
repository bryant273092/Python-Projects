from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl = []
        if len(args) < 1:  raise AssertionError ('DictList.__init__: None is not a dictionary')
        for x in args:
            if type(x) != dict:
                raise AssertionError ('DictList.__init__: {} is not a dictionary'.format(str(x)))
            else:
                self.dl.append(x)
    def __len__(self):
        result = set()
        for  x in self.dl:
            for k in x.keys():
                result.add(k)
        return len(result)
    
    def __repr__(self):
        return 'DictList({})'.format(','.join([str(x) for x in self.dl]))
    
    def __contains__(self,key):
        for x in self.dl:
            if key in x.keys(): return True
        return False
    
    def __getitem__(self,key):
        if not self.__contains__(key): raise KeyError
        else:
            result = []
            for x in self.dl:
                for k,v in x.items():
                    if k == key :
                        result.append((self.dl.index(x),v))
            return sorted(result,key = lambda x : -x[0])[0][1]
    
    def __setitem__(self,key,value):
        if self.__contains__(key):
            for x in self.dl:
                for k,v in x.items():
                    if k == key and self.__getitem__(key) == v:
                        x[k] = value
        else:
            self.dl.append({key:value})
            
    def __call__(self,key):
        if self.__contains__(key):
            result = []
            for x in self.dl:
                for k,v in x.items():
                    if k == key: result.append((self.dl.index(x),v))
            return result
        else:
            return []
    
    def __iter__(self):
        result = []
        for x in self.dl:
            for k in x.keys():
                if x[k] == self.__getitem__(k): result.append((self.dl.index(x),(k,x[k])))
        for x in sorted(result, key = lambda x: (-x[0],x[1][0])):
            yield x[1]
    
    def __eq__(self,value):
        if type(value) not in (DictList,dict):
            raise TypeError('DictList.__eq__: the type of {} is not DictList nor Dict'.format(str(value)))
        else:
            if type(value) == DictList:
                for x in self.dl:
                    for k in x.keys():
                        if self.__getitem__(k) != value.__getitem__(k): return False
                return True
            else:
                for x in self.dl:
                    for k in x.keys():
                        if k not in value or self.__getitem__(k) != value[k] : return False
                return True
    
    #Extra Credit:
    
    def __add__(self,right):
        if type(right) not in (DictList,dict):
            raise TypeError('DictList.__add__: the type of {} is not DictList nor Dict'.format(str(right)))
        if type(right) == type(self) == DictList:
            d1 = dict()
            d2 = dict()
            for x in self.dl:
                for k in x.keys():
                    d1[k] = self.__getitem__(k)
            for x in right.dl:
                for k in x.keys():
                    d2[k] = right.__getitem__(k)
            return DictList(d1,d2)
        if type(right) == dict:
            newdl = self.dl + [right]
            new = DictList(right)
            new.dl = newdl
            return new

    def __radd__(self,left):
        if type(left) not in (DictList,dict):
            raise TypeError('DictList.__add__: the type of {} is not DictList nor Dict'.format(str(left)))
        if type(left) == dict:
            newdl = [left] + self.dl
            new = DictList(left)
            new.dl = newdl
            return new
            
        




            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    adict = dict(a='one',b='two')
    print(d1+adict)
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
