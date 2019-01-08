from goody import type_as_str  # Useful in some exceptions
from builtins import KeyError

class DictList:
    def __init__(self,*term):
        self.dl=[]
        assert len(term)!=0,'empty arguments '
        for t in term:
            assert type(t)==dict,'Dictlist.__init__ is not a dict'
            self.dl.append(t)
            
        
    def __len__(self):
        result=set()
        for di in self.dl:
            for k in di:
                result.add(k)
        return len(result)
        
    def __repr__(self):
        lst=[]
        for di in self.dl:
            lst.append(di)
        for i in range(len(lst)):
            return 'DictList('+str(lst[i])+','+')'
            #return 'DictList('+str(self.dl[i])+',)'
   
    def __contains__(self,k):
        for di in self.dl:
            return k in di
        return False
            
    
    def __getitem__(self,key):
        for d in self.dl:
            if key not in d:
                raise KeyError
            else:
                for i in range(len(self.dl)):
                    if key in self.dl[i]:
     
                        return self.dl[i][key]
    def __setitem__(self,key,value):
        for di in self.dl:
            if key in di:
                self.dl[key]=value 
            elif key not in di:
                self.dl[key]={}
                self.d[key]=value
    def __call__(self,key):
        lst=[]
        if key not in self.dl:
            return []
        for di in self.dl:
              if key in di:
                  result=tuple()
                  result.add(di[key])
                  lst.append(result)  
        return lst       
   
    
    def __iter__(self):
        pass
    def __eq__(self,right):
        if type(right) is not DictList:
            raise TypeError
    
        
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
