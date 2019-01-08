from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl = []
        if len(args) == 0:
            raise AssertionError('init:no dict at all')
        for ele in args:
            if isinstance(ele, dict):
                self.dl.append(ele)
            else:
                raise AssertionError('init:not dict in the parameter')
    def __len__(self):
        r = []
        for d in self.dl:
            r.extend(d.keys())
        return len(set(r))
    def __repr__(self):
        r = 'DictList('
        for ele in self.dl:
            r += str(ele)+','
        return r+')'
    def __contains__(self,k):
        for d in self.dl:
            if k in d.keys():
                return True
        return False
    def __getitem__(self,key):
        r = None
        for d in self.dl:
            if d.get(key) != None:
                r = d.get(key)
        if r != None:
            return r
        elif r == None:
            raise KeyError
    def __setitem__(self,nk,nv):
        for x in range(len(self.dl)-1,-1,-1):
            if nk in self.dl[x].keys():
                self.dl[x][nk] = nv
                return
        self.dl.append({nk:nv})
        return
    def __call__(self,k):
        r = []
        for d in range(len(self.dl)):
            if k in self.dl[d].keys():
                r.append((d,self.dl[d][k]))
        return r
    def __iter__(self):
        ced = set()
        for x in range(len(self.dl)-1,-1,-1):
            for key in sorted(self.dl[x].keys()):
                if key not in ced:
                    yield (key,self.dl[x][key])
                    ced.add(key)
    def __eq__(self,right):
        sk=[]
        rk=[]
        for d in self.dl:
            sk.extend(d.keys())
        if isinstance(right,DictList):
            for d in right.dl:
                rk.extend(d.keys())
        elif isinstance(right, dict):
            rk = set(right.keys())
        else:
            raise TypeError('== only legal between dict and dictlist')
        if set(sk) != set(rk):
            return False
        else:
            for key in sk:
                if self[key] != right[key]:
                    return False
            return True
    def __add__(self,right):
        nsd = dict()
        for d in self.dl:
            for k in d.keys():
                nsd[k] = self[k]
        if isinstance(right,DictList):
            nrd = dict()
            for d in right.dl:
                for ke in d.keys():
                    nrd[ke] = right[ke]
            return DictList(nsd,nrd)
        elif isinstance(right, dict):
            new = repr(self)[:-1]
            new = new + str(right) +')'
            return eval(new)
        else:
            raise TypeError('unable to add type other than dict and DictList')
    def __radd__(self,left):
        if isinstance(left, dict):
            new = 'DictList('+str(left)+','
            for d in self.dl:
                new +=str(d)+','
            return eval(new+')')
        else:
            raise TypeError('unable to add type other than dict and DictList')
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
