from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        if len(args) == 0:
            raise AssertionError('DictList.__init__: {} is not a dictionary.'.format(args))
        for arg in args:
            if type(arg) != dict:
                raise AssertionError('DictList.__init__: {} is not a dictionary.'.format(arg))
        self.dl = list(args)
        
    def __len__ (self):
        keyset = set()
        for i in self.dl:
            for j in i.keys():
                keyset.add(j)
        return len(keyset)
    
    def __repr__(self):
        #print("DictList({})".format(dict for dict in self.dl))
        return "DictList({})".format(d for d in self.dl)
    
    def __contains__(self,item):
        c = 0
        for i in self.dl:
            if item in i.keys():
                c += 1
        return c > 0
    
    def __getitem__(self,item):
        result = ''  
        for i in self.dl:
            if item in i.keys():
                result = i[item]
        if result == '':
            raise KeyError('DictList.__getitem__: {} is not a key in any of the dictionaries'.format(item))
        else:
            return result
        
    def __setitem__(self,item,value):
        result = 0
        for i in self.dl:
            if item in i.keys():
                i[item] = value
                result = 1
        if result == 0:
            self.dl.append({item:value})
            
    def __call__(self,item):
        result =[]
        for i in range(len(self.dl)):
            if item in self.dl[i].keys():
                result.append((i,self.dl[i][item]))
        return sorted(result, key = lambda x:x[0])
        
    def __iter__(self):
        iterlist = []
        keyset = set()
        for d in reversed(self.dl):
            for key in sorted(d.keys()):
                if key not in keyset:
                    iterlist.append((key,d[key]))
                    keyset.add(key)
        return iter(iterlist)
    
    def __eq__(self,right):
        if type(right) not in (DictList,dict):
            raise TypeError('DictList.__eq__: {} is not of DictList or dict type'.format(right))
        for i in range(len(self.dl)):
            if self.dl[i].keys() != right.dl[i].keys():
                return False
        for d in reversed(self.dl):
            for k in d.keys():
                if self[k] != right[k]:
                    return False
        '''
                if type(right) not in (DictList,dict):
            raise TypeError('DictList.__eq__: {} is not of DictList or dict type'.format(right))
        k1 = set()
        k2 = set()
        if type(self) == DictList and type(right) == DictList:
            for i in self.dl:
                k1.add(i.keys())
            for i in right.dl:
                k2.add(i.keys())
        elif type(self) == DictList and type(right) == dict:
            for i in self.dl:
                k1.add(i.keys())
                k2 = right.keys()
        elif type(right) == DictList and type(self) == dict:
            for i in right.dl:
                k2.add(i.keys())
                k1 = self.keys()   
        result = (k1 == k2) 
                
        for d in self.dl:
            for k in d.keys():
                if self[k] != right[k]:
                    result2 = False
        return result and result2
        '''
                
    def __add__(self,right):
        if type(right) not in (DictList, dict):
            raise TypeError('DictList.__eq__: {} is not of DictList or dict type'.format(right))
        if  type(right) == DictList:
            ldict = dict()
            rdict = dict()
            for dict in self.dl:
                for key in dict:
                    if key not in ldict.keys():
                        ldict[key] = {}
                    ldict[key].add(dict[key]) 
            for dict in right.dl:
                for key in dict:
                    if key not in rdict.keys():
                        rdict[key] = {}
                    rdict[key].add(dict[key])   
            return DictList(ldict,rdict)    
        elif type(right) == dict:
            return DictList(self.dl,right)
        elif type(self) == dict and type(right) == DictList:
            return DictList(self,right.dl)
            
       


            
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
