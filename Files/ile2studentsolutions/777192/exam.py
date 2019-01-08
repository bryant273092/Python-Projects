from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *dic):
        if dic == dict():
            raise AssertionError
        for d in dic:
            if type(d) is not dict:
                raise AssertionError
        self.dl = []
        for d in dic:
            self.dl.append(d)
            #print('asdkfgawelifa',self.dl)
        
    def __len__(self):
        result = set()
        for d in self.dl:
            for k in d:
                result.add(k)
        return len(result)
    
    
    def __repr__(self):
        dict_str = ''
        for d in self.dl:
            dict_str + f'{d},'     
        return 'DictList('+ dict_str[:-1]+')'
    
    def __contain__(self,key):
        for d in self.dl:
            if key in d.keys():
                return True
        return False
    
    
    def __getitem__(self,key):
        result = []
        all_key = set()
        for d in self.dl:
            for k in d.keys():
                all_key.add(k)
        if key not in all_key:
            raise KeyError
        for d in self.dl:
            if key in d.keys():
                result.append(d[key])
        return result[-1]
    
    def __setitem__(self,k,v):
        for d in self.dl:
            if k in d.keys():
                d[k] = v

        
    def __call__(self,key):
        result = []
        for d in self.dl:
            if key in d.keys():
                result.append((self.dl.index(d),d[key]))
        return result
        
    def __iter__(self):
        check = []
        for d in self.dl[::-1]:
            for k,v in sorted(d.items(), key = lambda x:x[0]):
                if k not in check:
                    yield (k,v)
                    check.append(k)
                if k in check:
                    pass
                    
        
    
    def __eq__(self,right):
        if type(right) != DictList:
            raise TypeError
        for d in self.dl:
            if len(self.dl) != len(right.dl):
                return False
            for k in d.keys():
                if len(right.dl[k]) != len(self.dl[k]):
                    return False
        else:
            return True
        
            
            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test


    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#    driver.default_show_exception=True
#    driver.default_show_exception_message=True
#    driver.default_show_traceback=True
    driver.driver()
