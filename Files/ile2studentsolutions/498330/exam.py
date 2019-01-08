from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        assert len(args) != 0
        for a in args:
            assert type(a) == dict, str(a) + ' is type ' + type_as_str(a) + ' ...should be type dict' 
            self.dl.append(a)
            
    def __len__(self):
        count = 0
        c = set()
        for d in self.dl:
            for k in d:
                c.add(k)
        for i in c:
            count += 1
        return count
    
    def __repr__(self):
        x = []
        for d in self.dl:
            x.append(str(d))
        return 'DictList('+ ', '.join(x) + ')' 
        
    def __contains__(self,key):
        for d in self.dl:
            if key in d:
                return True
        return False
    
    def __getitem__(self,key):
        ind = []
        if self.__contains__(key) == False:
            raise KeyError()
        for d in self.dl:
            if key in d:
                ind.append(self.dl.index(d))
        
        return self.dl[max(ind)][key]
        
    def __setitem__(self, key, value):
        ind = []
        if self.__contains__(key) == False:
            self.dl.append({key:value})
        for d in self.dl:
            if key in d:
                ind.append(self.dl.index(d))
        self.dl[max(ind)][key] = value
    
    def __call__(self, key):
        l = []
        for d in self.dl:
            if key in d:
                l.append((self.dl.index(d), d[key]))
        return l
    
    def __iter__(self):
        l = []
        ind = {}
        for d in self.dl:
            for k in d:
                if k not in ind:
                    ind[k] = [self.dl.index(d)]
                else:
                    ind[k].append(self.dl.index(d))
        
        for k in sorted(ind, key = lambda x: max(ind[x]), reverse = True):
            l.append((k, self.dl[max(ind[k])][k]))
        
        for i in l:
            yield i
        
    
    def __eq__(self, right):
        if type(right) != DictList and type(right) != dict:
            raise TypeError(str(right) + ' is type ' + type_as_str(right) + ' ...should be type DictList')
        ans = []
        
        for d in self.dl:
            for k in d:
                if right.__contains__(k) == False:
                    return False

                if d[k] == right[k]:
                    ans.append(True)
                else:
                    ans.append(False)
        if False in ans:
            return False
        else:
            return True
        
                
                
        
    
     
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
