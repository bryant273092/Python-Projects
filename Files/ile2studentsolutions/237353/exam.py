from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *dicts):
        self.dl = []
        
        if len(dicts) == 0:
            raise AssertionError('DictList.__init__: Must contain at least one dict')
        
        for d in dicts:
            assert type(d) is dict, f"DictList.__init__: {repr(d)} is not a dictionary"
            self.dl.append(d)
            
    
    
    def __len__(self):
        return len(self.get_keys(self))
    
    
    
    def __repr__(self):
        return f"DictList({', '.join([str(d) for d in self.dl])})"
    
    
    
    def __contains__(self, key):
        return any([key in d.keys() for d in self.dl])
    
    
    
    def __getitem__(self, key):
        for d in reversed(self.dl):
            if key in d.keys():
                return d[key]
        raise KeyError(f"{key}")
    
    
    
    def __setitem__(self, key, value):
        if self.__contains__(key):
            for d in reversed(self.dl):
                if key in d.keys():
                    d[key] = value
                    return
                
        else: self.dl.append({key: value})
            
            
    
    def __call__(self, key):
        return [(i, self.dl[i][key]) for i in range(len(self.dl)) if key in self.dl[i].keys()]
    
    
    
    def __iter__(self):
        unused_keys = self.get_keys(self)

        for d in reversed(self.dl):
            for key in sorted(d.keys()):
                if key in unused_keys:
                    unused_keys.remove(key)
                    yield (key, d[key])
                    
                    
                    
    def __eq__(self, right):
        if type(right) is dict: return self.get_keys(self) == set(right.keys()) and all([self.__getitem__(key) == right[key] for key in self.get_keys(self)])
        elif type(right) is DictList: return self.get_keys(self) == self.get_keys(right) and all([self.__getitem__(key) == right.__getitem__(key) for key in self.get_keys(self)])   
        else: raise TypeError(f"{right} is a {type_as_str(right)}. Must be dictionary or DictList")
        
        
        
    def __add__(self, right):
        if type(right) is dict:
            result = eval(self.__repr__())
            result.dl.append({key:right[key] for key in right.keys()})
            return result
        
        elif type(right) is DictList:
            return DictList({key:self.__getitem__(key) for key in self.get_keys(self)},
                            {key:right.__getitem__(key) for key in right.get_keys(right)})
        
        else: raise TypeError(f"{right} is a {type_as_str(right)}. Must be dictionary or DictList")
    
    
    def __radd__(self, left):
        if type(left) is dict:
            result = eval(self.__repr__())
            result.dl = [{key:left[key] for key in left.keys()}] + result.dl
            return result
        
        elif type(left) is DictList:
            return DictList({key:left.__getitem__(key) for key in left.get_keys(left)},
                            {key:self.__getitem__(key) for key in self.get_keys(self)})
        
        else: raise TypeError(f"{left} is a {type_as_str(left)}. Must be dictionary or DictList")
    
    
    @staticmethod
    def get_keys(dl):
        keys = set()
        for d in dl.dl:
            for key in d.keys():
                keys.add(key)
        return keys



            
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
