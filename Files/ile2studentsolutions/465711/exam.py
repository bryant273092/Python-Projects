from goody import type_as_str  # Useful in some exceptions
from operator import __add__

class DictList:
    def __init__(self,*args):
        assert len(args) != 0, 'DictList.__init___: None is not a dictionary'
        self.dl = []
        for arg in args:
            assert type(arg) is dict, f'DictList.__init__: {arg} is not a dictionary'
            self.dl.append(arg)
    
    def __len__(self):
        result = []
        for d in self.dl:
            for k in d.keys():
                result.append(k)
        return len(set(result))
    
    def __repr__(self):
        return 'DictList('+','.join(str(d) for d in self.dl)+')'
    
    def __contains__(self,key):
        for d in self.dl:
            if key in d.keys(): return True
        return False
    
    def __getitem__(self,key):
        result = None
        for d in self.dl:
            if key in d.keys():
                result = d[key]
        if result == None:
            raise KeyError(f'DictList.__getitem__: {key} appears in not dictionaries')
        else:
            return result
            
        
    
    def __setitem__(self,key,value):
        result = None
        new = dict()
        for d in self.dl[-1::-1]:
            if key in d.keys():
                d[key] = value
                result = key
                break
        if result == None:
            self.dl.append({key:value})
    
    def __call__(self,key):
        result = []
        for d in self.dl:
            if key in d.keys():
                t = (self.dl.index(d),d[key])
                result.append(t)
        return result
    
    def __iter__(self):
        def do_it(dl):
            result = dict()
            for d in dl[-1::-1]:
                for k,v in sorted(d.items()):
                    if k not in result.keys(): 
                        result[k] = v
            for k,v in result.items():
                yield (k,v)
        return do_it(list(self.dl))
            
    
    def __eq__(self,right):
        if type(right) not in (DictList,dict):
            raise TypeError(f'DictList.__eq__: {str(type(right))} invalid type to compare')
        lk = []
        for d in self.dl:
            for k,v in d.items():
                lk.append(k)
        if type(right) is DictList:
            rlk = []
            for rd in right.dl:
                for rk,rv in rd.items():
                    rlk.append(rk)
                    if rk not in lk:
                        return False
                    elif right[rk] != self[rk]:
                        return False
            if set(lk) != set(rlk):
                return False
            return True
        elif type(right) is dict:
            for k,v in right.items():
                if k not in lk:
                    return False
                elif right[k] != self[k]:
                    return False
            if set(right.keys()) != set(lk):
                return False
            return True
    
    def __add__(self,right):
        if type(right) is DictList:
            dleft,dright = dict(),dict()
            for d in self.dl.copy():
                for k,v in d.items():
                    dleft[k] = v
            for d in right.dl.copy():
                for k,v in d.items():
                    dright[k] = v
            return DictList(dleft,dright)
        elif type(right) is dict:
            dl_left = self.dl.copy()
            d_right = right.copy()
            return DictList(*dl_left,d_right)
        else:
            raise TypeError(f'DictList.__add__: unsupported type for add {str(type(right))}')
        
    def __radd__(self,left):
        if type(left) is dict:
            dl_right = self.dl.copy()
            d_left = left.copy()
            return DictList(d_left,*dl_right)
        elif type(left) is DictList:
            return __add__(self,left)
        else:
            raise TypeError(f'DictList.__radd__: unsupported type for add {str(type(left))}')
            



            
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
