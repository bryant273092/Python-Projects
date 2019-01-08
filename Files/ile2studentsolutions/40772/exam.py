from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *arg):
        self.dl = []
        if len(arg) < 1:
            raise AssertionError
        for i in arg:
            if type(i) is dict and len(i) > 0:
                self.dl.append(i)
            else:
                raise AssertionError
    
    
    def __len__(self):
        l = []
        for d in self.dl:
            for k in d.keys():
                if k not in l:
                    l.append(k)
        
        return len(l)
    
    
    def __repr__(self):
        return "DictList({})".format(', '.join(str(d) for d in self.dl))
    
    
    def __contains__(self, arg):
        for d in self.dl:
            if arg in d.keys():
                return True
    
    
    def __getitem__(self, arg):
        for d in self.dl:
            if arg in d.keys():
                return d[arg]
        raise KeyError("\'{}' appears in no dictionaries".format(arg))
    
    
    def __setitem__(self, key, value):
        for d in self.dl:
            if key in d.keys():
                d[key] = value
            if key not in d.keys():
                d[key] = value
                
    
    def __call__(self, arg):
        for d in self.dl:
            if arg in d.keys():
                return [list(d.keys().index(arg), d[arg])]
            if arg not in d.keys():
                return []
    
    def __iter__(self):
        for d in self.dl:
            yield (d.key(),d.value)
    
    def __eq__(self,left,right):
        if left.keys() == right.keys():
            return True
        
    
    


            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test

    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
    driver.default_show_exception=True
    driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()
