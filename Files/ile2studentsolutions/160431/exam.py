from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self, *args):
        assert len(args) != 0, 'no dictionaries'
        self.dl = []
        for a in args:
            assert type(a) is dict, f'{a} is not a dictionary'
            self.dl.append(a)
            
    def __len__ (self):
        length = set()
        for d in self.dl:
            for key in d:
                length.add(key)
        return len(length)

    def __repr__ (self):
        return f"DictList({','.join(str(d) for d in self.dl)})"
 
    def __contains__ (self, key):
        return any(key in d for d in self.dl)
         
    def __getitem__ (self, key):
        if self.__contains__(key):
            new = [d for d in self.dl if key in d]
            return new[-1][key]
        else:
            raise KeyError
    
    def __setitem__ (self, key, value):
        if self.__contains__(key):
            t = enumerate(self.dl)
            new = [i[0] for i in t]
            self.dl[new[-1]][key] = value
        else:
            self.dl.append({key:value})
            
    def __call__ (self, key):
        result = []
        if self.__contains__(key):
            for d in self.dl:
                if key in d:
                    result.append((d.index(), self.dl[d][key]))
        return result
    
    def __iter__ (self):
        new = set()
        for d in self.dl:
            for k in d:
                new.add(k)
        for n in new:
            yield (n, self.__getitem__(n))
       
    def __eq__ (self, right):
        if type(right) is dict:
            new = set()
            for d in self.dl:
                for k in d:
                    new.add(k)
            return new == right.keys() and all(right[key] == self.__getitem__(key) for key in new)
        elif type(right) is DictList:
            new_self = set()
            for d in self.dl:
                for k in d:
                    new_self.add(k)
            new_right = set()
            for d in right.dl:
                for k in d:
                    new_self.add(k)
            return new_self == new_right and all(self.__getitem__(key) == right.__getitem__(key) for key in new_self)
        else:
            raise TypeError('cannot compare DictList object with non-dict or non-DictList object')
       
    def __add__ (self, right):
        pass
         
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
