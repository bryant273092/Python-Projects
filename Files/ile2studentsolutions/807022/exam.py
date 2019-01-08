from goody import type_as_str  # Useful in some exceptions
from _hashlib import new

class DictList:
    def __init__(self,*arg):
        self.dl = []
        assert len(arg) != 0 ,"DictList.__init__: "+str(arg)+" is not a dictionary."
        for i in arg:
            assert type(i) is dict, "DictList.__init__: "+str(i)+" is not a dictionary."
            self.dl.append(i)
    
    def __len__(self):
        pass
        l = []
        for d in self.dl:
            for k in d:
                l+=k
        return len(set(l))
    
    def __repr__(self):
        return "DictList("+",".join([str(i) for i in self.dl])+")"
        
    def __contains__(self,x):
        return any(x in i for i in self.dl)
    
    def __getitem__(self,x):
        for i in reversed(self.dl):
            if x in i:
                return i[x]
        else:
            raise KeyError(str(x)+"appears in no dictionaries.")

    def __setitem__(self,k,v):

        for i in reversed(self.dl):
            if k in i:
                i[k] = v
                break
        else:
            self.dl.append({k:v}) 
            
    def __call__(self,x):
        l = []
        for i in range(len(self.dl)):
            if x in self.dl[i]:
                l.append((i,self.dl[i][x]))
        return l
        
        
    def __iter__(self):
        l = []
        no = []
        for i in reversed(self.dl):
            d = sorted(i.items())
            for k in d:
                if k[0] not in no:
                    no.append(k[0])
                    l.append(k)
        for i in l:
            yield i
            
    
    def __eq__(self,right):
        if type(right) is DictList:
            k = set()
            k2 = set()
            for i in self.dl:
                for x in i:
                    k.add(x)
            for i in right.dl:
                for x in i:
                    k2.add(x)
            if k != k2:
                return False

            for d in right.dl:
                for k in d:
                    try:
                        if self[k] != right[k]:
                            return False
                    except:
                        return False

            else:
                return True
        elif type(right) is dict:
            k = set()
            for i in self.dl:
                for x in i:
                    k.add(x)
            if k != set(right):
                return False
            for k in right:
                try:
                    if self[k] != right[k]:
                        return False

                except:
                    return False
            else:
                return True
        else:
            raise TypeError(str(right)+" is neither a DictList nor a dict.")
    
    def __add__(self,right):
        if type(right) is DictList:
            l1 = {}
            for k,v in self:
                l1[k] = v
            l2 = {}
            for k,v in right:
                l2[k] = v
            return DictList(l1,l2)
        elif type(right) is dict:
            new = self
            new.dl.append(right)
            return new
        else:
            raise TypeError(str(right)+" is neither a dict nor a DictList.")
        


        
        
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
