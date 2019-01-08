#from goody import type_as_str  # Useful in some exceptions
#from builtins import str

class DictList:
    def __init__(self, *args):
        self.dl = []
        if args == None:
            raise AssertionError("must provide dictionary argument.")
        for item in args:
            if type(item) == dict:
                self.dl.append(item)
            else:
                raise AssertionError('DictList.__init__: ' + str(dict) + ' is not a dictionary.')
                
                
    def __len__(self):
        whole = set()
        for dic in self.dl:
            for key in dic.keys():
                whole.add(key)
                
        return len(whole)
    
    def __repr__(self):
        pass
    
    def __contains__(self, item):
        for dic in self.dl:
            for key in dic.keys():
                if key == item:
                    return True
        
        return False
                
    def __getitem__(self,key):
        position = []
        for dic in self.dl:
            if key in dic.keys():
                position.append(dic[key])
                  
        if len(position) == 0:
            raise KeyError(str(key) + 'is not in any dictionary.')
        
        else:
            return position.pop()
        
    
    def __setitem__(self, key, value):
        for dic in sorted(self.dl, reverse = True):
            if key in dic.keys():
                dic[key] = value
                break
            else:
                new_dic = {}
                new_dic[key] = value
                self.dl.append(new_dic)
                
    def __call__(self, key):
        tuple_list = []
        counter = -1
        for dic in self.dl:
            counter += 1
            if key in dic.keys():
                tuple_list.append((counter,dic[key]))
                
        return tuple_list
    
    def __iter__(self):
        unsorted_keys = set()
        for dic in self.dl:
            for key in dic.keys():
                unsorted_keys.add(key)
        
        sorted_keys = sorted(list(unsorted_keys))
        
        for dic in sorted(self.dl, reverse = True):
            for key in sorted_keys:
                yield((key, dic[key]))
                
    '''            
    def __eq__(self, d1, d2):
        if type(d2) != DictList or dict:
            raise TypeError("can only compare between dicts or DictList")
        
        if type(d2) == DictList:
            d1key = []
            d2key = []
            for dic in d1:
                for key in dic.keys():
                    d1key.append(key)
            for dic in d2:
                for key in dic.keys():
                    d2key.append(key)
            return d1key == d2key
        
        if type(d2) == dict:
            
        '''       

    
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test


    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()
