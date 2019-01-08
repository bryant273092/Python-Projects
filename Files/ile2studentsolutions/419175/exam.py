from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        if args == '':
            raise AssertionError("DictList.__init__: 'abc' is not a dictionary.")
        for i in args:
            if type(i) != dict:
                raise AssertionError("DictList.__init__: 'abc' is not a dictionary.")
            else:
                self.dl.append({k:v for k,v in i.items()})
        
        
    def __len__(self):
        count = set()
        for i in self.dl:
            for k in i:
                count.add(k)
        return len(count)
    
    def __repr__(self):
        rep = 'DictList('
        for i in self.dl:
            rep += str(i) + ', '
        rep.rstrip(', ')
        rep += ')'
        return rep
        
    def __contains__(self, value):
        for i in self.dl:
            if value in i:
                return True
        return False
    
    def __getitem__(self, k):
        max_ind = 0
        for i in self.dl:
            if k in i:
                max_ind = i[k]
        if max_ind == 0:
            raise KeyError       
        return max_ind

    def __setitem__(self, k, v):
        count = -1
        for i in self.dl:
            count += 1
            if k in i:
                pass
            else:
                self.dl.append({k:v})
            self.dl[count][k] = v
    
    
    def __call__(self, k):
        count = 0
        alist = []
        for i in self.dl:
            if k in i:
                alist.append((count, i[k]))   
            count += 1
        return alist
    
    def __iter__(self):
        alist = []
        for i in sorted(self.dl, reverse = True):
            for val in i.items():
                if val not in alist:
                    alist.append(val)
        return alist
    
    def __eq__(self, d1):
        d1keys = set()
        d2keys = set()
        for i in d1:
            for k in i:
                d1keys.add(k)
        for i2 in self.dl:
            for k in i2:
                d2keys.add(k)
        for is1 in d1keys():
            for is2 in d2keys():
                if d1[is1] != self.dl[is2]:
                    return False
        if d1keys != d2keys:
            return False
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
