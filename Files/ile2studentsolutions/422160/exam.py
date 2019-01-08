from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl = []
        for dicts in args:
            self.dict = dicts
            assert type(self.dict) is dict,\
                'AssertionError(DictList.__init__:'+str(args)+'is not a dictionary)'
            self.dl.append(self.dict)
    
    def __len__(self):
        myset = set()
        for dicts in self.dl:
            for k in dicts.keys():
                myset.add(k)
        return len(myset)
    
    def __repr__(self):
        return str(self.dl)
    
    def __contains__(self,i):
        for dicts in self.dl:
            if i in dicts.keys():
                return True
    
#    def __getitem__(self,i):
#        for dicts in self.dl:
#    
#    def __setitem__(self,i):
#        
    def __call__(self,i):
        for dicts in self.dl:
            for k,v in dicts.items():
                if i == k:
                    return (k)
        
        
            

            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d= DictList(dict(a=1,b=2,c=3), dict(c=13,d=14,e=15), dict(e=25,f=26,g=27))
#    print(d)
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
