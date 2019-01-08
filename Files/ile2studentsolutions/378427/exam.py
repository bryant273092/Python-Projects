from goody import type_as_str  # Useful in some exceptions

class DictList:
     
    def __init__(self,*kargs):
        self.dl = []
        assert(len(kargs)!= 0)
        for karg in list(kargs):
            if type(karg) == dict:
                self.dl.append(dict(karg))
                
            else:
                raise AssertionError
            
    def __len__(self):
        answer = set()
        for v in self.dl:
            for key in v.keys():
                answer.add(key)
        return len(answer)

    def __repr__(self):
        return "DictList("+",".join(str(v) for v in self.dl)+")"

    def __contains__(self,item):
        for v in list(self.dl):
            for key in v.keys():
                if item == key:
                    return True
        return False
    
    def __getitem__(self,item):
        temp = None
        for v in list(self.dl):
            for key in v.keys():
                if key == item:
                    temp = v[key]
        if temp == None: raise KeyError
        return temp            
    
    def __setitem__(self,item,value):
        if item in self:
            for num in range(len(self.dl)):
                if item in list(self.dl[num].keys()) and all(item not in i.keys() for i in self.dl[num+1:]):
                    self.dl[num][item]=value                  
        else:
            self.dl.append({item:value})
        
                
    def __call__(self,item):
        answer = []
        for num in range(len(self.dl)):
            for key in self.dl[num].keys():
                if key == item:
                    answer.append((num,self.dl[num][key]))
        return sorted(answer,key=lambda t:t[0])
    
    def __iter__(self):
        copy_dl = self.dl.copy()[::-1]
    
        for num in range(len(copy_dl)):
            for v in sorted(copy_dl[num].keys()):
                if all(v not in i.keys() for i in copy_dl[num+1:]):
                    yield (v,self[v])
    
    def __eq__(self,right):
        if type(right) in [DictList,dict]:
            for v in self.dl:
                for i in v.keys():
                    if i not in right or self[i] != right[i]:
                        return False
            return True
        else:
            raise TypeError       
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    
    
    d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    d2 = DictList(dict(a=1,b=12), dict(c=13))
    
    print(d1 == dict(a=1,c=13))
    
    
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
