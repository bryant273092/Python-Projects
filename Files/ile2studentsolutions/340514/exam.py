from goody import type_as_str  # Useful in some exceptions
#from _ast import arg

class DictList:
    def __init__(self, *args):
        for a in args:
            if type(a) != dict:
                raise AssertionError('DictList.__init__: Argument(s) not a dictionary')
        assert len(args) != 0, f"DictList.__init__: Must have at least one argument"
        
        self.dl = []
        for a in args:
            self.dl.append(a)
            
    def __len__(self):
        count = 0
        unique = set()
        for d in self.dl:
            for k in d.keys():
                unique.add(k)
        for _ in unique:
            count += 1
        return count
    
    def __repr__(self):
        result = "DictList("
        count = 0
        for each in self.dl:
            count += 1
            result += str(each)
            if count < len(self.dl):
                result += ", "
            else:
                result += ")"
        return result
    
    def __contains__(self, item):
        for d in self.dl:
            for k in d.keys():
                if k == item:
                    return True
                
    def __getitem__(self, item):
        options = []
        for d in self.dl:
            for k,v in d.items():
                if k == item:
                    options.append(v)
        if len(options) > 0:
            return max(options)
        else:
            raise KeyError('DictList.__getitem__: No keys found')
        
    def __setitem__(self, item, value):
        options = []
        for d in range(len(self.dl)):
            if item in self.dl[d]:
                for k,v in self.dl[d].items():
                    if k == item:
                        options.append(v)
                for o in options:
                    if o == max(options):
                        self.dl[d][item] = value
            else:
                x = {}
                x[item] = value
                self.dl.append(x)
        #add
        
    def __call__(self, item):
        result = []
        for d in range(len(self.dl)):
            if item in self.dl[d]:
                result.append((d, self.dl[d][item]))
        return result
         
    def __iter__(self):
        count = 0
        for d in range(len(self.dl)):
            if d == (len(self.dl) - count):
                for k,v in self.dl[d].items():
                    yield((k,v))
                count += 1
                
        
        
    def __eq__(self, right):
        if type(right) == dict:
            for d in self.dl:
                for k,v in self.dl[d].items():
                    if k in right:
                        if v == right[k]:
                            return True
        elif type(right) == DictList:
            for d in range(len(self.dl)):
                for k,v in self.dl[d].items():
                    if k == right[d]:
                        if v == right[d][k]:
                            return True     
                        
        else:
            raise TypeError("DictList.__eq__: Not a dict or DictList")
                    
    
                    




            
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
