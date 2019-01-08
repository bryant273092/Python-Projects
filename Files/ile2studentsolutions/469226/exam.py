from goody import type_as_str  # Useful in some exceptions
from operator import __getitem__

class DictList:
    def __init__(self,*args):
        self.dl = []
        if args:
            for arg in args:
                if type(arg) != dict:
                    raise AssertionError('input should be a dictionary')
    
                if type(arg) == dict:
                    self.dl.append(arg)
                else:
                    raise AssertionError('input must be dictionary')
        else:
            raise AssertionError('input must contain a dictionary')
        
    def __len__(self):
        l=[]
        for item in self.dl:
            for k in item.keys():
                if k not in l:
                    l.append(k)
        return len(l)
    
    def __repr__(self):
        result = ()
        for item in self.dl:
            result += (item,)
        
        return 'DictList{}'.format(result)
                    
    def __contains__(self, item):
        for d in self.dl:
            if item in d.keys():
                return True    
        return False 
    
    def __getitem__(self, index):
        for d in self.dl[::-1]:
            if index in d.keys():
                return d[index]
        raise KeyError('item is not in dictionary')
                
        
    def __setitem__(self, key,val):
        for d in self.dl[::-1]:
            if key in d.keys():
                d[key] = val
                break   
        self.dl.append({key:val})


    def __call__(self, item):
        result = []
        for d in self.dl:
            if item in d.keys():
                result.append((self.dl.index(d), d[item]))
        return result
                       
    def __iter__(self):
        iter_list = []
        for i in self.dl[::-1]:
            for k,v in i.items():
                if k not in iter_list:
                    iter_list.append(k)
                    yield (k,v)
            
    
    def __eq__(self,item2):
        result = True
        for d1 in self.dl:
            for k in d1.keys():
                if k in item2:
                    if d1[k] == item2[k]:
                        result = True
                    else:
                        result = False
                else:
                    result = False          
        return result 
                
            
                
    
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
