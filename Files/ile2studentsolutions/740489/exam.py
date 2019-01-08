from goody import type_as_str  # Useful in some exceptions
def simplify(lis):
    thedict = {}
    for d in lis:
        for k in d:
            if k not in thedict:
                thedict.update({k:d[k]})
            else:
                thedict[k] = d[k]
    return thedict
class DictList:
    def __init__(self,*args):
        if len(args) == 0:
            raise AssertionError("Empty parameter")
        self.dl = []
        for d in args:
            if type(d) != dict:
                raise AssertionError("DictList.__init__: "+str(d)+" is not a dictionary")
            else:
                self.dl.append(d)

    def __len__(self):
        newkeys = []
        for d in self.dl:
            for k in d:
                if k not in newkeys:
                    newkeys.append(k)
                else:
                    pass
        return len(newkeys)
    
    def __repr__(self):
        reprstr = "DictList("
        for d in self.dl[0:-1]:
            reprstr += str(d)+","
        reprstr += str(self.dl[-1])+")"
        return reprstr
    
    def __contains__(self,value):
        for d in self.dl:
            if value in d.keys():
                return True
        return False 
    
    def __getitem__(self,index):
        nlis = self.dl.copy()
        x = nlis.reverse()
        for d in nlis:
            for k in d:
                if k == index:
                    return d[k] 
        raise KeyError
    def __setitem__(self,index,value):
        nlis = self.dl.copy()
        x = nlis.reverse()
        for d in nlis:
            for k in d:
                if k == index:
                    d[k] = value
                    y = nlis.reverse()
                    self.dl = nlis
                    return
    def __call__(self,value):
        result = []
        for d in self.dl:
            if value in d.keys():
                result.append((self.dl.index(d),d[value]))
        return result
    def __iter__(self):
        def get(lis):
            lis.reverse()
            yielded = []
            for d in lis:
                for k in d:
                    if k not in yielded:
                        yielded.append(k)
                        yield (k,d[k])
        return get(self.dl)
    

    def __eq__(self,right):
        if type(right) == DictList:
            origdict = simplify(self.dl)
            rightdict = simplify(right.dl)
            if set(origdict.keys()) == set(rightdict.keys()):
                for k1 in origdict.keys():
                    if origdict[k1] != rightdict[k1]:
                        return False
                return True
            else:
                return False
        if type(right) == dict:
            origdict = simplify(self.dl)
            if set(origdict.keys()) == set(right.keys()):
                for k1 in origdict.keys():
                    if origdict[k1] != right[k1]:
                        return False
                return True
            else:
                return False
        else:
            raise TypeError
    def __add__(self,right):
        if type(right) == DictList:
            leftdict = simplify(self.dl)
            rightdict = simplify(right.dl)
            return DictList(leftdict,rightdict)
        if type(right) == dict:
            args = tuple(self.dl)
            return DictList(*args,right)
        else:
            raise TypeError
    
    def __radd__(self,left):
        if type(left) == dict:
            args = tuple(self.dl)
            return DictList(left,*args)
        else:
            raise TypeError
            
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
