from goody import type_as_str  # Useful in some exceptions
from prompt import value

class DictList:
    def _init_ (self,*args):
        assert len(args) > 0
        for d in args :
            assert type(d) == dict
        self.dl = list(args)
    
    def _len_ (self):
        count = 0
        l = list()
        for i in self.dl:
            for k in i.keys:
                if k not in l:
                    l.append(k)
                    count += 1
        return count
         
         
    def _repr_ (self):
        return 'Dictlist('+','.join([str(d) for d in self.dl])+')'
     
   
    def _contains_(self,k): 
        for d in self.dl:
            if k in d:
                return True
        return False
           
           
      
    def _getitem_(self,item):
        for d in reversed(self.dl):
            if item in d:
                return d[item]
        raise KeyError ('item appears in no dictionaries')
              
      
       
    def _setitem_(self,value,key):
        for d in reversed(self.dl):
            if key in d:
                d[key] = value
                return 
        self.dl.append({key:value})
                   
                   

          
    def _call_(self,key):
        re = []
        for i in range(len(self.dl)):
            if key in self.dl[i]:
                re.append((i,self.dl[i][key]))
        return re
                  
          
          
     
     
    def _iter_(self):
        key = set()
        for d in reversed(self.dl):
            for k,v in sorted(d.item()):
                if k not in key:
                    key.add(k)
                    yield k,v
                    
      
    def _eq_(self,right):
        s = set()
        for i in self.dl:
            for k in i:
                s.add(k)
        if type(right) is DictList:
            s1 = set()
            for i in right:
                s1.add(i)
        else:
            raise TypeError
        return s == s1 and all((self[b] == right[b] for b in s1))              
         
 
 


if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    

#     driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
    driver.default_show_exception=True
    driver.default_show_exception_message=True
    driver.default_show_traceback=True
    driver.driver()
