from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl = []
        if len(args) == 0:
            raise AssertionError
        for elm in args:
            if type(elm) == dict:
                self.dl.append(elm)
            else:
                raise AssertionError
    
    def __len__(self):
        a = set()
        for item in self.dl:
            for elm in item.keys():
                a.add(elm)
        return len(a)
    
    def __repr__(self):
        ans = ''
        ans += ','.join(str(elm) for elm in self.dl)
        return 'DictList('+ans+')'
    def __contains__(self,key):
        b = []
        for a in self.dl:
            if key in a.keys():
                b.append(key)
        if len(b) != 0:
            return True
      
    def __getitem__(self,k):
        a = 0
        for d in self.dl:
            for key in d.keys():
                if key == k:
                    a = d[key]
        if a != 0:
            return a
        else:
            raise KeyError
        
    def __setitem__(self,key,val):
        for d in self.dl:
            try:
                d.__getitem__(key)
                d[key] = val
            except KeyError:
                self.dl.append({key: val})
    
    def __call__(self,key):
        i = 0
        ans = []
        for d in self.dl:
            if key in d.keys():
                ans.append((i,d[key]))
            i += 1
        return ans
    
    def __iter__(self):
        a = []
        for d in self.dl[::-1]:
            for k,v in sorted(d.items()):
                if k not in a:
                    yield k,v
                a.append(k)
    
    def __eq__(self,right):
        a = True
        if type(right) == DictList:
            for D in self.dl:
                for k in D.keys():
                    if D.__getitem__(k) == right.__getitem__(k):
                        a = True
                    else:
                        a = False
            return a
        elif type(right) == dict:
            for d in self.dl:
                for k in d.keys():
                    if d.__getitem__(k) == right.__getitem__(k):
                        a = True
                    else:
                        a = False
            return a
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
