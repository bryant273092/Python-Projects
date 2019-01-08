from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        if len(args) == 0:
            raise AssertionError
        dlist = []
        for i in args:
            if not isinstance(i,dict):
                raise AssertionError

        for i in args:
            dlist.append(i)
        self.dl = dlist
                   
    def __len__(self):
        ans = []
        for i in self.dl:
            d = i.keys()
            ans.extend(list(d))
        a = set(ans)
        return len(a)
    
    def __repr__(self):
        s = tuple(self.dl)
        return "DictList" + str(s)


    def __contains__(self,k):
        ans = []
        for i in self.dl:
            d = i.keys()
            ans.extend(list(d))
        a = set(ans)
        if k in a:
            return True
        else:
            False
    
    def __getitem__(self,k):
        ans = []
        res = []
        for i in self.dl:
            d = i.keys()
            ans.extend(list(d))
        a = set(ans)
        if k not in a:
            raise KeyError
        else:
            for j in self.dl:
                for h in j.keys():
                    if k == h:
                        f = j[k]
                        res.append(f)
        return max(res)
        
    def __setitem__(self,k,v):
        ans = []
        res = []

        for i in self.dl:
            d = i.keys()
            ans.extend(list(d))
        a = set(ans)
        if k in a:
            for j in self.dl:
                for h in j.keys():
                    if k == h:
                        f = j[k]
                        res.append(f)
            b = max(res)

            for j in self.dl:
                for h in j.keys():
                    f = j.get(h,"a")
                    if f == b:
                        j[h] = v
        else:
            self.dl.append({k:v})
                        
    def __call__(self,k):
        
        ans = []
        l = []
        a = enumerate(self.dl,0)
        for m,n in a:
            ans.append(tuple((m,n)))
            for c in n.keys():
                if k == c:
                    res = n[k]
                    l.append(tuple((m,res)))
        return l
    def __iter__(self):
        res = []
        ans = []
        c = []
        p = []
        for i in self.dl[-1::-1]:
    
            k = sorted(i)
            for j in k:
                d = (j,i[j])
                res.append(d)
        ans.extend(res)
        for i in ans:
            if i[0] not in p:
                p.append(i[0])
                
                c.append(i)
            else:
                None
        for l in c:
            yield l
            
    
    def __eq__(self,right):
        ansl = []
        ansr = []
        ll = []
        kk = []
        for i in self.dl:
            d = i.keys()
            ansl.extend(list(d))
        a = set(ansl)
        if type(right) == dict:
            for i in right.keys():
                ansr.append(i)
            b = set(ansr)


            for q in a:
                for w in b:
                    
                    if a == b and q == w and self.__getitem__(q) == right[w]:
                        kk .append(right[w])
                        if len(kk) == 1:
                            return True
                        else:
                            return False
                     
                    else:
                        return False
          
        elif type(right) == DictList:
            s = []
#            print(right)
            for f in right:
                s.append(f[0])
            qw = set(s)
#            print(qw)
#            print(a)
            if qw == a:
                
                for z in right:
                    for k in a:
                    
                        if z[0] == k:
                            if z[1] == self.__getitem__(k):
                                ll.append(True)
                            else:
                                ll.append(False)
                if all(ll):
                    return True
                else:
                    return False              
            else:
                return False
        else:
            raise TypeError("wrong type")
        
            
        
    
                
                    
                      
        


            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d0 = dict(a=1,b=2,c=3)
    d1 = dict(c=13,d=14,e=15)
    d2 = dict(e=25,f=26,g=27)
    d  = DictList(d0,d1,d2)
    d['x'] = 'new5'

    d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    d2 = DictList(dict(a=1,b=12), dict(c=13))
  
    '''  
            for i in right:
                print("i",i)
                p = i.keys()
                ansr.extend(list(p))
            b = set(ansr)
            for q in a:
                for w in b:
                    if q == w and self.__getitem__(q) == self.__getitem__(w):
                        return True
                    else:
                        return False
    '''  
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
