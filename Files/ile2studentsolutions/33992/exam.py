from goody import type_as_str  # Useful in some exceptions


class DictList:
    def __init__ (self, *args):
        self.dl = []
        
        arg = args
        for a in arg:
            print(a)
            assert type(a) is dict
            assert len(arg) >0
            self.dl.append(a)
    
    def __len__(self):
        track = set()
        for l in self.dl:
            for k in l.keys():
                track.add(k)
        return len(track)
    
    def __repr__(self):
       
        return 'DictList(' + ', '.join(str(c) for c in self.dl) +')'
    
    def __contains__(self, look):
        allk= set()
        for l in self.dl:
            for k in l.keys():
                allk.add(k)
        return look in allk
    
    def __getitem__(self, k):
        if not k in self:
            raise KeyError
                
        for l in self.dl:
            if k in l.keys():
                val = l.get(k)
        return val
    
    def __setitem__(self,k,v):
        if not k in self:
            newdict= dict()
            newdict[k] = v
            self.dl.append(newdict)
        else:
            ind = 0
            for l in self.dl:
                if k in l.keys():
                    ind+=1
            self.dl[ind][k] = v
            
    def __call__(self, k):
        result = []
        ind = 0
        for l in self.dl:
            if k in l.keys():
                val = l.get(k)
                result.append((ind, val))
                ind+=1
            else:
                ind+=1
        print(result)
        return result
    
    
    
    def __eq__(self,other):
        if type(other) not in (DictList, dict):
            raise TypeError
        elif type(other) is DictList:
            sset = set()
            oset = set()
            for l in self.dl:
                for k in l.keys():
                    sset.add(k)
            for m in other.dl:
                for n in m.keys():
                    oset.add(n)
            
            if sset==oset:
                for akey in sset:
                    if self[akey]==other[akey]:
                        continue
                    else:
                        return False
                return True
            
            else:
                return False
        elif type(other) is dict:
            sset = set()
            oset = set()
            for l in self.dl:
                for k in l.keys():
                    sset.add(k)
            for m in oset.keys():
                oset.add(m)
                
            if oset==sset:
                for akey in sset:
                    if self[akey]==other[akey]:
                        continue
                    else:
                        return False
                return True
            else:
                return False
            
                



            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    #d  = DictList()
    #d  = DictList(1)
    #d  = DictList('a')


    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
