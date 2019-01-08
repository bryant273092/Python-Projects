from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self,*args):
        if len(args) ==0:
            raise AssertionError('empty argument')
        for i in args:
            if type(i) != dict:
                raise AssertionError(f"DictList.__init__:{i} is not a dictionary")
            self.dl = list(args)
    
    def __len__(self):
        key_set = set()
        for d in self.dl:
            for k in d:
                key_set.add(k)
                
        return len(key_set)
    def __repr__(self):
        result = "DictList("
        for d in self.dl:
            result += repr(d)
            result += ','
        else:
            result.rstrip(',')
            result+= ')'
        return result
    
    def __contains__(self,key):
        for d in self.dl:
            if key in d:
                return True
        else:
            return False
    
    def __getitem__(self,key):
        
        k_in = False
        for d in self.dl:
            if key in d:
                k_in = True
                break
            
        if k_in == False:
            raise KeyError(f"{key} appears in no dictionaries")
        
        
        result = list()
        
        for d in self.dl:
            
            if key in d:
                result.append(d[key])
        else:
            return result[-1]
    
    def __setitem__(self,key,value):
        
        if key not in self:
            self.dl.extend([{key:value}])
        else:
            d_index = None
            
            for i in range(len(self.dl)):
                
                if key in self.dl[i]:
                    d_index = i
            else:
                self.dl[d_index][key] = value 
    
    
    def __call__(self,key):
        
        if (key in self) == False:
            return []
        else:
            result = list()
            
            
            for i in range(len(self.dl)):
                
                if key in self.dl[i]:
                    result.append((i,self.dl[i][key]))            
        return result 
    
    def __iter__(self):
        def gen(dl):
            
            copy_l = dl[::-1]
            
            history = set()
            
            for d in copy_l:
                for k in sorted(d):
                    if k not in history:
                        yield (k,d[k])
                        history.add(k)

                     
        return gen(self.dl)
                         
                    
    def __eq__(self,dict_l):
        if type(dict_l) !=  DictList and type(dict_l) != dict :
            raise TypeError('not a dict oject')
        
        if type(dict_l) == DictList:
            
            if len(dict_l) != len(self):
                return False
            
            d_check = {}
            for d in self.dl:
                d_check.update(d)
                
            for k in d_check:
                    
                if k not in dict_l:
                    return False
                    
                    
                if  dict_l[k] != self.__getitem__(k):
                    return False
                    
            else:
                return True

            
        elif type(dict_l) == dict:
            
            for d in self.dl:
                
                for k in d:
                    
                    if k not in dict_l:
                        return False
                    
                    if  dict_l[k] != self.__getitem__(k):
                        return False
                else:
                    return True            
            
            
        
        
        
        
            



            
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
