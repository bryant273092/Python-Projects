from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        if len(args) == 0:
            raise AssertionError
        for x in args: 
            if type(x) == dict: 
                self.dl.append(x)
            else:
                raise AssertionError
    
    def __len__(self):
        valid = []
        for d in self.dl: 
            for keys in d: 
                if keys not in valid: 
                    valid.append(keys)
        
        return len(valid)
            
    
    def __repr__(self):
        dict_str = "DictList({})".format(','.join(str(x) for x in self.dl))
        return dict_str
    
    def __getitem__(self, key):
        latest = [0]
        if self.__contains__(key):           
            for d in self.dl: 
                for keys in d: 
                    if key == keys: 
                        latest[0] = (d[keys])
            return latest[0]
        else: 
            raise KeyError
    
    def __setitem__(self,key,value):
        #print(key, value)
        if self.__contains__(key):
            loc = self.__call__(key)
            loc1 = loc[len(loc)-1]
            self.dl[loc1[0]][key] = value
        else: 
            new_dict = {key: value}
            self.dl.append(new_dict)
    
    def __contains__(self, key):
        #print(key)
        for d in self.dl:
            for keys in d.keys():
                if key == keys:
                    return True
        return False

    def __call__(self,key):
        lst = []
        if self.__contains__(key):
            for i in range(0, len(self.dl)):
                if key in self.dl[i].keys():
                    lst.append((i, self.dl[i][key]))
            return lst
        else: 
            return []
        
    
    def __iter__(self):
        already_outputted = []
        for i in range(len(self.dl), 0, -1):
            s = sorted(self.dl[i-1])
            for value in s:
                if value not in already_outputted:
                    yield((value, self.__getitem__(value)))
                    already_outputted.append(value)
    
    def __eq__(self, d1):
        if type(d1) == dict: 
            for x in self.dl:
                for keys in x.keys():
                    try: 
                        if self.__getitem__(keys) != d1[keys]:
                            return False
                    except: 
                        return False
            return True
        elif type(d1) == DictList:
            for x in self.dl: 
                for keys in x.keys():
                    try: 
                        if self.__getitem__(keys) != d1.__getitem__(keys):
                            return False
                    except: 
                        return False
            return True
        else: 
            raise TypeError


    def __add__(self,d1):
        if type(d1) == dict: #create copy 
            pass
            
        elif type(d1) == DictList:
            n1 = dict()
            for x in self.dl:
                for keys in x.keys():
                    n1[keys] = self.__getitem__(keys)
            n2 = dict()
            for y in d1.dl:
                for keys in y.keys():
                    n2[keys] = d1.__getitem__(keys)
            return DictList(n1,n2)
        else: 
            def add(d1, self):
                if type(d1) == dict: 
                    pass
                elif type(d1) == DictList:
                    n1 = dict()
                    for x in self.dl:
                        for keys in x.keys():
                            n1[keys] = self.__getitem__(keys)
                    n2 = dict()
                    for y in d1.dl:
                        for keys in y.keys():
                            n2[keys] = d1.__getitem__(keys)
                    return DictList(n1,n2)
                else: 
                    raise TypeError
        

            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    '''d0 = dict(a=1,b=2,c=3)
    d1 = dict(c=13,d=14,e=15)
    d2 = dict(e=25,f=26,g=27)
    
    c = DictList(d0, d1, d2)
    print(c) #repr
    
    print(len(c))
    print(c.__contains__('a'))
    print(c['c']) #getitem
    print(c['e'])
    #print(c['x'])
    
    #setitem
    c['k'] = 12
    c['a'] = 'asl;dkfj;k'
    print(c)
    
    print(c('e'))
    print(c('x'))
    
    #eq
    e1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    e2 = DictList(dict(a=1,b=12), dict(c=13))
    e3 = {}
    
    print(e1 == e2)
    
    print(e1 == dict(a=1,c=13))
    
    #iter
    i0 = dict(a=1,b=2,c=3)
    i1 = dict(c=13,d=14,e=15)
    i2 = dict(e=25,f=26,g=27)
    i  = DictList(i0,i1,i2)
    produced = [j for j in i]
    print(produced)
    
    
    #add
    a1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    a2 = DictList(dict(a='one',b='two'), dict(b='twelve',c='thirteen'))
    adict = dict(a='one',b='two')
    
    print('addddddddddddddddddddd')
    print(a1 + adict)
    print(a1+a2)
    print(adict+a1)'''
    
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
