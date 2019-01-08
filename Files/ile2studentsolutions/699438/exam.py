from goody import type_as_str  # Useful in some exceptions
from pip._internal.utils.misc import enum

class DictList:
    def __init__(self,*args):
        self.dl=[]
        assert len(args) != 0
        for i in args:
            assert type(i)==dict
            self.dl.append(i)
        
    def __len__(self):
        l=[]
        for j in self.dl:
            for i in j:
                if i not in l:
                    l.append(i)
        return len(l)
            
    def __repr__(self):
        return 'DictList({})'.format(', '.join([str(i) for i in self.dl]))
    
    def __contains__(self,item):
        return any([item in i for i in self.dl])
    
    def __getitem__(self,item):
        l=[]
        if any([item in i for i in self.dl]):
            for i in self.dl:
                if item in i:
                    l.append(i[item])
            return max(l)
        else:
            raise KeyError
    
    def __setitem__(self,item,value):
        l=[]
        if any([item in i for i in self.dl]):
            for i in range(len(self.dl)):
                if item in self.dl[i]:
                    l.append((i,item,self.dl[i][item]))
            l=sorted(l,key=lambda x:x[2],reverse=True)
            self.dl[l[0][0]][l[0][1]]=value    
        else:
            self.dl.append({item:value})
            
            
    def __call__(self,item):
        l=[]
        for i in range(len(self.dl)):
                if item in self.dl[i]:
                    l.append((i,self.dl[i][item])) 
        return l
    
    def __iter__(self):
        l=[]
        for i in range(len(self.dl)):
            for k in sorted(self.dl[-(i+1)].keys()):
                if k not in l:
                    yield (k,self.__getitem__(k))
                    l.append(k)

    def __eq__(self,item):
        s=set()
        s1=set()
        for i in self.dl:
            s=s.union(set(i.keys()))
        if type(item) is DictList:
            for j in item.dl:
                s1=s1.union(set(j.keys()))
            return s==s1 and all([self.__getitem__(i)==item.__getitem__(i) for i in s])
        elif  type(item) is dict:
            s1=set(item.keys())
            return s==s1 and all([self.__getitem__(i)==item[i] for i in s])
        else:
            raise TypeError
                
                
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