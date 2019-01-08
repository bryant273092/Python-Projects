from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*dicts):
        self.dl = []
        assert len(dicts) >= 1, "DictList.__init__: have no dictionaries"
        for d in dicts:
            assert type(d) is dict,"DictList.__init__: {} is not a dictionary".format(d)
            self.dl.append(d)
    
    def __len__(self):
        temp = []
        for d in self.dl:
            for k in d.keys():
                if k not in temp:
                    temp.append(k)
        return len(temp)

    def __repr__(self):
        return "DictList({})".format(",".join(str(d) for d in self.dl))

    def __contains__(self,item):
        for d in self.dl:
            if item in d.keys():
                return True
        return False
    
    def __getitem__(self,item):
        result = None
        for d in self.dl:
            if item in d.keys():
                result = d[item]
        if result is None:
            raise KeyError("{} appears in no dictionaries".format(item))
        else:
            return result
        
    def __setitem__(self,item,value):
        i = len(self.dl)-1
        change = False
        while i >= 0:
            if item in self.dl[i].keys():
                self.dl[i][item] = value
                change = True
                break
            else:
                i = i - 1
        if not change:
            self.dl.append({item:value})
        
    def __call__(self,item):
        result = []
        for index,d in enumerate(self.dl):
            if item in d.keys():
                result.append((index,d[item]))
        return result
    
    def __iter__(self):
        temp = []
        i = len(self.dl)-1
        while i >= 0:
            for k in sorted(self.dl[i].keys()):
                if k not in temp:
                    temp.append(k)
                    yield (k,self.dl[i][k])
            i = i-1
            
    def __eq__(self,right):
        temp = []
        for d in self.dl:
            for k in d.keys():
                temp.append(k)
        temp = set(temp)
        if type(right) is DictList:
            result = []
            for d in right.dl:
                for k in d.keys():
                    result.append(k)
            result = set(result)
            if temp != result:
                return False
            for k in temp:
                if self.__getitem__(k) != right.__getitem__(k):
                    return False
            return True
        elif type(right) is dict:
            if temp != right.keys():
                return False
            for k,v in right.items():
                if self.__getitem__(k) != v:
                    return False
            return True
        else:
            raise TypeError("The right operand type {} is neither a dict nor a DictList".format(type_as_str(right)))
                    
    def __add__(self,right):
        if type(right) is DictList:
            temp1 = {}
            for d in self.dl:
                for k in d.keys():
                    if k not in temp1.keys():
                        temp1[k] = self.__getitem__(k)
            temp2 = {}
            for d in right.dl:
                for k in d.keys():
                    if k not in temp2.keys():
                        temp2[k] = right.__getitem__(k)
            return DictList(temp1,temp2)
        elif type(right) is dict:
            return DictList(*self.dl.copy(),right.copy())
        else:
            raise TypeError("The right operand type {} is neither a dict nor a DictList".format(type_as_str(right)))
        
        
    def __radd__(self,left):
        if type(left) is DictList:
            temp1 = {}
            for d in self.dl:
                for k in d.keys():
                    if k not in temp1.keys():
                        temp1[k] = self.__getitem__(k)
            temp2 = {}
            for d in left.dl:
                for k in d.keys():
                    if k not in temp2.keys():
                        temp2[k] = left.__getitem__(k)
            return DictList(temp2,temp1)
        elif type(left) is dict:
            return DictList(left.copy(),*self.dl.copy())
        else:
            raise TypeError("The left operand type {} is neither a dict nor a DictList".format(type_as_str(left)))
    
        
        
        
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
    #driver.batch_self_check()
