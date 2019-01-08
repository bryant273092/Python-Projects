from goody import type_as_str  # Useful in some exceptions
from builtins import AssertionError

class DictList:
    def __init__(self, *kargs):
        self.dl = []
        if len(kargs) == 0:
            raise AssertionError
        
        for g in kargs:
            if type(g) != dict:
                raise AssertionError
            else:
                if len(g)>0:
                    self.dl.append(g)
        
        
        
                
    def __len__(self):
        g = 0
        z=[]
        for i in self.dl:
            for x in i:
                if x not in z:
                    z.append(x)
                    g+=1
        return g
    
    def __repr__(self):
        answer = 'DictList('
        for x in self.dl:
            answer+= str(x)+','
            
        answer = answer[:len(answer)-1]
        answer += ')'
        return answer
    
    def __contains__(self,right):
        for i in self.dl:
            for x in i:
                if x==right:
                    return True
        return False
    
    def __getitem__(self,right):
        g = []
        for i in self.dl:
            for x in i:
                if x ==right:
                    g.append(self.dl.index(i))
        if len(g)>0:
            return self.dl[max(g)][right]
        else:
            raise KeyError
    
    def __setitem__(self,right,val):
        g = []
        for i in self.dl:
            for x in i:
                if x==right:
                    g.append(self.dl.index(i))
        
        if len(g)>0:
            self.dl[max(g)][right] = val
        else:
            self.dl.append({right:val})
    
    def __call__(self,key):
        answer = []
        for i in self.dl:
            for x in i:
                if x == key:
                    answer.append((self.dl.index(i),i[key]))
        return answer
    
    def __iter__(self):
        answer = []
            
            
        for i in self.dl:
            for x in i:
                if not any(x in item for item in answer):
                    answer.append((x,i[x]))
                else:
                    for b in answer:
                        if b[0] == x:
                            del answer[answer.index(b)]
                            answer.append((x,i[x]))
        answer = sorted(answer, key = lambda x:(x[1],x[0]))
        return iter(answer)
    
    def __eq__(self,right):
        if type(right) == DictList:
            s =[]
            r = []
            for i in self.dl:
                for x in i:
                    if x not in s:
                        s.append(x)
            for j in right.dl:
                for y in j:
                    if y not in r:
                        r.append(y)
            s = sorted(s)
            r=sorted(r)       
            if s != r:
                return False
            
            else:
                for t in s:
                    if self[t] != right[t]:
                        return False
                return True
                    
        if type(right) == dict:
            p= []
            d = [] 
            for k in self.dl:
                for x in k:
                    if x not in p:
                        p.append(x)
            for j in right:
                if j not in d:
                    d.append(j)
            p = sorted(p)
            d  = sorted(d)
            if p!=d:
                return False
            else:
                for t in p:
                    if self[t]!=right[t]:
                        return False
                return True
        else:
            raise TypeError
        
        def __add__(self,right):
            pass
                  
                    
                    
            
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
