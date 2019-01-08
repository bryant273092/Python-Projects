from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl = []
        assert args
        for d in args:  
            assert isinstance(d, dict)
            self.dl.append(d)
    
    def __len__(self):
        l = set()
        for d in self.dl:
            for key in d:
                l.add(key)
        return len(l)
    
    def __repr__(self):
        result = 'DictList({'
        dicts = list()
        for d in self.dl:
            dis = list()
            for k in d:
                dis.append("'"+str(k)+"'"+":"+str(d[k])+"")
            dicts.append(",".join(dis)+"}")
        result += ", {".join(dicts)+")"
        return result
    
    def __contains__(self,x):
        for d in self.dl:
            for k in d:
                if k == x:
                    return True
        return False
    
    def __getitem__(self,x):
        if not x in self:
            raise KeyError
        for d in self.dl:
            for k in d:
                if k == x:
                    result = d[k]
        return result
    
    def __setitem__(self,x,y):
        if x in self:
            dis = 0
            for d in range(len(self.dl)):
                for k in self.dl[d]:
                    if k == x:
                        dis = d
            self.dl[dis][x] = y
        else:
            self.dl.append({x:y})
            
    def __call__(self,x):
        dicts = list()
        for d in range(len(self.dl)):
            for k in self.dl[d]:
                if k == x:
                    dicts.append((d,self.dl[d][k]))
        return dicts
    
    def __iter__(self):
        r = list()
        result = list()
        index = len(self.dl)
        while index >= 0:
            index -= 1
            n = list()
            for k in self.dl[index]:
                if k in r:
                    continue
                n.append(k)
            n = sorted(n)
            for i in n:
                r.append(i)
        for i in r:
            result.append((i,self[i]))
        for i in result:
            yield i
        
    def __eq__(self,x):
        if isinstance(x, DictList):
            for d in self.dl:
                for k in d:
                    if not k in x:
                        return False
                    elif self[k] != x[k]:
                        return False
            for d in x.dl:
                for k in d:
                    if not k in self:
                        return False
                    elif x[k] != self[k]:
                        return False
            return True
        if isinstance(x, dict):
            for d in self.dl:
                for k in d:
                    if not k in x:
                        return False
                    elif x[k] != self[k]:
                        return False
            for k in x:
                if not k in self:
                    return False
                elif x[k] != self[k]:
                        return False
            return True
        else:
            raise TypeError

    def __add__(self,x,reverse = False):
        if isinstance(x, DictList):
            n_dict = {}
            for d in self.dl:
                for k in d:
                    n_dict[k] = self[k]
            s_dict = {}
            for d in x.dl:
                for k in d:
                    s_dict[k] = x[k]
        elif isinstance(x,dict):
            n_dict = {}
            for d in self.dl:
                for k in d:
                    n_dict[k] = self[k]
            s_dict = x
        else:
            raise TypeError
        if reverse:
            return DictList(s_dict,n_dict)
        else:
            return DictList(n_dict,s_dict)
    
    def __radd__(self,x):
        result = self.__add__(x,True)
        return result
        
        
                    
    




            
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
