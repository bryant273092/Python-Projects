from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        if len(args) == 0 or any(type(dic) is not dict for dic in args):
            raise AssertionError("DictList.__init__:Argument includes data that is not a dictionary")
        self.dl = list(args)
        

    
    def __len__(self):
        length = set()
        for dic in self.dl:
            for k in dic: 
                length.add(k)
        return len(length)
    
    def __repr__(self):
        return 'DictList('+','.join(str(dic) for dic in self.dl) + ")"
    
    def __contains__(self,k):
        return any(k in dic for dic in self.dl)
    
    def __getitem__(self,k):
        for dic in self.dl[::-1]:
            if k in dic:
                return dic[k]
        raise KeyError(f"DictList.__getitem__: could not locate key {k} in {self}")
    
    def __setitem__(self,k,v):
        for dic in self.dl[::-1]:
            if k in dic:
                dic[k] = v
                return
        self.dl.append({k:v})
    
    def __call__(self,k):
        answer = []
        for dic in enumerate(self.dl):
            if k in dic[1]:
                answer.append((dic[0],dic[1][k]))
        return answer
        
    def __iter__(self):
        def gen(adict):
            key_hist = set()
            for dic in adict[::-1]:
                for k in sorted(dic):
                    if k not in key_hist:
                        key_hist.add(k)
                        yield (k,dic[k])
        return gen(list(self.dl))
                        
                 
    
    def __eq__(self,right):
        if type(right) not in (DictList,dict):
            raise TypeError("DictList.__eq__:Right operand must be of type DictList or dict, is of type " + type_as_str(right))
        
        selfkeys = set([k for dic in self.dl for k in dic])
        if type(right) is dict:
            rightkeys = set([k for k in right])
        elif type(right) is DictList:
            rightkeys = set([k for dic in right.dl for k in dic])
        
        if selfkeys == rightkeys:
            for selfk,rightk in zip(selfkeys,rightkeys):
                if self[selfk] != right[rightk]:
                    return False
        else:
            return False
        return True
    
    def __add__(self,right):
        if type(right) not in (DictList,dict):
            raise TypeError("DictList.__add__:Right operand must be of type DictList or dict, is of type " + type_as_str(right))
        
                
        if type(self) in (DictList,dict):
            if type(self) is dict:
                selfdict = self
            else:
                selfdict = dict()
                for dic in self.dl:
                    for k,v in dic.items():
                        selfdict[k] = v
                
                
        if type(right) is DictList:
            rightdict = dict()
            for dic in right.dl:
                for k,v in dic.items():
                    rightdict[k] = v
            print(selfdict,rightdict)
            return DictList(selfdict,rightdict)
        
        elif type(right) is dict:
            selfdictlist = []
            for dic in self.dl:
                selfdictlist.append(dict(dic))
            return DictList(*selfdictlist,dict(right))
    
    
    def __radd__(self,left):

        if type(left) not in (dict,DictList):
            raise TypeError("DictList.__eq__:Left operand must be of type DictList or dict, is of type " + type_as_str(left))
        if type(left) is DictList:
            return self + left
        else:
            return DictList.__add__(left, self) # dict in self arg, DictList in right arg
        
        
        





            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d1 = DictList(dict(a=1,b=2),dict(b=12,c=13))
    d2 = DictList(dict(a = 'one',b = 'two'),dict(b='twelve',c='thirteen'))
    #print(d1+d2)
    #print(d2+d1)
    
    adl = DictList(dict(a=1,b=2),dict(b=12,c=13))
    adict = dict(a='one',b = 'two')
    #print(adl+adict)
    
    adl = DictList(dict(a=1,b=2),dict(b=12,c=13))
    adict = dict(a='one',b='two')
    #print(adict + adl)
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
