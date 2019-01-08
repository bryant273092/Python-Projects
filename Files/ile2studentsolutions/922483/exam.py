from goody import type_as_str  # Useful in some exceptions
from prompt import for_value

class DictList:
    def __init__(self, *args):
        if len(args) == 0: raise AssertionError
        self.dl = []
        for arg in args:
            if type(arg) != dict: raise AssertionError(f'DictList.__init__: {repr(arg)} is not a dictionary')
            self.dl.append(arg)
            
    def __len__(self):
        distinct_keys=[]
        for i in self.dl:
            for k in i.keys():
                if k not in distinct_keys:
                    distinct_keys.append(k)
        return len(distinct_keys)
    
    def __repr__(self):
        return f"DictList({', '.join([str(d) for d in self.dl])})"
    
    def __contains__(self,item):
        for i in self.dl:
            if item in i.keys():
                return True
        return False
    
    def __getitem__(self,key):
        if not self.__contains__(key): raise KeyError(f"{repr(key)} appears in no dictionaries")
        k=''
        for i in self.dl:
            if key in i.keys():
                k=i[key]
        return k
    
    def __setitem__(self,key,val):
        if not self.__contains__(key):
            self.dl.append({key: val})
        else:
            for i in reversed(self.dl):
                if key in i.keys():
                    i[key] = val
                    break
                
    def __call__(self,key):
        if not self.__contains__(key): return []
        l=[]
        for i in range(len(self.dl)):
            if key in self.dl[i].keys(): l.append((i,self.dl[i][key]))
        return l
    
    def __iter__(self):
        distinct_keys=[]
        for i in self.dl:
            for k in i.keys():
                if k not in distinct_keys:
                    distinct_keys.append(k)
        return iter(sorted([(i,self.__getitem__(i))for i in distinct_keys], key=lambda x: (x[0],x[1])))
    
    def __eq__(self, r):
        if '.DictList' in type_as_str(r) or type(r) is dict:
            distinct_keys_l=[]
            for i in self.dl:
                for k in i.keys():
                    if k not in distinct_keys_l:
                        distinct_keys_l.append(k)
            distinct_keys_r=[]
            if '.DictList' in type_as_str(r):
                for i in r.dl:
                    for k in i.keys():
                        if k not in distinct_keys_r:
                            distinct_keys_r.append(k)
            else:
                for k in r.keys():
                    if k not in distinct_keys_r:
                        distinct_keys_r.append(k)
            if sorted(distinct_keys_l) != sorted(distinct_keys_r): return False
            for key in distinct_keys_l:
                if self.__getitem__(key) != r.__getitem__(key):
                    return False
            return True
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
