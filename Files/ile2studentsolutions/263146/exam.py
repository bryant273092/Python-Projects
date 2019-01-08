from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*dictpar):
        assert dictpar
        lisst = []
        for d in dictpar:
            assert isinstance(d,dict)
            lisst.append(d)
        self.dl = lisst

    def __len__(self):
        dup = []
        for d in self.dl:
            for dkeys in d:
                if dkeys not in dup:
                    dup.append(dkeys)
        return len(dup)
            
    def __repr__(self):
        for d in self.dl:
            return 'DictList({0})'.format(d)

    def __contains__(self,check):
        for d in self.dl:
            if check in d:
                return True
        else:
            return False
            
    def __getitem__(self,item):
        for d in self.dl:
            if item in d:
                indexx = self.dl.index(d)
                return self.dl[indexx][item]
        else:
            raise KeyError("Not in DictList")
        
    def __setitem__(self,item,value):
        for d in self.dl:
            if item in d:
                d[item] = value
            else:
                new = {}
                new[item] = value
                self.dl.append(new)    
                
    def __call__(self,item):
        lisst = []
        for d in self.dl:
            if item in d:
                lisst.append((self.dl.index(d), d[item]))
        return lisst
        
    def __iter__(self):
        for d in sorted(self.dl):
            for k,v in sorted(d.items(), key = lambda x:x[0]):
                yield k,v
            
    def __eq__(self,right):
        if type(right) is DictList:
            for d in self.dl:
                for r in right.dl:
                    if r == d:
                        for k,v in r.items():
                            for key,val in d.items():
                                if r[k] == d[key]:
                                    return True
                                else:
                                    return False
                    else:
                        return False
        if type(right) == dict:
            for k,v in right.items():
                for d in self.dl:
                    if k in d:
                        return True
                    else:
                        return False 
        else:
            raise TypeError("needs to be dict")
            
            
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
