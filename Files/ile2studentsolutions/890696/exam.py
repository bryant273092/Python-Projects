from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *dicts):
        self.dl = []
        
        assert len(dicts) > 0, "DictList.__init__: you must specify at least one dictionary"
        
        for d in dicts:
            assert type(d) == dict, f"DictList.__init__: '{d}' is not a dictionary"
            
            self.dl.append(d)
            
            
    def __len__(self):
        key_set = set()
        
        for d in self.dl:
            for k in d.keys():
                key_set.add(k)
                
        return len(key_set)
    
    
    def __repr__(self):
        return f"DictList(*{self.dl})"
    
    
    def __contains__(self, s):
        for d in self.dl:
            for k in d.keys():
                if k == s:
                    return True
                
        return False
    
    def __getitem__(self, k):
        for d in self.dl[::-1]:
            if k in d:
                return d[k]
            
        raise KeyError(f"DictList.__getitem__: '{k}' not in DictList")
    
    
    def __setitem__(self, k, v):
        for d in self.dl[::-1]:
            if k in d:
                d[k] = v
                return
            
        self.dl.append({k:v})
        
        
    def __call__(self, k):
        return_list = []
        
        for i in range(len(self.dl)):
            if k in self.dl[i]:
                return_list.append((i, self.dl[i][k]))
                
        return return_list
    
    
    def __iter__(self):
        used_keys = set()
        
        def tup_gen():
            for d in self.dl[::-1]:
                for k, v in sorted(d.items()):
                    if k not in used_keys:
                        yield (k, v)
                        
                        used_keys.add(k)
                
        return tup_gen()
    
    
    def __eq__(self, right):
        if type(right) == DictList:
            if len(self) != len(right):
                return False
            
            for k, v in right:
                if k not in self:
                    return False
                
                else:
                    if right[k] != self[k]:
                        return False
            
        elif type(right) == dict:
            if len(self) != len(right):
                return False
            
            for k in right.keys():
                if k not in self:
                    return False
                
                else:
                    if right[k] != self[k]:
                        return False
        
        else:
            raise TypeError(f"DictList.__eq__: a '{type_as_str(right)} cannot be compared to a DictList'")
        
        
        return True
    
    
    def __add__(self, right):
        if type(right) == DictList:
            dict1 = {}
            dict2 = {}
            
            for k, v in self:
                dict1[k] = v
            
            for k, v in right:
                dict2[k] = v
                
            return DictList(dict1, dict2)
        
        elif type(right) == dict:
            copy_dl = [dict(d) for d in self.dl]
            
            new_dl = copy_dl + [dict(right)]
            
            return DictList(*new_dl)
        
        
        else:
            raise TypeError(f"DictList.__eq__: a '{type_as_str(right)} cannot be compared to a DictList'")
            
            
    def __radd__(self, left):
        if type(left) == dict:
            copy_dl = [dict(d) for d in self.dl]
            
            new_dl = [dict(left)] + copy_dl
            
            return DictList(*new_dl)
        
        
        else:
            raise TypeError(f"DictList.__eq__: a '{type_as_str(left)} cannot be compared to a DictList'")
    
    
    
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test

    d = DictList({"a":1, "b": 1}, {"b":"asdfas", "c":4})
    for k, v in d:
        print(f"{k} -> {v}")


    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
