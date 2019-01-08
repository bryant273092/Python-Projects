from goody import type_as_str  # Useful in some exceptions

class DictList:

    def __setitem__(self,key,value):
        ran = False
        for x in range(1,len(self.dl)):
            for k in self.dl[-x]:
                if key == k:
                    self.dl[-x][k] = value
                    ran = True
        if ran == False:
            for x in self.dl[0]:
                if key == x:
                    self.dl[0][key] = value
                    ran = True
        if ran == False:
            self.dl.append(dict([(key,value)]))
            
    def __getitem__(self,key):
        result = ''
        ran = False
        for x in range(1,len(self.dl)):
            for k in self.dl[-x]:
                if key == k:
                    result = self.dl[-x][k]
                    return result
        if ran == False:
            for x in self.dl[0]:
                if key == x:
                    result = self.dl[0][key]
        if result == '': raise KeyError(str(key) + ' appears in no dictionaries')
        else: return result
        
    def __init__(self,*args):
        self.dl = []
        if len(args) == 0: raise AssertionError("DictList.__init__: DictList is empty")
        else:
            for x in args:
                if type(x) != dict: raise AssertionError("DictList.__init__: " + str(x) + " is not a dictionary")
                else:
                    self.dl.append(x)
    
    def __len__(self):
        result = set()
        for x in self.dl:
            for k in x.keys():
                result.add(k)
        return len(result)
    
    def __repr__(self):
        string = ''
        for x in self.dl:
            string += str(x)
        return "DictList("+string+')'
    
    def __contains__(self,key):
        result = False
        for x in self.dl:
            for k,v in x.items():
                if key == k:
                    result = True
        return result
    
    def __call__(self,key):
        result = []
        for x in range(len(self.dl)):
            for k in self.dl[x]:
                if key == k:
                    result.append((x,self.dl[x][k]))
        return result
    
    def __iter__(self):
        l = []
        for x in range(1,len(self.dl)):
            for k,v in self.dl[-x].items():
                if (k,v) not in l:
                    l.append((k,v))
        for x in self.dl[0]:
            for k,v in self.dl[0].items():
                if (k,v) not in l:
                    l.append((k,v))
        x = iter(l)
        try:
            while True:
                n = next(x)
                yield n
        except StopIteration:
            return
        
    def __eq__(self,other):
        b = True
        try:
            self.dl.__getitem__(x[0])
        except:
            return False
        return b
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    d2 = DictList(dict(a=1,b=12), dict(c=13))
    print(d1==d2)

    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
