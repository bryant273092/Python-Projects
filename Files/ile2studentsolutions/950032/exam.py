from goody import type_as_str  # Useful in some exceptions
from _collections import defaultdict

class DictList:
    def __init__(self,*arges):
        self.dl = []
        assert len(arges) > 0
        for item in arges:
            assert type(item) is dict
            assert len(item) > 0
            self.dl.append(item)


    def __len__(self):
        result = []
        for d in self.dl:
            for k in d:
                if k not in result:
                    result.append(k)
        return len(result)

    def __repr__(self):
        return 'DictList(' 
    
    def __contains__(self,arg):
        for d in self.dl:
            if arg in d.keys() and type(arg) == str:
                return True
            return False
       
        
    def __getitem__(self,arg):
        a = defaultdict()
        for i in self.dl:
            for k,v in i.items():
                a[k] = v
        if arg not in a:
            raise KeyError
        else:
            return a[arg]
            
                    
    def __setitem__(self,key,value):
        a = defaultdict()
        for i in self.dl:
            for k,v in i.items():
                a[k] = v
        for k in a:
            if key not in k:
                self.dl.append({key:value})
    
    def __call__(self,arg):
        f = []
        for d in self.dl:
            if arg in d.keys():
                f.append((self.dl.index(d),d[arg]))
        return f
                
            
    def __iter__(self):
        a = defaultdict()
        for i in self.dl:
            for k,v in i.items():
                a[k] = v
    
    
    def __eq__(self,right):
        a = defaultdict()
        for i in self.dl:
            for k,v in i.items():
                a[k] = v
        if type(right) == DictList:
            for d in right:
                for k,v in d.items():
                    for k2,v2 in a.items():
                        if k == k2 and v == v2:
                            return True
                        else:
                            return False
        elif type(right) == dict:
            if right.keys() == a.keys():
                for k in right:
                    for k2 in a:
                        if right[k] == a[k2]:
                            return True
                        else:
                            return False
            else:
                return False
        else:
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
