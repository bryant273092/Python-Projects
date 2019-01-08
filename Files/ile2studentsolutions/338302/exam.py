from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self, *args):
        assert len(args) > 0
        self.dl = []
        for arg in args:
            assert type(arg) is dict, "DictList.__init__: '" + str(arg) + "' is not a dictionary"
            self.dl.append(arg)

    def __len__(self):
        
        unique = []
        for d in self.dl:
            for k,v in d.items():
                if k not in unique:
                    unique.append(k)
        return len(unique)
    
    
    def __repr__(self):
        
        return "DictList("+ ",".join(str(d) for d in self.dl) + ")"
    
    
    def __contains__(self,arg):
        
        for d in self.dl:
            for k,v in d.items():
                if arg == k:
                    return True
        return False
    
    
    def __getitem__(self, arg):
        
        keys = []
        vals = []
        
        for d in self.dl:
            for k,v in d.items():
                if k not in keys:
                    keys.append(k)
                if arg in d:
                    if k == arg:
                        c = v
                        vals.append(c)
        if arg not in keys:
            raise KeyError
        else:
            return max(vals)


    def __setitem__(self, key, val):
        
        keys = []
        vals = [0]
            
        for d in self.dl:
            for k,v in d.items():
                if k not in keys:
                    keys.append(k)
                if key in d:
                    if k == key:
                        c = v
                        vals.append(c)
        
        biggest_val = max(vals)     


            
        if key not in keys:
            not_in = {}
            not_in[key] = val
            self.dl.append(not_in)
                
        elif key in keys:
            
            for d in self.dl:
                for k,v in d.items():
                    if v == biggest_val:
                        d[key] = val
            
        
                    
            
    
    def __call__(self, arg):
        
        
        count_dict = -1
        tup = []
        for d in self.dl:
            count_dict += 1
            for k,v in d.items():
                if arg == k:
                    tup.append((count_dict,v))
        return tup
    
    
    def __iter__(self):
        
        for d in self.dl:
            for k, v in d.items():
                yield (k,v)
    
    def __eq__(self, right):
        
        k1 = []
        k2 = []
        v1 = []
        v2 = []
        
        
        for d in self.dl:
            for k,v in d.items():
                k1.append(k)
        
        print(right)      
        for r in right:
            for k,v in r.items():
                k2.append(k)
        if k1 == k2:
            for k in k1:
                for d in self.dl:
                    v1.append(d[k])
                for r in right:
                    v2.append(d[k])
            return v1 == v2
        else:
            return False
        
        
    def __add__(self,right):
        pass
        
                
             
            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test

    d = DictList({'a':1, 'b':2, 'c':3}, {'c':13,'d':14, 'e':15},{'e':25,'f':26,'g':27})
    print(d.dl)
    d['x'] = 'new'
    d['c'] = 'new'
    print(d)

    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
