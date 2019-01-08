from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *dicts):
        self.dl = []
        if len(dicts) == 0:
            raise AssertionError(f"DictList.__init__: argument must contain dictionaries")
        for d in dicts:
            assert type(d) is dict, f"DictList.__init__: '{d}' is not a dictionary"
            self.dl.append(d)
        
        
    def __len__(self):
        distinct_keys = set()
        for d in self.dl:
            for key in d:
                distinct_keys.add(key)
        return len(distinct_keys)
    
    
    def __repr__(self):
        return "DictList(" + ','.join([str(d) for d in self.dl]) + ")"
          
                  
    def __contains__(self, key):  
        for d in self.dl:
            for k in d:
                if key == k:
                    return True
        return False
    
        
    def __getitem__(self, key):
        if self.__contains__(key):
            for d in reversed(self.dl):
                for k,val in d.items():
                    if k == key:
                        return val
        else:
            raise KeyError(f"DictList.__getitem__: {key} not in any dictionary")
        
        
    def __setitem__(self, key, value):
        if self.__contains__(key):
            each = []
            for d in self.dl:
                if key in d:
                    each.append(d[key])
                else:
                    each.append(0)
            index = each.index(max(each))
            self.dl[index][key] = value
        else:
            self.dl.append({key:value})
            
            
    def __call__(self, key):
        results = []
        for i,d in enumerate(self.dl):
            for k,val in d.items():
                if k == key:
                    results.append((i,val))
        return results
    
    
    def __iter__(self):                
        new = {}
        for d in reversed(self.dl):
            for k,v in sorted(d.items()):
                if k not in new:
                    new[k] = v
                else:
                    if new[k]<v:
                        new[k] = v
        for n,v in new.items():
            yield (n,v)
            
    
    def __eq__(self, other):
        self_keys = set()
        other_keys = set()
        
        for d in self.dl:
            for key in d:
                self_keys.add(key)
        if type_as_str(other) != type_as_str(key):
            for d in other:
                other_keys.add(d[0])
        else:
            for d in other.dl:
                for key in d:
                    other_keys.add(key)

        if self_keys==other_keys:
            for k in self_keys:
                if self.__getitem__(k) == other.__getitem__(k):
                    return True
                else:
                    return False
        else:
            return False



            
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
