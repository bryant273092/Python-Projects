from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        for item in args:
            if type(item) != dict:
                raise AssertionError(f"DictList.__init__: {item} is not a dictionary")
        if args == ():
            raise AssertionError(f"DictList.__init__: DictList constructor requires at least 1 argument")
        self.dl = [i for i in args]
        
    def __len__(self):
        result = set()
        for d in self.dl:
            for k in d.keys():
                result.add(k)
        return len(result)
    
    def __repr__(self):
        result = tuple((i for i in self.dl))
        return f"DictList{result}"
    
    def __contains__(self, item):
        for d in self.dl:
            if item in d:
                return True
        return False
    
    def __getitem__(self, item):
        if not item in self:
            raise KeyError(f"{item} appears in no dictionaries")
        for d in reversed(self.dl):
            if item in d:
                return d[item]
            
    def __setitem__(self, item, value):
        if item in self:
            for d in reversed(self.dl):
                if item in d:
                    d[item] = value
                    return
        else:
            self.dl.append({item: value})
            
    def __call__(self, item):
        result = []
        if item not in self:
            return result
        for i,d in enumerate(self.dl):
            if item in d:
                result.append((i, d[item]))
        return result
    
    def __iter__(self):
        unique_keys = []
        iterable = []
        for d in reversed(self.dl):
            result = []
            for k in d:
                if k not in unique_keys:
                    result.append(k)
                    unique_keys.append(k)
            iterable.append(sorted(result))
        
        def gen(iterable):
            for item in iterable:
                for key in item:
                    yield (key, self[key])
        
        return gen(iterable)
    
    def __eq__(self, right):
        if type(right) not in (DictList, dict):
            raise TypeError(f"{right} is not  of type DictList or dict\n  type(right): {type_as_str(right)}")
        
        self_keys = set()
        for d in self.dl:
            for k in d:
                self_keys.add(k)
        
        right_keys = set()
        
        if type(right) == DictList:
            for d in right.dl:
                for k in d:
                    right_keys.add(k)
        else:
            for k in right:
                right_keys.add(k)
        
        if self_keys != right_keys:
            return False
        for k in self_keys:
            if self[k] != right[k]:
                return False
        return True
    
    def __add__(self, right, radd=None):
        
        if type(right) not in (DictList, dict):
            raise TypeError(f"{right} is not  of type DictList or dict\n  type(right): {type_as_str(right)}")

        
        result = []
        inner = dict()
        for d in self.dl:
            inner = dict()
            for k in d:
                inner[k] = d[k]
            result.append(inner)
            
        if type(right) == DictList:
            inner = dict()
            for d in right.dl:
                for k in d:
                    inner[k] = right[k]
            result.append(inner)
            
        else:
            result.append(right.copy())
        
        if radd:
            new = [result[-1]]
            for i in result[0:-1]:
                new.append(i)
            result = new
        
        return DictList(*result)
    
    def __radd__(self, right):
        return self.__add__(right, True)
                
                
                    

        




            
if __name__ == '__main__':



    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
