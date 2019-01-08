from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl = []
        if len(args) < 1:
            raise AssertionError('DictList.__init__: there\'s no dict')
        for d in args:
            if type(d) != dict: 
                raise AssertionError('DictList.__init__: it is not a dictionary.')
            self.dl.append(d)
           
    def __len__(self):
        count = 0
        for d in self.dl:
            for key in d:
                count += 1   
        return count
    
    def __repr__(self):
        return 'DictList({})'.format(','.join(str(d) for d in self.dl))
    
    def __contains__(self,key):
        for d in self.dl:
            if key in d:
                return True
            
            
    
    def __getitem__(self,k):
        
        if not self.__contains__(k):
            raise KeyError('{} appears in no dictionary.'.format(k))
        values = []    
        for d in self.dl:
            if k in d:
                values.append(d[k])
        return values[-1]
             
                    
            
    
    def __setitem__(self,k,v):
        if self.__contains__(k):
            for d in self.dl:
                d[k] = v
                
    def __call__(self,k):
        answer = []
        for d in self.dl:
            if k in d:
                answer.append((self.dl.index(d),d[k]))
        return answer
    
    def __iter__(self):
        pass
    
    def __eq__(self,right):
        if type(right) is DictList or type(right) is dict:
            for d in right.dl:
                return [d.keys()] == [d.keys() for d in self.dl]
                
            
        

        
                
            
            
                
                
            
            
 
                
            




            
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
