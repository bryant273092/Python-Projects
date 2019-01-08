from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        #print(args)
        #print(type(args))
        #print(list(args))
        
        for i in args:
            
            
            assert type(i) is dict,"DictList.__init__: "+ str(i)\
            +"is not a dictionary"
        
        
        self.dl=list(args)
        
        
    def __len__(self):
        #print(self.dl)
        l=[]
        for d in self.dl:
            #print(d)
            for k in d.keys():
                #print(k)
                l.append(k)
        
        return len(l)
        
    def __repr__(self):
        
        return "DictList("+','.join(str(i) for i in self.dl)+")"
    def __contains__(self,key):
        for d in self.dl:
            if key in d.keys():
                return True
        return False
    def __getitem__(self,key):
        for d in self.dl:
            if key not in d:
                raise KeyError(str(key)+"appears in no dictionaries")
            
            else:
                return self.dl[self.dl.index(d)][key]
    def __setitem__(self,key,value):
        for d in self.dl:
            if key in d:
                self.dl[self.dl.index(d)][key]=value
            else:
                
                self.dl.append({key:value})
    def __call__(self,key):
        for d in self.dl:
            if key not in d:
                return []
            else:
                return [tuple(self.dl.index(d),self.dl[self.dl.index(d)][key])]
        
            
    #def __iter__(self):  
        
    #def __eq__(self,right):
        



            
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
