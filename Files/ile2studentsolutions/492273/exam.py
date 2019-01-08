from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        #if type(args) == None:
            #raise AssertionError ()
        for arg in args:
            if type(arg) != dict:
                raise AssertionError ("DictList.__init__: arg is not a dictionary")
            self.dl.append(arg)
    
    def __len__(self):
        count = 0
        key_list = []
        for dicts in self.dl:
            for key in dicts.keys():
                if key not in key_list:
                    key_list.append(key)
        count += len(key_list)

        return count
 
    def __repr__(self):
        return "DictList({})"

    def __contains__(self, k):
        for dicts in self.dl:
            if k in dicts.keys():
                return True
        
    def __getitem__(self, k):         
        for dicts in self.dl:
            if k in dicts:
                return dicts[k]
            else:
                raise KeyError("DictList.__getitem__: key is not in any dictionary") 
    
    def __setitem(self, k, v):
        for dicts in self.dl:
            if k in dicts:
                dicts[k] = v
            else:
                new_dict= {}
                new_dict[k] = v
                self.dl.append(new_dict)   
    
    def __call__(self, k):
        tuple_list = []
        for dicts in self.dl:
            if k not in dicts:
                return []
            #else:
                #for x in range(self.dl):
                #tuple_list.append()
                
    #def __eq__(self, right):
        #for d in self.dl:
            #for dict in right.dl:
                
            
            
            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    ##d0 = dict(a=1,b=2,c=3)
    #DictList(d0)
    #DictList.__len__(d0)

    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
