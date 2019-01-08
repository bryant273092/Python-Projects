# Submitter: rbuwalda(Buwalda, Rheena)
from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        assert len(args) > 0 and all(type(x) is dict for x in args), f"{type_as_str(self)}.__init__: {args} is not a dictionary"
        self.dl = list(args)
        
    def __len__(self):
        k = set()
        {k.update(set(d.keys())) for d in self.dl}
        return len(k)
        
    def __repr__(self):
        string = f"{type_as_str(self)}("
        for d in self.dl:
            string += f"{d}, "
        return string + ')'

    def __contains__(self, item):
        for d in self.dl:
            if item in d:
                return True
        return False
    
    def __getitem__(self, item):
        for d in self.dl[::-1]:
            if item in d:
                return d[item]
        raise KeyError()
    
    def __setitem__(self, key, item):
        found = False
        for d in self.dl[::-1]:
            if key in d:
                found = True
                break
        if found:
            for d in self.dl[::-1]:
                if key in d:
                    d[key] = item
                    break
        else:
            self.dl.append({key: item})
        
    def __call__(self, key):
        result = []
        for i in range(len(self.dl)):
            if key in self.dl[i]:
                result.append((i, self.dl[i][key]))
        return sorted(result, key = lambda f: (f[0], f[1]))
    
    def __iter__(self):
        keys_checked = set()
        for d in self.dl[::-1]:
            for k, v in sorted(d.items()):
                if k not in keys_checked:
                    keys_checked.add(k)
                    yield (k, v)
                    
    def __eq__(self, obj):
        if type(obj) not in (DictList, dict):
            raise TypeError(f"DictList.__eq__: operator == is not supported with {type(obj)}")
        keys = set()
        for d in self.dl:
                for k in d:
                    keys.add(k)
        if type(obj) is DictList:
            return all(self.__getitem__(k) == obj.__getitem__(k) for k in keys)
        else:
            if len(keys) != len(obj):
                return False
            for k in obj:
                return all(self.__getitem__(k) == obj[k] for k in obj)
            
            
    def __add__(self, obj):
        if type(obj) not in (DictList, dict):
            raise TypeError(f"DictList.__add__: operator + is not supported with {type(obj)}")
        new_dict = DictList(*tuple(self.dl.copy()))
        if type(obj) is dict:
            new_dict.dl.append(obj.copy())
        else:
            new_dict.dl += obj.dl.copy()
        return new_dict
            
    def __radd__(self, obj):
        if type(obj) not in (DictList, dict):
            raise TypeError(f"DictList.__add__: operator + is not supported with {type(obj)}")
        new_dict = DictList(obj.copy())
        new_dict.dl += self.dl.copy()
        return new_dict
            
            

            
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
