
class DictList:
    def __init__(self, *args):
        self.dl = []
        if len(args) == 0:
            raise AssertionError
        for d in args:
            if type(d) != dict:
                raise AssertionError
            self.dl.append(d)

    def __len__(self):
        returnset = set()
        for d in self.dl:
            for k in d.keys():
                returnset.add(k)
        return len(returnset)

    def __repr__(self):
            return 'DictList'+str(tuple(self.dl))
    
    def __contains__(self,item):
        for d in self.dl:
            for k in d.keys():
                if k == item:
                    return True
        return False
    
    def __getitem__(self,item):
        returnval = None
        for d in self.dl:
            for k,v in d.items():
                if k == item:
                    returnval = v
        if returnval == None:
            raise KeyError
        return returnval
                
    def __setitem__(self,item,value): ###NEEDS FIX###
        templist = list(self.dl)
        found = 0
        count = len(self.dl) - 1
        while templist != [] and found == 0:
            active = templist.pop(-1)
            if item in active:
                self.dl[count][item] = value
                found = 1
            else:
                count -= 1
        if found == 0:
            self.dl.append({item:value})

    def __call__(self,item):
        returnlist = []
        for x,d in enumerate(self.dl):
            for k,v in d.items():
                if k == item:
                    returnlist.append((x,v))
        return returnlist
    
        
    def __iter__(self):
        returnlist = []
        usedlist = []
        workwith = list(self.dl)
        while True:
            active = workwith.pop(-1)
            for k,v in active.items():
                if k not in usedlist:
                    returnlist.append((k,v))
                    usedlist.append(k)
            if len(workwith) == 0:
                break
        for item in returnlist:
            yield item    
    
    def __eq__(self,right):
        if type(right) not in [DictList,dict]:
            raise TypeError
        for d in self.dl:
            for k in d.keys():
                try:
                    if self.__getitem__(k) != right.__getitem__(k):
                        return False
                except KeyError:
                    return False
        return True
               
    def __add__(self,right):
        newdict1 = {}
        if type(right) == DictList:
            newdict2 = {}
            for d in self.dl:
                newdict1.update(d)
            for d in right.dl:
                newdict2.update(d)
            return DictList(newdict1, newdict2)
        elif type(right) == dict:
            for d in self.dl:
                newdict1.update(d)
            newdict1.update(right)
            return DictList(newdict1)
        else:
            raise TypeError
    def __radd__(self,left):
        if type(left) == dict:
            for d in self.dl:
                left.update(d)
            return DictList(left)
        else:
            raise TypeError   
          
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    d2 = DictList(dict(a='one',b='two'), dict(b='twelve',c='thirteen'))
    adict = dict(a='one',b='two')
    d = d1+adict
    print('d1+adict =', d1+adict)
    d1['b'] = 'x'
    print('d1 =',d1)
    print(d['b'])
    adict['b'] = 'x'
    print(d['b'])
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
