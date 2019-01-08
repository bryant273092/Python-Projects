from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*dl):
        assert len(dl) != 0 and type(dl[0]) == dict,'AssertionError'
        self.dl = dl
        
    def __len__(self):
        tot = []
        for i in self.dl:
            for j in i:
                if j not in tot:
                    tot.append(j)
        return len(tot)
    
    def __repr__(self):
        s = 'DictList('
        for num,i in enumerate(self.dl):
            if num == 0:
                s = s + str(i)
            else:
                s = s + ', {}'.format(i)
        return s+')'
    
    def __contains__(self,obj):
        is_in = False
        for i in self.dl:
            if obj in i:
                is_in = True
        return is_in
    
    def __getitem__(self,obj):
        tot = 0
        for i in self.dl:
            for j in i:
                if j == obj:
                    tot = i[j]
        #print(tot)
        if tot != 0:
            return tot
        else:
            raise KeyError()
        
    def __setitem__(self,k,s):
        ind = 0
        is_in = None
        if type(k) == str:
            for num,i in enumerate(self.dl):
                if k in i:
                    ind = num
                    is_in = True
            if is_in == True:
                self.dl[ind][k] = s
            else:
                self.dl.add({k:s})
                
    def __call__(self,obj):
        l = []
        for num,i in enumerate(self.dl):
            if obj in i:
                l.append((num,i[obj]))
        
        return sorted(l,key = lambda x: x[0])
    
    def __iter__(self):
        d = {}
        for i in self.dl:
            for j in i:
                if j not in d:
                    d[j] = [i[j]]
                else:
                    d[j].append(i[j])
        l = []
        #new_l = []
        for i in d:
            l.append((i,d[i][-1]))
        
        #l = sorted(l,reverse = True)
        for i in l:
            yield i       
        
    def __eq__(self,obj):
        if type(obj) not in [DictList,dict]:
            raise TypeError()
        d = {}
        for i in self.dl:
            d.update(i)
        
        if type(obj) == DictList:
            new_d = {}
            for j in obj.dl:
                new_d.update(j)
            return d == new_d
        elif type(obj) == dict:
            #print(self.dl)
            #return self.dl[0] == obj
            return d == obj
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
