from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self,*args):
        self.dl = []
        if len(args) > 0:
            for arg in args:
                if type(arg) != dict:
                    raise AssertionError("DictList.__init__:'abc' is not a dictionary")
                else:
                    self.dl.append(arg)
        else:
            raise AssertionError("DictList.__init__:'abc' is not a dictionary")
    
    def __len__(self):
        vlist = []
        for i in self.dl:
            for k in i.keys():
                if k not in vlist:
                    vlist.append(k)
        return len(vlist)

    def __repr__(self):
        result = ""
        for i in range(len(self.dl)-1):
            result += str(self.dl[i]) + ', '
        return "DictList(" + str(result) + str(self.dl[-1]) +  ")"
    
    def __contains__(self,item):
        for i in self.dl:
            if item in i.keys():
                return True
        return False
    def __getitem__(self,key):
        klist = []
        kdict = {}
        for i in range(len(self.dl)):
            for k in self.dl[i].keys():
                if k not in klist:
                    klist.append(k)
                    kdict[k] = i
                elif k in klist:
                    kdict[k] = i
        if key not in klist:
            raise KeyError
        elif key in klist:
            for i in self.dl:
                if key in [k for k in i.keys()]:
                    return self.dl[kdict[key]][key]
    
    def __setitem__(self,key,value):
        klist = []
        kdict = {}
        for i in range(len(self.dl)):
            for k in self.dl[i].keys():
                if k not in klist:
                    klist.append(k)
                    kdict[k] = i
                elif k in klist:
                    kdict[k] = i
        
        if key in klist:
            for i in self.dl:
                if key in [k for k in i.keys()]:
                    self.dl[kdict[key]][key] = value
        elif key not in klist:
            self.dl.append({key:value})
        
    def __call__(self,key):
        klist = []
        kdict = {}
        for i in range(len(self.dl)):
            for k in self.dl[i].keys():
                if k not in klist:
                    klist.append(k)
                    kdict[k] = [(i,self.dl[i][k])]
                elif k in klist:
                    kdict[k].append((i,self.dl[i][k]))
        if key in klist:
            for i in self.dl:
                for k in i.keys():
                    if k == key:
                        return [j for j in kdict[key]]
        else:
            return []
        
    def __iter__(self):
        klist = []
        for i in range(len(self.dl)):
            for k in self.dl[-i-1].keys():
                if k not in klist:
                    klist.append(k)
                    yield(str(k),self.dl[-i-1][k])
                else:
                    pass
    
    def __eq__(self,right):
        if type(right) == DictList:
            klist = [i for i in self]
            rlist = [i for i in right]
            if sorted(klist,key = lambda x:x[0]) == sorted(rlist,key=lambda x:x[0]):
                return True
            else:
                return False
        elif type(right) == dict:
            klist = [i for i in self]
            dlist = [(k,v) for k,v in right.items()]
            if sorted(klist,key = lambda x:x[0]) == sorted(dlist,key=lambda x:x[0]):
                return True
            else:
                return False
            
            
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
