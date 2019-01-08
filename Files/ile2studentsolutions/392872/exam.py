from goody import type_as_str  # Useful in some exceptions
from Tools.demo.sortvisu import distinct

class DictList:
    def __init__(self, *args):
        assert len(args) > 0, "DictList must be given at least one argument"
        self.dl = []
        for a in args:
            assert type(a) == dict, f"{a} is not a dictionary"
            self.dl.append(a)
        
    def __len__(self):
        distinctKeys = []
        for d in self.dl:
            for k in d.items():
                if k[0] not in distinctKeys:
                    distinctKeys.append(k[0])
        return len(distinctKeys)
        
    def __repr__(self):
        result = "DictList("
        result += ', '.join([str(d) for d in self.dl]) + ")"
        return result

    def __contains__(self, value):
        for d in self.dl:
            if value in d.keys():
                return True
        return False
    
    def __getitem__(self, name):
        if self.__contains__(name) == False:
            raise KeyError(f"'{name}' appears in no dictionaries")
        
        for d in self.dl.__reversed__():
            if name in d.keys():
                return d[name]
        
    def __setitem__(self, name, value):
        if self.__contains__(name) == False:
            self.dl.append({name: value})
        else:
            for d in self.dl.__reversed__():
                if name in d.keys():
                    d[name] = value
                    break
                
    def __call__(self, name):
        result = []
        
        for i in range(0, len(self.dl)):
            d = self.dl[i]
            if name in d.keys():
                result.append((i, d[name]))
        
        return result
    
    def __iter__(self):
        iterList = []
        for d in self.dl.__reversed__():
            dList = []
            for item in d.items():
                unique = True
                for i in iterList:
                    if i[0] == item[0]:
                        unique = False
                if unique:
                    dList.append(item)
            for i in sorted(dList, key = lambda x: x[0]):
                iterList.append(i)
                
        class dl_iter:
            def __init__(self, iterable):
                self._iterable = iterable
            def __next__(self):
                if len(self._iterable) <= 0:
                    raise StopIteration
                else:
                    return self._iterable.pop(0)
            def __iter__(self):
                return self
        
        return dl_iter(iterList)
    
    def __eq__(self, value):
        distinctKeys = []
        for d in self.dl:
            for k in d.items():
                if k[0] not in distinctKeys:
                    distinctKeys.append(k[0])
        distinctKeys = sorted(distinctKeys)
        
        if type(value) == dict:
            d2Keys = sorted(list(value.keys()))
            if distinctKeys != d2Keys:
                return False
            for i in d2Keys:
                if value[i] != self.__getitem__(i):
                    return False
            return True
        elif type(value) == type(self):
            d2Keys = []
            for d in value.dl:
                for k in d.items():
                    if k[0] not in d2Keys:
                        d2Keys.append(k[0])
            d2Keys = sorted(d2Keys)
            
            if distinctKeys != d2Keys:
                return False
            for i in d2Keys:
                if self.__getitem__(i) != value[i]:
                    return False
            return True
        else:
            raise TypeError(f"Trying to compare invalid type: {type(value)}")
                
        
    
    def __add__(self, value):
        def uniqueDict(dl: DictList) -> dict:
            distinctKeys = []
            for d in dl.dl:
                for k in d.items():
                    if k[0] not in distinctKeys:
                        distinctKeys.append(k[0])
            d = {}
            for i in distinctKeys:
                d[i] = dl[i]
            return d
                        
        if type(value) == DictList:
            return DictList(uniqueDict(self), uniqueDict(value))
        elif type(value) == dict:
            arg = "DictList(" + ', '.join([str(d) for d in self.dl]) + ", " + str(value) + ")"
            return eval(arg)
        else:
            raise TypeError(f"Trying to add invalid type: {type(value)}")
                            
    def __radd__(self, value):
        if type(value) == dict:
            arg = "DictList(" + str(value) + ", " + ', '.join([str(d) for d in self.dl]) + ")"
            return eval(arg)
        else:
            raise TypeError(f"Trying to add invalid type: {type(value)}")
        
    
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    dl = DictList(dict(a=1,b=2,c=3),
                  dict(c=13,d=14,e=15),
                  dict(e=25,f=26,g=27))
    
    dl2 = DictList(dict(a=1,b=2,c=3),
                  dict(c=13,d=14,e=15),
                  dict(e=25,f=26,g=27))
    
    dl + dl2

    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
