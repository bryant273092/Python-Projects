from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        assert len(args) != 0
        for arg in args:
            assert type(arg) is dict, 'DictList.__init__:'+repr(arg)+ 'is not a dictionary'
            self.dl.append(arg)
    
    def __len__(self):
        counted_set = set()
        count = 0
        for d in self.dl:
            for key in d:
                if key not in counted_set:
                    count+=1
                    counted_set.add(key)
        return count
    
    def __repr__(self):
        return 'DictList('+','.join(str(d) for d in self.dl)+')'
    
    def __contains__(self,key):
        for d in self.dl:
            if key in d:
                return True
        return False
    
    def __getitem__(self, key):
        for n in range(len(self.dl)-1,-1,-1):
            if key in self.dl[n]:
                return self.dl[n][key]
        raise KeyError(repr(key)+' appears in no dictionary')
    
    def __setitem__(self,key,value):
        for n in range(len(self.dl)-1,-1,-1):
            if key in self.dl[n]:
                self.dl[n][key]=value
                return None
        self.dl.append(dict({key:value}))
        
    def __call__(self,key):
        call_list = []
        for n in range(len(self.dl)):
            if key in self.dl[n]:
                call_list.append((n,self.dl[n][key]))
        return call_list
    
    def __iter__(self):
        itered_set=set()
        for n in range(len(self.dl)-1,-1,-1):
            for item in sorted(self.dl[n].items(), key=(lambda item: item[0])):
                if not item[0] in itered_set:
                    itered_set.add(item[0])
                    yield item
    
    def __eq__(self,right):
        if type(right) is DictList:
            for d in right.dl:
                for key in d:
                    if not (key in self and self[key]==right[key]):
                        return False
            return True
        elif type(right) is dict:
            for d in self.dl:
                for key in d:
                    if not (key in right and self[key]==right[key]):
                        return False
            return True
        else:
            raise TypeError('DictList.__eq__: == is not supported between'+type_as_str(self)+' and '+type_as_str(right))
                        
                    
    def __add__(self,right):
        if type(right) is DictList:
            return DictList(dict((item for item in self)), dict((item for item in right)))
        elif type(right) is dict:
            return DictList(*(d for d in self.dl.copy()),right.copy())
        else:
            raise TypeError('DictList:__add__: + operation is not supported between '+type_as_str(self)+' and '+type_as_str(right))  
    
    def __radd__(self,left):
        if type(left) is dict:
            return DictList(left.copy(),*(d for d in self.dl.copy()))
        else:
            raise TypeError('DictList:__radd__: + operation is not supported between '+type_as_str(self)+' and '+type_as_str(left))  




            
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
