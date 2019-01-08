from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl = []

        assert len(args)>0
        for i in args:
            assert type(i) == dict
            self.dl.append(i)
            


    
    def __len__(self):
        dkey = []
        for i in self.dl:
            for k,v in i.items():
                dkey.append(k)
        return len(set(dkey))
    
    def __repr__(self):
        rtstr = ""
        for i in self.dl:
            rtstr += str(i)
            rtstr += ","
        rtstr = rtstr[:-1]
        return str("DictList("+rtstr+")")
    
    def __contains__(self,key):
        for i in self.dl:
            if key in list(i.keys()):
                return True
        return False
    
    def __getitem__(self,key):
        rtvalue = None
        for i in self.dl:
            for k,v in i.items():
                if k == key:
                    rtvalue = i[k]
        if rtvalue == None:
            raise KeyError
        else:
            return rtvalue
    
    def __setitem__(self,key,value):
        if key in self:
            latest = 0
            for i in range(len(self.dl)):
                if key in self.dl[i].keys():
                    latest = i
            self.dl[latest][key] = value
                
        else:
            k = dict()
            k[key] = value
            self.dl.append(k)
    
    def __call__(self,key):
        rtlist = []
        for i in range(len(self.dl)):
            if key in self.dl[i].keys():
                rtlist.append((i,self.dl[i][key]))
        return rtlist
            
    def __iter__(self):
        iterlist = []
        keylist = []
        for i in range(len(self.dl),0,-1):
            for k in sorted(list(self.dl[i-1].keys())):
                if k not in keylist:
                    iterlist.append((k,self.dl[i-1][k]))
                    keylist.append(k)
                    
        return iter(iterlist)
    
    def __eq__(self,right):
        if type(right) not in (DictList,dict):
            raise TypeError
        selfkey = []
        rightkey = []
        for i in self:
            selfkey.append(i[0])
        for j in right:
            rightkey.append(j[0])
        if set(selfkey) == set(rightkey):
            for k in selfkey:
                if not self[k]==right[k]:
                    return False
            return True
        else:
            return False
        
    def __add__(self,right):

        rtself = dict()
        rtright = dict()
        for i in self:
            rtself[i[0]] = i[1]

        if type(right) == DictList:

            for i in right:
                rtright[i[0]] = i[1]
            return DictList(rtself,rtright)
        elif type(right) == dict:
            rtlist = []
            for i in self.dl:
                rtlist.append(i)
            rtlist.append(right)
            return DictList(rtlist)
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
