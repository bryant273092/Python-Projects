from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl=[]
        for arg in args:
            assert type(arg) == dict,'DictList.__init__:{} is not a dictionary'.format(arg)
            self.dl.append(arg)
        assert self.dl !=[],'DictList.__init__:{} has no dictionary'.format(self.dl)
            
    def __len__(self):
        answer=set()
        for m in self.dl:
            for n in m.keys():
                answer.add(n)
        result = len(answer)
        return result
            
    def __repr__(self):
        return 'DictList('+','.join(str(i) for i in self.dl)+')'

    def __contains__(self,c):
        for i in self.dl:
            if c in i.keys():
                return True
    
    def __getitem__(self,k):
        
        for m in range(-1,-len(self.dl)-1,-1):
            for n in self.dl[m]:
                if n == k:
                    result = self.dl[m][n]
                    return result
        raise KeyError('DictList.__getitem__:{} appears in no dictionaries'.format(k))      
    
    def __setitem__(self,k,value):
        if k in self:
            while True:
                for m in range(-1,-len(self.dl)-1,-1):
                    for n in self.dl[m]:
                        if n == k:
                            self.dl[m][n] = value 
                            return None
        elif k not in self:
            temp_d = {k:value}
            self.dl.append(temp_d)
            
    def __call__(self,k):
        result = []
        for i in range(len(self.dl)):
            for j in self.dl[i]:
                if j == k:
                    result.append((i,self.dl[i][j]))
        return result
    
    def __iter__(self):
        temp_l = []
        for i in range(-1,-len(self.dl)-1,-1):
            for j in sorted(self.dl[i]):
                if j not in temp_l:
                    temp_l.append(j)
        for m in temp_l:
            yield(m,self[m])
    
    def __eq__(self,right):
        temp_left,temp_right = set(),set()
        
        if type(right) == dict:
            for i in self.dl:
                for j in i:
                    temp_left.add(j)
            for m in temp_left:
                if m not in right: 
                    return False
                if self[m] != right[m]:
                    return False
        elif type(right) == DictList:
            for i in self.dl:
                for j in i:
                    temp_left.add(j)
            for m in right.dl:
                for n in m:
                    temp_right.add(n)
            if temp_left!=temp_right:
                return False
            for i in temp_left:
                if self[i] != right[i]:
                    return False
        elif type(right) not in [dict,DictList]:
            raise TypeError('DictList.__eq__:{} is not a DictList or dict'.format(right))
        return True 
    
    def __add__(self,right):
        if type(right) == DictList:
            new = DictList(dict(self),dict(right))
            return new
        elif type(right) == dict:
            copy_D = self.copy()
            copy_d = right.copy()
            new = DictList(dict(copy_D),dict(copy_d))
            return new
        else:
            raise TypeError('DictList.__eq__:{} is not a DictList or dict'.format(right))
    
    def __radd__(self,left):
        return self.dl + left
           
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
