from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *d):
        assert len(d) >= 1
        for data in d:
            assert type(data) is dict
        self.dl = list(d)
    
    def __len__(self):
        return len({x for d in self.dl for x in d.keys()})
    
    def __repr__(self):
        line = "DictList("
        line += ', '.join(str(d) for d in self.dl) +')'
        return line
    
    def __contains__(self, key):
        for d in reversed(self.dl):
            if key in d:
                return True
    
    def __getitem__(self, key):
        for d in reversed(self.dl):
            if key in d:
                return d[key]
        else:
            raise KeyError
    
    def __setitem__(self, key, value):
        for d in reversed(self.dl):
            if key in d:
                d[key] = value
                return
        self.dl.append({key: value})
    
    def __call__(self, key):
        items = list()
        for x in range(len(self.dl)):
            if key in self.dl[x]:
                items.append((x, self.dl[x][key]))
        return items
                
    def __iter__(self):
        yielded = set()
        for d in reversed(self.dl):
            for k, v in d.items():
                if k not in yielded:
                    yield k, v
                    yielded.add(k)
    
    def __eq__(self, right):
        if type(right) is DictList:
            
            for d in reversed(self.dl):
                for k in d:
                    if k in right:
                        if d[k] == right.__getitem__(k):
                            return True
                        else:
                            return False
                    else:
                        return False
            
        
        elif type(right) is dict:
            for d in reversed(self.dl):
                for k in d:
                    if k in right:
                        if d[k] == right[k]:
                            return True
                        else:
                            return False
                    else:
                        return False
            
                
        else:
            raise TypeError
            



            
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
