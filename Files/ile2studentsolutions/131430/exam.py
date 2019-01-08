from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *dlist):
        self.dl = []
        if len(dlist) == 0:
            raise AssertionError
        for d in dlist:
            #print(f'd is {d}')
            if type(d) is not dict:
                raise AssertionError ('DictList.__init__: \'{}\' is not a dictionary'.format(dlist))
            else:
                self.dl.append(d)
    
    def __len__(self):
        the_len = set()
        for d in self.dl:
            for key in d:
                the_len.add(key)
        return len(the_len)
            
    def __repr__(self):
        st = 'DictList('
        for index in self.dl:
            st += str(index) + ','
        st2 = st[:-1]
        st2 += ')'
        return st2
        #return DictList()
     
    def __contains__(self, st):
        for index in self.dl:
            for key in index:
                if st == key:
                    return True
        return False        

    def __getitem__(self, item):
        #d['c'] = new2
        try:
            greater = []
            for index in self.dl:
                for k, v in index.items():
                    #print(f'k is {k}, v is {v}')
                    for key, val in greater:
                        if k == item:
                            if v > val:
                                greater.pop(0)
                                greater.append((k, v))
                    if item == k:
                        greater.append((k, v))
                                
            return greater[0][1]
        except (KeyError, IndexError):
            raise KeyError
                
        #print(f'greater has {greater}')        
    def __setitem__(self, item, value):
        #d['b'] = 'new1'
        greater = []
        num = 0
        for index in self.dl:
            for k, v in list(index.items()):
                #print(f'k is {k}, v is {v}')
                for key, val in greater:
                    if k == item:
                        #print('break point')
                        if type(v) is int:
                            if v > val:
                                greater.pop(0)
                                greater.append((k, v))
                                index[item] = value         
                if item == k:
                     greater.append((k, v))
                if len(greater) != 0:
                    index[item] = value
                else:
                    self.dl.append({item:value})
        
        #print(f'greater has {greater}')
        pass

  
    def __call__(self, item):
        freq = []
        count = 0
        for index in self.dl:
            for key in index:
                if item == key:
                    freq.append((count, index[item])) 
            count +=1
        #print(f'freq contains {freq}')
        return freq

    def __iter__(self):
        out = []
        a = set()
        for index in self.dl:
            for k, v in index.items():
                out.append((k, v))
                #print(f'k is {k}, v is {v}')
                for i in range(len(out)):
                    if k == out[i][0]:
                        if v > out[i][1]:
                            print(out[i][1])
                            out.pop(i)
                            break
    
        for t in sorted(out, key = lambda x: x[0]):
            yield t
    
    def __eq__(self, right):
        if type(right) is not DictList or type(right) is not dict:
            raise TypeError
        if type(right) == dict:
            for key in self.dl:
                if self.dl[key] <= right[key]:
                    continue
                if self.dl[key] != right[key]:
                    return False
              
            pass
                     
    
    
       
        

            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d = DictList(dict(a=1,b=2,c=3), dict(c=13,d=14,e=15), dict(e=25, f=26, g=27))
    #d = DictList(dict(a=1,b=2,c=3))
    print(f'dl is {d.dl}')
    print([i for i in d])
    #print(d('a'))
    #d['b'] = 'new1'


    
    

    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
