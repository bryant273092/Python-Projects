from goody import type_as_str  # Useful in some exceptions
from collections import defaultdict

class DictList:
    def __init__(self,*args):
        ls=[]
        for d in args:
            assert type(d)==dict,f"DictList.__init__:{d} is not a dictionary."
            ls.append(d)
        assert len(ls)>0,"DictList.__init__:No dictionary in parameter."
        self.dl=ls
    
    def __len__(self):
        s=set()
        for d in self.dl:
            for k in d:s.add(k)
        return len(s)
    
    def __repr__(self):
        ls=[str(d) for d in self.dl]
        return ("DictList("+",".join(ls)+")")
    
    def __contains__(self,key):
        for d in self.dl:
            for k in d:
                if k==key:return True
        return False
    
    def __getitem__(self,key):
        dd=defaultdict(list)
        for d in self.dl:
            for k in d:dd[k].append(d[k])
        try:return dd[key][-1]
        except:raise KeyError(f"DictList.__getitem__:{key} appears in no dictionaries")
    
    def __setitem__(self,_key,_value):
        ls=[]
        for n,d in enumerate(self.dl):
            if _key in d:ls.append(n)
        if len(ls)>0:self.dl[ls[-1]][_key]=_value
        else:self.dl.append({_key:_value})
                
    def __call__(self,_key):
        result=[]
        for n,d in enumerate(self.dl):
            if _key in d:result.append((n,d[_key],))
        return result
    
    def __iter__(self):
        added_key=set()
        for d in self.dl[::-1]:
            sorted_key=sorted(d.keys())
            for k in sorted_key:
                if k not in added_key: 
                    yield (k,d[k])
                    added_key.add(k)
    
    def __eq__(self,other):
        if type(other) not in [DictList,dict]:raise TypeError("DictList.__eq__:The other parameter is not a DictList or a dict type item.")
        if len(self)!=len(other): return False
        kl=set()
        for d in self.dl:
            for k in d:
                kl.add(k)
        return all([self[_key]==other[_key] for _key in kl])
    
    def __add__(self,other):
        def dl_to_d(dictlist):
            kl=set()
            for d in dictlist.dl:
                for k in d: kl.add(k)
            return {key:dictlist[key] for key in sorted(list(kl))}
        if type(other)==DictList:
            return DictList(dl_to_d(self),dl_to_d(other))
        elif type(other)==dict:
            copy_self=[d for d in self.dl]
            copy_dict={k:v for k,v in other.items()}
            return DictList(*copy_self,copy_dict)
        else:raise TypeError(f"DictList.__add__:The right operand is {type_as_str(other)}, needs to be a dict or a DictList.")
    
    def __radd__(self,other):
        if type(other)==dict:
            return DictList(other,*self.dl)
        else:
            return self.__add__(other)
#         
        
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    
    d1=DictList(dict(a=1,b=2,c=3),dict(c=13,d=14,e=15,a=0))
    print(d1.dl)
    print(len(d1))
    print(d1)
    print("k" in d1)
    print(d1["a"])
    d1["c"]="new"
    print(d1)
    d1["x"]="newX"
    print(d1)
    print(d1.__call__("c"))
    for i in d1:
        print(i)
    d2=DictList(dict(a=1,b=2,c=3),dict(c=13,d=14,e=15,a=0))
    d3=DictList(dict(a=1,b=2,c=3),dict(c=13,d=14,e=15,a=0))
    print(d2==d3)
    d4=DictList(dict(a=1,b=2),dict(b=12,c=13))
    d5=DictList(dict(a="one",b="two"),dict(b="twelve",c="thirteen"))
    print(d4+d5)
    print(d5+d4)
    dict6=dict(a="one",b="two")
    print(d4+dict6)
    print(dict6+d4)
    
    
    print("\n\n")
    d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    adict = dict(a='one',b='two')
    d = d1+adict
    print(d)
    d1['b'] = 'x'
    print(d)
    print(d["b"])
    adict["b"]="x"
    print(d["b"])
    
    adict['b'] = 'x'
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
    driver.default_show_exception=True
    driver.default_show_exception_message=True
    driver.default_show_traceback=True
    driver.driver()
