from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl=[]
        for i in args:
            assert type(i) is dict,f"{i} is not a dictionary"
            self.dl.append(i)
        assert self.dl !=[]
            
    def __len__(self):
        result=set()
        for i in self.dl:
            for j in i:
                result.add(j)
        return len(result)
    
    def __repr__(self):
        return f"DictList({','.join(str(i) for i in self.dl)})"

    def __contains__(self,c):
        for i in self.dl:
            for j in i:
                if c == j:
                    return True
        return False
    
    def __getitem__(self,k):
        for i in range(-1,-len(self.dl)-1,-1):
            for j in self.dl[i]:
                if k==j:
                    return self.dl[i][j]
        raise KeyError(f"{k} appears in no dictionaries")
    
    def __setitem__(self,k,value):
        if k in self:
            for i in range(-1,-len(self.dl)-1,-1):
                for j in self.dl[i]:
                    if k==j:
                        self.dl[i][j]=value
                        return
        else:
            self.dl.append({k:value})
            
    def __call__(self,k):
        result = []
        for i in range(len(self.dl)):
            for j in self.dl[i]:
                if k==j:
                    result.append((i,self.dl[i][j]))
        return result
    
    def __iter__(self):
        a=[]
        result=[]
        for i in range(-1,-len(self.dl)-1,-1):
            for j in sorted(self.dl[i]):
                if j not in a:
                    a.append(j)
        for i in a:
            result.append((i,self[i]))
        return iter(result)
    
    def __eq__(self,right):
        le=set()
        ri=set()
        for i in self.dl:
            for j in i:
                le.add(j)
        if type(right) == type(self):
            for i in right.dl:
                for j in i:
                    ri.add(j)
            if le!=ri:
                return False
            for i in le:
                if self[i] != right[i]:
                    return False
        elif type(right) is dict:
            for i in le:
                if i not in right or self[i] != right[i]:
                    return False
        else:
            raise TypeError(f"{right} is {type_as_str(right)} but can only be dictionary or DictList")
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
