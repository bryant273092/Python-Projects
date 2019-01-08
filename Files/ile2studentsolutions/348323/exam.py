from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *kwargs):
        self.dl = []
        assert kwargs is not tuple()
        for kwarg in kwargs:
            assert type(kwarg) is dict
            self.dl.append(kwarg)
            
            
    def __len__(self):
        seen = set()
        for d in self.dl:
            for k, _v in d.items():
                seen.add(k)
        return len(seen)
    
    def __repr__(self):
        final = 'DictList('
        for d in self.dl:
            final += str(d) +','
        final = final.rstrip(',')
        final += ')'
        return final
    
    def __contains__(self, item):
        counter = 0
        for d in self.dl:
            for k, _v in d.items():
                if k == item:
                    counter += 1
                if counter == 1:
                    return True
        if counter == 0:
            return False
    
    def __getitem__(self, item):
        final = []
        for d in self.dl:
            for k, v in d.items():
                if item == k:
                    final.append(v)
        if final == []:
            raise KeyError
        else:
            return final[-1]
        
    def __setitem__(self, key, value):
        final = []
        nums = []
        for d in self.dl:
            for k, v in d.items():
                final.append(k)
                if key == k:
                    nums.append(v)
        if key not in final:
            self.dl.append({key: value})
        elif key in final:
            d[key] = value
            
    
    def __call__(self, key):
        final = []
        counter = -1
        for d in self.dl:
            counter += 1
            for k, v in d.items():
                if key == k:
                    final.append((counter, v))
        return final
        
        
    def __iter__(self):
        final = []
        for d in self.dl:
            for k, v in d.items():
                final.append((k,v))
        return sorted(final)
                
                
    
    def __eq__(self, right):
        if type(right) not in [DictList, dict]:
            raise TypeError
        if type(right) is DictList:
            for d in self.dl:
                for _k, _v in d.items():
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
