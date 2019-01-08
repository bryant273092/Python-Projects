class DictList:
    def __init__(self,*args):
        if args == (): raise AssertionError
        for i in args:
            if not (type(i) is dict):
                assert False, 'DictList.__init__: {} is not a dictionary'.format(str(*args))
        self.dl = list(args)
        
    def __len__(self):
        s = set()
        for i in self.dl:
            for j in i:
                s.add(j)
        return len(s)
    def __repr__(self):
        return 'DictList('+','.join(str(i) for i in self.dl)+')'
    def __contains__(self,a):
        for i in self.dl:
            if a in i:
                return True
        return False
    def __getitem__(self,a):
        n_dic = dict()
        for i in self.dl:
            if a in i:
                n_dic[a] = i[a]
        if n_dic == {}: raise KeyError
        return n_dic[a]
    def __setitem__(self,k,v):
        count = 0
        n_dl = list(reversed(self.dl))
        for i in n_dl:
            if k in i:
                count += 1
                i[k] = v
                break
        d = dict()
        d[k]=v
        if count == 0: self.dl.append(d)
        else: self.dl = list(reversed(n_dl))
    def __call__(self,k):
        a = []
        for i in range(1,len(self.dl)+1):
            if k in self.dl[i-1]:
                a.append((i-1,self.dl[i-1][k]))
        return a
    def __iter__(self):
        a = []
        n_dl = list(reversed(self.dl))
        for i in n_dl:
            i = sorted(i)
        for j in n_dl:
            for k in j:
                if k in a: continue
                else: 
                    a.append(k)
                    yield (k,self.__getitem__(k))
    def __eq__(self,right):
        if not (type(right) is DictList or type(right) is dict): raise TypeError
        for i in self.dl:
            for j in i:
                a = self.__getitem__(j)
                if j in right and right[j] == a:
                    continue
                else: return False
        return True
    def __add__(self,right):
        if not (type(right) is DictList or type(right) is dict): raise TypeError
        f_dic = dict()
        s_dic = dict()
        if type(right) is DictList:
            for i in self.dl:
                for j in i:
                    if j in f_dic: continue
                    f_dic[j] = self.__getitem__(j)
            for k in right.dl:
                for l in k:
                    if l in s_dic: continue
                    s_dic[l] = right[l]
            return eval('DictList('+str(f_dic)+','+str(s_dic)+')')
        elif type(right) is dict:
            return eval('DictList('+','.join([str(i) for i in self.dl])+','+str(right)+')')
    def __radd__(self,left):
        if not (type(left) is DictList or type(left) is dict): raise TypeError
        if type(left) == dict:
            return eval('DictList('+str(left)+','+','.join([str(i) for i in self.dl])+')')
        return self+left
                
                
        
        
    
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
