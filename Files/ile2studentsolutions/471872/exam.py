from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self, *args):
        self.dl = list()
        if len(args) == 0:
            raise AssertionError ('DictList.__init__: Requires at least on dictionary argument')
        for arg in args:
            if type(arg) is not dict:
                raise AssertionError ('DictList.__init__:' + str(arg) + 'is not a dictionary')
            self.dl.append(arg)

    def __len__(self):
        rpts = set()
        qty = 0
        for item in self.dl:
            for k in item.keys():
                if k in rpts:
                    pass
                else:
                    qty += 1
                    rpts.add(k)
        return qty 
    
    def __repr__(self):
        return 'DictList(' + ','.join(str(d) for d in self.dl) + ')'
 
    def __contains__(self, item):
        for d in self.dl:
            if item in d.keys():
                return True
        else:
            return False
        
    def __getitem__(self, item):
        val = 'error'
        for d in self.dl:
            if item in d.keys():
                val = d[item]
        if val == 'error':
            raise KeyError (str(item) + ' does not appear in any dictionaries')
        return val
    
    def __setitem__(self, item, val):
        index = None
        for loc, d in enumerate(self.dl):
            if item in d.keys():
                index = loc
        if index == None:
            self.dl.append({item:val})
        else:
            self.dl[index][item] = val 
            
    def __call__(self, item):
        iteml = []
        for loc, d in enumerate(self.dl):
            if item in d.keys():
                iteml.append((loc, d[item]))
        return iteml
    
    
    def __iter__(self):
        rpt = set()
        for i in range(len(self.dl)):
            for k,v in sorted(self.dl[len(self.dl) - 1 - i].items()):
                if k in rpt:
                    pass
                else:
                    yield ((k, v))
                    rpt.add(k)


    def __eq__(self, right):
        
        if not isinstance(right, (DictList, dict)):
            raise TypeError ('DictList.__eq__: Cannot compare a ' + type(right) + ' to a DictList')
        else:    
            if isinstance(right, DictList):
                for item in right.dl:
                    for k in item.keys():
                        if not self.__contains__(k):
                            return False
                        if self.__getitem__(k) != right.__getitem__(k):
                            return False
            elif isinstance(right, dict):
                for item in self.dl:
                    for k in item.keys():
                        if k in right.keys() and self.__getitem__(k) == right[k]:
                            pass
                        else:
                            return False
        return True
    
    def __add__(self, right):
        ld = dict()
        rd = dict()
        for itm in self.dl:
            for k,v in itm.items():
                ld[k] = v
        if isinstance(right, DictList):                    
            for itm in right.dl:
                for k,v in itm.items():
                    rd[k] = v
        elif isinstance(right, dict):
            return eval(self.__repr__()[:-1] + ',' + str(right) + ')')
        else:
            raise TypeError ('DictList.__add__: Can not add ' + type(right)  + ' to a DictList')
        return eval('DictList(' + str(ld) + ',' + str(rd) + ')')
    
    def __radd__(self, left):
        if not isinstance(left, (dict)):
            raise TypeError ('DictList.__add__: Can not add ' + type(left)  + ' to a DictList')
        return eval('DictList(' + str(left) + ',' + self.__repr__()[9:])                        
        
    

            
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
