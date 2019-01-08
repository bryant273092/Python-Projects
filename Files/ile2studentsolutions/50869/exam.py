from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*dic):
        self.dl = []
        if len(dic) == 0:
            raise AssertionError
        for d in dic:
            if type(d) is not dict:
                raise AssertionError("'DictList.__init__':'abc'is not a dictionary")
            else:
                self.dl. append(d)
                
    def __len__(self):
        n = 0
        s = set()
        for i in range(len(self.dl)):
            for x in self.dl[i].keys():
                s.add(x)
            n = len(s)
        return n
    
    def __repr__(self):
        for i in range(len(self.dl)):
            return 'DictList('+str( self.dl[i])+','+')'
                                                    
    def __contains__(self,n):
        v = set()
        for x in self.dl:
            for key in x.keys():
                v.add(key)
        if n in v:
            return True
        else:
            return False
    def __getitem__(self,k):
        l = []
        n = []
        if self.__contains__(k):
            for x in self.dl:
                if k in x.keys():
                    l . append(x)
            for x in l:
                n.append(self.dl.index(x))
            x[k] = self.dl[max(n)][k]
        
        else:
            raise KeyError
        return x[k]
    def __setitem__(self,k,v):
        l=[]
        n = []
        for x in self.dl:
            if any(k in x):
                l.append(x)
                n.append(self.dl.index(x))
                self.dl[max(n)] = v
            elif all(k in x):
                w = {}
                self.dl.append(w)
                w[k] = v 
                self.__len__+=1
    def __call__(self,k): 
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
