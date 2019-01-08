from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self, *matcharg):
        dllist=[]
        if matcharg == ():
            raise AssertionError("DictList.__init__: "+str(matcharg)+" is not a dictionary.")
        for x in matcharg:
            if type(x) != dict or len(matcharg)==0:
                raise AssertionError("DictList.__init__: "+str(matcharg)+" is not a dictionary.")
            else:
                dllist.append(x)
                self.dl = dllist
                
    def __len__(self):
        countlist = []
        for dictarg in self.dl:
            for keys in dictarg:
                if keys not in countlist:
                    countlist.append(keys)
        return len(countlist)
    
    def __repr__(self):
        return "DictList("+",".join([str(x) for x in self.dl])+")"
    
    def __contains__(self, inarg):
        found = []
        for dictarg in self.dl:
            if inarg in dictarg.keys():
                found.append(inarg)
        return len(found)>0
                
        
    def __getitem__(self,k):
        finalvalue = []
        for dictarg in self.dl:
            if k in dictarg.keys():
                finalvalue.append(dictarg.get(k))
        if len(finalvalue) > 0:
            return finalvalue[-1]               
        else: raise KeyError

    def __setitem__(self,k,v):
        finalvalue = []
        for dictarg in self.dl:
            if type(dictarg)==str:
                finalvalue.append(dictarg)
            else:
                if k in dictarg.keys():
                    finalvalue.append(dictarg)
                else:
                    newdict = dict()
                    newdict[k] = v
                    self.dl.append(newdict)
        self.dl[self.dl.index(finalvalue[-1])]=v
    
        
    def __call__(self,k):
        tuplelist=[]
        finalvalue = []
        for dictarg in self.dl:
            if k in dictarg.keys():
                finalvalue.append(dictarg)
        for valid in finalvalue:            
            for key,v in self.dl[self.dl.index(valid)]:
                tuplelist.append(k,v)
        return tuplelist
    
    def __iter__(self):
        uniquelist = []
        for dictarg in self.dl:
            for key,value in dictarg.items():
                if key not in uniquelist:
                    uniquelist.append((key,value))
        for x in uniquelist:
            yield x
            
    def __eq__(self,right):
        uniquekeys = []
        for x in right:
            if x not in uniquekeys:
                uniquekeys.append(x[0])
        uniquerightkeys=[]
        for x in self:
            if x not in uniquerightkeys:
                uniquerightkeys.append(x[0])
        if len(uniquekeys) == len(uniquerightkeys):
            if uniquekeys == uniquerightkeys:
                return True
            else:return False
        else: return False
        
    def __ne__(self,right):
        return self!=right
        
            
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
