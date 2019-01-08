from goody import type_as_str  # Useful in some exceptions
from nt import lstat

class DictList:
    def __init__(self, *args):
        self.dl=[]
        assert len(args) != 0, "DictList.__init__:can't give empty argument"
        for x in args:
            assert isinstance(x, dict), "DictList.__init__:"+str(x)+"is not a dictionary"
            self.dl.append(x)
    def __len__(self):
        temp=[]
        for d in self.dl:
            for k in d.keys():
                if k not in temp:
                    temp.append(k)
        return len(temp)
    def __repr__(self):
        return "DictList("+", ".join(str(d) for d in self.dl)+")"
    def __contains__(self,t):
        for d in self.dl:
            if t in d.keys():
                return True
        return False
    def __getitem__(self,t):
        n=None
        for d in self.dl:
            if t in d.keys():
                n=d[t]
        if n!=None:
            return n
        else:
            raise KeyError("DictList.__getitem__:"+str(t)+"appears in no dictionary")
    def __setitem__(self,t,v):
        n=None
        for d in self.dl:
            if t in d.keys():
                n=d
        if n!=None:
            n[t]=v
        else:
            self.dl.append({t:v})
    def __call__(self,t):
        lst=[]
        for i in range(len(self.dl)):
            if t in self.dl[i].keys():
                lst.append((i,self.dl[i][t]))
        return lst
    def __keys__(self):
        t=set()
        for x in self.dl:
            t=t.union(x.keys())
        return t
    def __iter__(self):
        self.repeat=[]
        self.m=len(self.dl)-1
        self.lst=sorted(self.dl[self.m].keys())
        self.n=0
        return self
    def __next__(self):
        while len(self.lst)>self.n:
            if self.lst[self.n] not in self.repeat:
                self.repeat.append(self.lst[self.n])
                return (self.lst[self.n],self.dl[self.m][self.lst[self.n]])
            self.n+=1
            while len(self.lst)==self.n:
                self.m-=1
                if self.m<0:
                    raise StopIteration
                self.lst=sorted(self.dl[self.m].keys())
                self.n=0
    def __eq__(self,right):
        if type(right) is DictList:
            if self.__keys__()!=right.__keys__():
                return False
            for x in self.__keys__():
                if self.__getitem__(x)!=right[x]:
                    return False
            return True
        elif type(right)is dict:
            if self.__keys__()!=set(right.keys()):
                return False
            for x in self.__keys__():
                if self.__getitem__(x)!=right[x]:
                    return False
            return True
        else:
            raise TypeError



            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    a=DictList({1:2},{3:4})
    print(a.__keys__())
    for x in a:
        print(x)

    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
