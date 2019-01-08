from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self, *dicts):
        self.dl = []
        if not dicts:
            raise AssertionError('DictList.__init__: no dictionaries were given.')
        for d in dicts:
            assert type(d) == dict, f'DictLis.__init__: \'{d}\' is not a dictionary.'
            self.dl.append(d)
            
        
    def __len__(self):
        kset = set()
        for d in self.dl:
            for key in d:
                kset.add(key)
        return len(kset)
    
    
    def __repr__(self):
        #return "DictList(" + str(list(d for d in self.dl).join(',')) + ")"
        return "DictList({})".format(*[d for d in self.dl])
    
    
    def __contains__(self, item):
        for d in self.dl:
            if item in d:
                return True
        return False
    
    
    def __getitem__(self, item):
        max_index = None
        for d in self.dl:
            if item in d:
                max_index = self.dl.index(d)
                
        if max_index != None:
            return self.dl[max_index][item]
        else:
            raise KeyError('DictList.__getitem__: key does not exist in any dictionary in the DictList')
        
        
    def __setitem__(self, item, value):
        max_index = None
        for d in self.dl:
            if item in d:
                max_index = self.dl.index(d)
                
        if max_index != None:
            self.dl[max_index][item] = value
        else:
            self.dl.append({item: value})
            
            
    def __call__(self, key):
        return_list = []
        for d in self.dl:
            if key in d:
                return_list.append((self.dl.index(d), self.dl[self.dl.index(d)][key]))
        return return_list
    
    
    def __iter__(self):
        def dl_gen():
            kset = set()
            for d in self.dl[::-1]:
                for key in sorted(d):
                    if key not in kset:
                        kset.add(key)
                        yield (key, d[key])
        
        return dl_gen()
    
    
    def __eq__(self, right):
        try:
            if type(right) == DictList or type(right) == dict:
                skeyset = set()
                for d in self.dl:
                    for key in d:
                        skeyset.add(key)                  
                for key in skeyset:
                    assert self[key] == right[key]           
            else:
                raise TypeError('DictList.__eq__: right operand must be either of type DictList or type dict.')
            
            return True
            
        except:
            return False
        
        
    def __add__(self, right):
        if type(right) == DictList:
            sdict = {}
            rdict = {}
            for d in self.dl:
                for key in d:
                    if key not in sdict:
                        sdict[key] = self[key]
            for d in right.dl:
                for key in d:
                    if key not in rdict:
                        rdict[key] = right[key]
            return DictList(sdict, rdict)
        
        elif type(right) == dict:
            dldicts = []
            for d in self.dl:
                dldicts.append(d)
            dldicts.append(right)
            
            return DictList(*dldicts)
        
        else:
            raise TypeError('DictList.__add__: right operand must be either of type DictList or type dict.')
        
        
    def __radd__(self, left):
        return self + left
        



            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d = DictList(dict(a=1,b=2,c=3), dict(c=13,d=14,e=15), dict(e=25,f=26,g=27))
    print(len(d), repr(d))
    print(d.dl, d['c'])
    d['c'] = 'new_c'
    d['z'] = 'new_z'
    print(d.dl)
    print(d('e'))
    print(sorted(d.dl[2]))

    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
