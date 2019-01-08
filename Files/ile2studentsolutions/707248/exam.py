from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        assert len(args) > 0, 'The parameters given are not dictionaries'
        assert all(type(arg) is dict for arg in args), 'The parameters given are not dictionaries'
            
        self.dl = [arg for arg in args]
       
        
    def __len__(self):
        count = set()
        for d in self.dl:
            for key in d:
                count.add(key)
        return len(count)


    def __repr__(self):
        return 'DictList(' + ', '.join(str(d) for d in self.dl) + ')'
    
    
    def __contains__(self,k):
        for d in self.dl:
            for key in d:
                if k == key:
                    return True
                
        return False
    
    
    def __getitem__(self,k):
        answer = None
        for d in self.dl:
            for key in d:
                if k == key:
                    answer = d[k]
                    
        if answer == None:
            raise KeyError("'"+ str(answer) +"'"+ 'appears in no dictionaries.')
        
        return answer
                    
    
    def __setitem__(self,k,v):
        new = dict()
        for d in enumerate(self.dl):
            i, d2 = d
            for key in d:
                if k in d2:
                    d2[k] = v
                else:
                    new[k] = v
                    self.dl.append(new)
                    
     
    def __call__(self,k):
        tup_l = []
        for d in enumerate(self.dl):
            i, d2 = d
            for key in d2:
                if k == key:
                    tup_l.append((i,d2[k]))
                    
        return tup_l
                               
 
    def __iter__(self):
        answer = set()
        for d in self.dl:
            for k,v in sorted(d.items()):
                answer.add((k,v))

        yield answer
     
     
    def __eq__(self,right):
        for d in self.dl:
            for key in d:
                if type(right) is DictList:
                    return DictList.__getitem__(self,key) == DictList.__getitem__(right,key)
                elif type(right) is dict:
                    return DictList.__getitem__(self,key) == right[key]
                else:
                    raise TypeError('Cannot compare the two objects, different data types.')
                        

            
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
