from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = list()
        assert len(args) != 0, f'DictList.__init__: {args} is not a dictionary.'
        for arg in args:
            assert type(arg) == dict, f'DictList.__init__: {arg} is not a dictionary.'
            self.dl.append(arg.copy())
            
    def __len__(self):
        result = list()
        for dic in self.dl:
            for k in dic.keys():
                if k not in result:
                    result.append(k)
        return len(result)

    def __repr__(self):
        result = 'DictList('
        for d in self.dl:
            result += str(d) + ','
        result = result[:-1] +')'
        return result
    
    def __contains__(self, key):
        for d in self.dl:
            if key in d.keys():
                return True
        return False
    
    def __getitem__(self,key):
        result = None
        for d in self.dl:
            if key in d.keys():
                result = d[key]
        if result == None:
            raise KeyError (f"DictList.__getitem__: '{key}' appears in no dictionaries. ")
        return result

    def __setitem__(self, key, value):
        i = []
        n = 0
        for d in self.dl:
            if key in d.keys():
                i.append(n)
            n += 1
        if i == []:
            d = {key: value}
            self.dl.append(d)
        else:
            self.dl[i[-1]][key] = value
          
    def __call__(self, key):
        result = list()
        i = 0
        for d in self.dl:
            if key in d.keys():
                result.append((i,d[key]))
            i +=1
        return result  
    
    def __iter__(self):
        i = -1 
        result = dict()
        for n in range(len(self.dl)):
            for key in sorted(self.dl[i].keys()):
                if key not in result.keys():
                    result[key] = self.dl[i][key]
            i -= 1
        result = list(result.items())
        for i in result:
            yield i
     
    def _keys(self):
        keys = list()
        for d in self.dl:
            for k in d.keys():
                if k not in keys:
                    keys.append(k) 
        return keys
           
    def __eq__(self, right):
        if type(right) not in [DictList, dict]:
            raise TypeError (f'DictList.__eq__: {right} is not a DictList or dict.')
        keys = self._keys()
        for k in keys:
            try:
                if self[k] != right[k]:
                    return False
            except:
                return False
        return True
        
    def __add__(self,right):
        if type(right) == DictList:
            lkeys = self._keys()
            ld = dict()
            for k in lkeys:
                ld[k] = self[k]
            rkeys = right._keys()
            rd = dict()
            for k in rkeys:
                rd[k] = right[k]
            return DictList(ld,rd)
        elif type(right) == dict:
            result = DictList(self.dl[0].copy())
            for i in range(1,len(self.dl)):
                result.dl.append(self.dl[i].copy())
            result.dl.append(right.copy())
            return result    
        else:
            raise TypeError(f'DictList.__add__: {right} is not a Dictlist or dict.')
    
    def __radd__(self, left):
        if type(left) == DictList:
            lkeys = self._keys()
            ld = dict()
            for k in lkeys:
                ld[k] = self[k]
            rkeys = left._keys()
            rd = dict()
            for k in rkeys:
                rd[k] = left[k]
            return DictList(ld,rd)
        elif type(left) == dict:
            result = DictList(left.copy())
            for i in range(len(self.dl)):
                result.dl.append(self.dl[i].copy())
            return result    
        else:
            raise TypeError(f'DictList.__add__: {left} is not a Dictlist or dict.')
                
            
        

            

        



            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d0 = dict(a=1,b=2,c=3)
    d1 = dict(c=13,d=14,e=15)
    d    = DictList(d0,d1)
    drep = eval(repr(d))

    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
