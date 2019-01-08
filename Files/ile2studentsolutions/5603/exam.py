from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *param):
        assert len(param) > 0
        for p in param:
            assert type(p) == dict
        self.dl = []
        for d in param:
            self.dl.append(d)
            
    def __len__(self):
        final = []
        for d in self.dl:
            final = final + list(d)   
        final = len(set(final))

        return final

    def __repr__(self):
        s = ''
        for d in self.dl:
            if len(self.dl) == 1:
                s += str(d)
            else:
                s += str(d) + ', '
        return 'DictList(' + s + ')'

    def __contains__(self, thing):
        x = []
        for d in self.dl:
            if thing in d:
                return True
            
    def __getitem__(self, i):
        if i not in self: #check
            raise KeyError
        ret = []
        for d in self.dl:
            if i in d:
                ret.append(d[i])
        return ret[-1]
    
    def __setitem__(self, k, v):
        info = []
        if k in self:
            for d in self.dl:
                if k in d:
                    info.append(self.dl.index(d))
            last_index = info[-1]
            self.dl[last_index][k] = v
        else:
            new = {k: v}
            self.dl.append(new)
            
    def __call__(self, k):
        if k not in self:
            return []
        ret_lst = []
        for d in self.dl:
            if k in d:
                ret_lst.append((self.dl.index(d), self.dl[self.dl.index(d)][k]))
        return ret_lst
    
    def __iter__(self):
        unique = []
        fin = []
        for d in self.dl:
            fin.append(sorted(list(d.items())))
   
        lenn = len(fin) - 1
        for ind in range(lenn, -1, -1):   #-1 for first one
            for x in fin[ind]:
                
                if x[0] not in unique:
                    yield x
                    unique.append(x[0])
            
    def __eq__(self, d2):
        if type(d2) != DictList and type(d2) != dict:
            raise TypeError
        first = set()
        second = set()
        for d in self:
            first.add(d[0] in d2)
        for d1 in self:
            if d1[0] in d2:
                val_from_d2 = d2[d1[0]]
#                 print(d[1])
#                 print(val_from_d2)
#                 q = d[1] == val_from_d2
                second.add(d1[1] == val_from_d2)
            
        return all(first) and all(second)
    
    def __add__(self, r):
        if type(r) not in (DictList, dict):
            raise TypeError
        if type(r) == DictList:
            left = {}
            right = {}
            for d in self:
                left[d[0]] = d[1]
            for d in r:
                left[d[0]] = d[1]
             
            return DictList(left, right)


        
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
