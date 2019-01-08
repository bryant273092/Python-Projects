# Submitter: jveloria(Veloria, Joshua)

from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *kargs):
        self.dl = []
        if len(kargs)==0:
            raise AssertionError
        for karg in kargs:
            if type(karg)==dict:
                self.dl.append(karg)
            else:
                raise AssertionError
            
    def __len__(self):
        result = set()
        for d in self.dl:
            for k,v in d.items():
                result.add(k)
        return len(result)
    
    def __repr__(self):
        return 'DictList('+','.join(str(d) for d in self.dl)+')'
    
    def __contains__(self,item):
        for d in self.dl:
            if item in d:
                return True
        return False
    
    def __getitem__(self,item):
        results = set()
        t=False
        for d in self.dl:
            if item in d:
                t=True
        if t:
            for d in self.dl:
                for k,v in d.items():
                    if item==k:
                        results.add(v)
            return max(results)
        else:
            raise KeyError

    def __setitem__(self,item,value):
        t=False
        for d in self.dl:
            if item in d:
                t=True
        if t:
            for d in self.dl:
                for k,v in d.items():
                    if self[item]==v:
                        d[item] = value
        else:
            self.dl.append({item:value})
    
    def __call__(self,item):
        result=[]
        for i,d in enumerate(self.dl,0):
            for k,v in d.items():
                if item==k:
                    result.append((i,v))
        return result
    
    def __iter__(self):
        remember = set()
        for d in self.dl[::-1]:
            for k,v in d.items(): 
                if k not in remember:
                    yield (k,v)
                remember.add(k)
    
    def __eq__(self,right):
        if type(right)==DictList:
            remember = set()
            for d in self.dl:
                for k,v in d.items():
                    remember.add(k)
            for d in right.dl:
                for k,v in d.items():
                    if k not in remember:
                        return False
            for r in remember:
                if self[r]!=right[r]:
                    return False
            return True
        elif type(right)==dict:
            remember = set()
            for d in self.dl:
                for k,v in d.items():
                    remember.add(k)
            for r in remember:
                if r not in right:
                    return False
                for k,v in right.items():
                    if r==k and self[r]!=right[k]:
                        return False
            return True
        else:
            raise TypeError
        
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test

    #t = [1,2,3]
    #print(t[::-1])
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
