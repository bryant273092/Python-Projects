from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*dic):
        self.dl=[]
        for i in dic:
            if type(i)!=dict:
                raise AssertionError ('DictList.__init__:'+dic+'is not a dictionary.')
            else:
                self.dl.append(i)


    def __len__(self):
        l=[]
        for i in self.dl:
            for a in i.keys():
                l.append(a)
        m=set(l)
        return len(m)
    
    def __repr__(self):
        m='DictList('
        for i in self.dl:
            m+=str(self.dl[i])
        return m+')'
    
    def __contains__(self,m):
        for i in self.dl:
            if m in i.keys():
                return True
        return False
        
    def __getitem__(self,a):
        assert type(a)==str
        m=0
        for i in reversed(self.dl):
            if a in i.keys():
                    m=i[a]
                    return m
            else:
                raise KeyError
        
    def _setitem__(self,a,m):
        for i in self.dl:
            for w in i.keys():
                if a==w:
                    self.dl[w]=m
                    return
        self.dl.append('{'+str(a)+':'+str(m))
                
    def __call__(self,a):
        m=0
        n=0
        p=()
        for i in self.dl:
            if a in i.keys():
                n=i[a]
                p=(m,n)
                return '['+str(p)+']'
            m+=1
    
    def __iter__(self):
        pass
    
    def __equal__(self,right):
        if type(right)!=DictList or type(right)!=dict:
            raise TypeError('Wrong Type!')
    
        
        
        
        
if __name__ == '__main__':
    d=DictList({'a':1,'b':2,'c':3},{'c':13,'d':14},{'e':15})
#Put code here to test DictList before doing bsc test


    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
