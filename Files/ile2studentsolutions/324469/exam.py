from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        for arg in args:
            if type(arg) == dict or type(arg) == DictList:
                self.dl.append(arg)
            else:
                raise AssertionError('DictList.__init__:' +"'"+arg+"'"+'is not a dictionary')
            
    def __len__(self):
        le = set()
        for dic in self.dl:
            for key in dic.keys():
                le.add(key)
        lk = sorted(le)
        return len(lk)
    
    def __repr__(self):
        lk = ''
        for dic in self.dl:
            lk += str(dic)+','
        return 'DictList('+lk+')'
    
    def __contains__(self, item):
        for dic in self.dl:
            if item in dic.keys():
                return True
            else:
                return False
            
    def __getitem__(self, item):
        le = []
        for dic in self.dl:
            if item in dic.keys():
                le.append(dic[item])
                   
        return le[-1]
            
    def __setitem__(self, item, value):
        for dic in self.dl:
            if item in dic.keys():
                dic[item] = value
            else:
                self.dl.append({item:value})
    
    def __call__(self, item):
        le = []
        for dic in self.dl:
            if item in dic.keys():
                le.append((self.dl.index(item), dic[item]))
            else:
                return []
        
    
    def __eq__(self, item):
        it = []
        le = []
        if type(item) ==  dict or type(item) == DictList:
            for dic in self.dl:
                for key in dic.keys():
                    if key not in le:
                        le.append(key)
            for i in item:
                for key1 in i.keys():
                    if key1 not in it:
                        it.append(key1)
        else:
            raise TypeError
        if it == le:
            return True
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
