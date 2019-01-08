from goody import type_as_str  # Useful in some exceptions


class DictList:
    def __init__(self, *adict):
        
        assert len(adict) > 0
        
        self.dl = []
        result = []
        temp = {}
        tempinner = {}
        for item in adict:
            assert type(item) is dict
       
        for item in adict:
            temp = {}
            for k,v in item.items():
           
                
          
                temp[k] = v
                
                
            self.dl.append(temp)
    
    
             
      
        print(self.dl)
        
    def __len__(self):
        counter = 0
        seen = []
        for i in self.dl:
            for k in i.keys():
                if k not in seen:
                    counter += 1
                    
                seen.append(k)
         
        return counter
                
                
            
            
           
    def __repr__(self):
        result = ''
        for i in self.dl:
            result+=str(i)
        
            
        return "DictList("+str(self.dl)+')'
    
    
        
    def __contains__(self, other):    
        for item in self.dl:
            for k in item.keys():
                if other == k:
                    return True
        return False     
        
    def __getitem__(self, other):
        result = None
        for item in self.dl:
            for k,v in item.items():
                if other == k:
                    result = v
        if result == None:
            raise KeyError
        return result
                

    def __setitem__(self,other, value):
        index = 0
    
        for item in reversed(self.dl):
            
           
            if other in item.keys():
                self.dl[index][other] = value
                return
             
            index += 1
#         counter = 0
#         for item in self.dl:
#             
#             if other not in item.keys():
#                 counter +=1
#         if counter == len(self.dl):

  
        self.dl.append({other: value})
            
    def __call__(self, other):
        result = []
        index = 0
        for i in self.dl:
            
            if other not in i.keys():
                pass
            else:
                for k,v in i.items():
                    result.append((index, v))
            index += 1
        return result
    
    def __eq__(self,other):
        pass
        
                
            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d = DictList({'a': 1, 'b':2 },{'a': 1, 'b':4 },{'r':3},{'t':3})
    print(len(d))
    print(d)
    d['a'] = 3
    print(d)

    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
