from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl=[]
        assert len(args)>0,'DictList.__init__: there is not dict in the argument'
        for a in args:
            assert type(a) is dict, 'DictList.__init__: '+repr(a)+' is not a dictonary'
            self.dl.append(a)
    
    def __len__(self):
        count=[]
        for d in self.dl:
            for k in d:
                if k not in count:
                    count.append(k)
        return len(count)
    
    def __repr__(self):
        dl_str=''
        for d in self.dl:
            dl_str+=str(d)+','
        return "DictList({})".format(dl_str.rstrip(','))
    
    def __contains__(self,item):
        judge=False
        for d in self.dl:
            for k in d:
                if k==item:
                    judge=True
        return judge
        
    def __getitem__(self,item):
        if item not in self:
            raise KeyError('DictList.__getitem__: KeyError: '+repr(item))
        result=0    
        for d in self.dl:
            for k,v in d.items():
                if k==item:
                    result=v
        return result   
    
    def __setitem__(self,item,value):
        if item in self:
            index=0
            for i in range(len(self.dl)):
                for k in self.dl[i]:
                    if k==item:
                        index=i
            self.dl[index][item]=value
        else:
            self.dl.append({item:value})  
            
    def __call__(self,item):
        if item not in self:
            return []
        else:
            result=[]
            for i in range(len(self.dl)):
                for k,v in self.dl[i].items():
                    if k==item:
                        result.append((i,v))
            return result
        
    def __iter__(self):
        key=[]
        result=[]
        for d in reversed(self.dl):
            dl=[]
            for k,v in d.items():
                if k not in key:
                    dl.append((k,v))
                    key.append(k)
            result.append(sorted(dl))
        for x in result:
            for y in x:
                yield y

    def __eq__(self,right):
        if type(right) not in [DictList,dict]:
            raise TypeError('DictList.__eq__: TypeError: '+repr(right))
        else:
            if type(right) is DictList:
                dl1={k:v for (k,v) in self}
                dl2={k:v for (k,v) in right}
                return dl1==dl2
            else:
                dl={k:v for (k,v) in self}
                return dl==right
                    
    def __add__(self,right):
        if type(right) is DictList:
            return DictList({k:v for (k,v) in self}.copy(),{k:v for (k,v) in right}.copy())   
        elif type(right) is dict:
            return DictList(*(d.copy() for d in self.dl),right.copy())   
        else:
            raise TypeError('DictList.__add__: TypeError: '+repr(right)) 
    
    def __radd__(self,left):
        if type(left) is DictList:
            return DictList({k:v for (k,v) in left}.copy(),{k:v for (k,v) in self}.copy())   
        elif type(left) is dict:
            return DictList(left.copy(),*(d.copy() for d in self.dl))   
        else:
            raise TypeError('DictList.__radd__: TypeError: '+repr(left))                  
                    

            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    adict = dict(a='one',b='two')
    d=d1+adict
    d1['b']='x'
    print(d1)
    print(d)
    
    


    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
