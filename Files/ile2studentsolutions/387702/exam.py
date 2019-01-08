from goody import type_as_str  # Useful in some exceptions


class DictList:
    def __init__(self,*dicts):
        assert len(dicts) !=0, f"arguments cannot be empty"
        for i in dicts:
            assert type(i) is dict, f"{repr(i)} is not a dictionary."
        self.dl = list(dicts)
        
    def __len__(self):
        temp = set()
        for i in self.dl:
            for key in i:
                temp.add(key)
        return len(temp)
    def __repr__(self):
        return "DictList(" + ','.join(str(x) for x in self.dl)+')'
    def __contains__(self,item):
        for i in self.dl:
            if item in i:
                return True
        return False
    def __getitem__(self,item):
        status = False
        for i in self.dl:
            if item in i:
                status = True
                result = i[item]
        if not status:
            raise KeyError(f"{item} is not in any dictionary of the Dictlist")
        return result
    def __setitem__(self, item, value):
        try:
            temp = self[item]
            for i in range (len(self.dl)):
                if item in self.dl[i] and self.dl[i][item] == temp:
                    self.dl[i][item] = value
        except KeyError:
            self.dl.append({item:value})
    
    def __call__(self, item):
        result = []
        for i in range(len(self.dl)):
            if item in self.dl[i]:
                result.append((i, self.dl[i][item]))
        return result
    
    def __iter__(self):
        def gen(dl):
            temp = set()
            for i in reversed(dl):
                for k,v in sorted(i.items(), key = lambda x: x[0]):
                    if k not in temp:
                        yield (k,v)
                        temp.add(k)
        return gen(list(self.dl))  
    
    def __eq__(self,right):
        if type(right) not in (dict, DictList):
            raise TypeError(f'the right operand type {type_as_str(right)} is not of type dict or DictList')
        
        ltemp = set()
        for i in self.dl:
                for key in i:
                    ltemp.add(key)
        
        if type(right) is DictList:  
            rtemp = set()
            for j in right.dl:
                for key1 in j:
                    rtemp.add(key1)
            if ltemp == rtemp:
                return all(self[i] == right[i] for i in ltemp)
            else:
                return False
        else:
            if ltemp == set(right.keys()):
                return all(self[i] == right[i] for i in ltemp)
            else:
                return False
                
    def __add__(self, right):
        if type(right) not in (dict, DictList):
            raise TypeError(f'the right operand type {type_as_str(right)} is not of type dict or DictList')
        elif type(right) is DictList:
            temp1 = {}
            temp2 = {}
            for i in self.dl:
                for k,v in i.items():
                    temp1[k] = v
            for j in right.dl:
                for k1, v1 in j.items():
                    temp2[k1] = v1 
            return DictList(temp1, temp2)
        else:
            return eval(repr(self).strip(")") +","+ str(right) + ')')
        
    def __radd__(self,left):
        if type(left) is not dict:
            raise TypeError(f'the left operand type {type_as_str(left)} is not of type dict')
        return eval("DictList(" + str(left)+',' + ','.join(str(x) for x in self.dl)+')')
    
           
            
                
    
            
        
            
        




            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
#    d1 = DictList('avc')
    d = DictList({'a':1,'b':2,'c':3}, {'c':13, 'd':14, 'e':15}, {'e':25, 'f':26, 'g':27})
    print(len(d))
    print(repr(d))
    print('x' in d)
    print('a' in d)
    print(d['a'])
    print(d['d'])
    print(d['g'])
    print(d['c'])
    print(d['e'])
#    print(d['x'])
    d['c'] = 'new'
    d['x'] = 'new'
    print(d)
    print(d('a'))
    print(d('e'))
    for i in d:
        print(i)
    d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    d2 = DictList(dict(a=1,b=12),dict(c=13))
    print(d1==d2)
    print(d1 == dict(a=1,b=12,c=13))
    print(d1 == dict(a=1,c=13))
    print(d1 == dict(a=1,b=2,c=13))
    
    adict = dict(a='one',b='two')
    print(d+adict)
    print(adict+d)
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#    driver.default_show_exception=True
#    driver.default_show_exception_message=True
#    driver.default_show_traceback=True
    driver.driver()
