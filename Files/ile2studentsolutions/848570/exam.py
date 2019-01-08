from goody import type_as_str  # Useful in some exceptions
from _ast import arg

class DictList:
    def __init__(self, *args):
        if not(len(args)):
            raise AssertionError('At least one dictionary must be given as an argument')
        for arg in args:
            if type(arg) != dict:
                raise AssertionError('Each argument must be a dictionary')
        self.dl = []
        for arg in args:
            self.dl.append(arg)
    
    def __len__(self):
        distinct_keys = set()
        for d in self.dl:
            for k in d:
                distinct_keys.add(k)
        return len(distinct_keys)
    
    def __repr__(self):
        return 'DictList('+','.join(str(d) for d in self.dl)+')'

    def __contains__(self,target):
        result = False
        for d in self.dl:
            for k in d:
                if k == target:
                    result = True
        return result
    
    def __getitem__(self,target):
        for d in self.dl[::-1]:
            for k in d:
                if k == target:
                    return d[k]
        raise KeyError('key not found in any dictionaries')
    
    def __setitem__(self,key,value):
        if self.__contains__(key):
            finished = False
            for d in self.dl[::-1]:
                for k in d:
                    if k == key and not(finished):
                        finished = True
                        d[k] = value
        else:
            self.dl.append({key:value})
    
    def __call__(self,key):
        return [(i,self.dl[i][key]) for i in range(len(self.dl)) if key in self.dl[i]]
    
    def __iter__(self):
        L = []
        unique = set()
        for d in self.dl[::-1]:
            for k in sorted(d):
                if k not in unique:
                    unique.add(k)
                    L.append((k,d[k]))
        for t in L:
            yield t
    
    def __eq__(self,right):
        def create_unique(dl_obj):
            return set(k for i in range(len(dl_obj.dl)) for k in dl_obj.dl[i])
        if type(right) == DictList:
            if not(create_unique(self) == create_unique(right)): return False
        elif type(right) == dict:
            if not(create_unique(self) == set(k for k in right)): return False
        for k in create_unique(self):
            if self[k] != right[k]:
                return False
        return True
    
    def __add__(self,right):
        def create_unique(dl_obj):
            return set(k for i in range(len(dl_obj.dl)) for k in dl_obj.dl[i])
        if type(right) == DictList:
            adict = dict()
            bdict = dict()
            for k in create_unique(self):
                adict[k] = self[k]
                bdict[k] = right[k]
            return DictList(adict,bdict)
        elif type(right) == dict:
            copy_d = dict()
            arg = []
            for d in self.dl:
                new_d = dict()
                for k in d:
                    new_d[k] = d[k]
                arg.append(new_d)
            for k in right:
                copy_d[k] = right[k]
            return DictList(*arg,copy_d)
        else:
            raise TypeError('Can only add DictList with another, or DictList with dict')
    
    def __radd__(self,left):
        if type(left) == dict:
            arg = []
            copy_d = dict()
            for d in self.dl:
                new_d = dict()
                for k in d:
                    new_d[k] = d[k]
                    arg.append(new_d)
            for k in left:
                copy_d[k] = left[k]
            return DictList(copy_d,*arg)
        else:
            raise TypeError('Can only add DictList with another, or DictList with dict')
    
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
