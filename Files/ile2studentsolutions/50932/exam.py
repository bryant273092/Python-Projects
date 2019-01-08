from goody import type_as_str  # Useful in some exceptions
from _hashlib import new

class DictList:
    def __init__(self,*d):
        if d==():
            raise AssertionError
        for a in d:
            if type(a)!=dict:
                raise AssertionError
        
        self.dl=[]
        for l in d:
            self.dl.append(l)
        
    
    def __len__(self):
        x=[]
        for d in range(len(self.dl)):
            for a in self.dl[d]:
                if a not in x:
                    x.append(a)
        return len(x)
                
                    
        return len(x)
    
    def __repr__(self):
        return 'DictList('+str(self.dl)[1:-1]+')'

    def __contains__(self,k):
        x=0
        for d in self.dl:
            for a in d:
                if a==k:
                    x+=1
        if x>=1:
            return True
        else:
            return False
    def __getitem__(self,k):
        x=None
        for d in range(len(self.dl)):
            for a in self.dl[d]:
                if a==k:
                    x=self.dl[d][a]
        if x==None:
            raise KeyError
        else:
            return x
    
    def __setitem__(self,k,v):
        x=[]
        for d in range(len(self.dl)):
            for a in self.dl[d]:
                if a==k:
                    x.append(d)
        if x==[]:
            new={k:v}
            self.dl.append(new)
        elif x!=[]:
            self.dl[x[-1]][k]=v
    def __call__(self,k):
        x=[]
        for d in range(len(self.dl)):
            for a in self.dl[d]:
                if a==k:
                    t=(d,self.dl[d][a])
                    x.append(t)
        return x
    def __iter__(self):
        x=[]
        for d in self.dl:
            x.append(d)
        y=[]
        x.reverse()
    
        
        for first in range(len(x)):
            for second in x[first]:
                if second not in y:
                    y.append(second)
                    answer=(second,x[first][second])
                    yield answer
                
                
    def __eq__(self,k):
        if type(k) is dict or type(k) is DictList:
            x=[]
            y=[]
            for d in range(len(self.dl)):
                for a in self.dl[d]:
                    if a not in x:
                        x.append(a)
            if type(k)==dict:
                for d in k:
                    if d not in y:
                        y.append(d)
            elif type(k)==DictList:
                for d in range(len(k.dl)):
                    for a in k.dl[d]:
                        if a not in y:
                            y.append(a)
            answer=0
            
            if x==y:
                x_get=None
                y_get=None
                for n in x:
                    x_get=self.__getitem__(n)
                    y_get=k.__getitem__(n)
                    if x_get!=y_get:
                        answer+=1
                if answer==0:
                    return True
                else:
                    return False
                 
            else:
                return False
        else:
            raise TypeError
    
    def __add__(self,new_dict):
        if type(new_dict)==DictList:
            x=dict()
            y=dict()
            for a in range(len(self.dl)):
                for d in self.dl[a]:
                    if d in x:
                        del x[d]
                    x[d]=self.dl[a][d]
            for b in range(len(new_dict.dl)):
                for e in new_dict.dl[b]:
                    if e in y:
                        del y[e]
                    y[e]=new_dict.dl[b][e]
            new=DictList(x,y)
            return new
        if type(new_dict)==dict:
            x={}
            for a in range(len(self.dl)):
                for d in self.dl[a]:
                    if d in x:
                        del x[d]
                    x[d]=self.dl[a][d]
            new=DictList(x,new_dict)
            return new
        else:
            raise TypeError
    def __radd__(self,new_dict):
        return self.__add__(new_dict)
    
    
        
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
