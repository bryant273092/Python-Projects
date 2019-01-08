from goody import type_as_str  # Useful in some exceptions
from _operator import index

class DictList:
    
    def __init__(self, *args):
        self.dl = []
        assert len(args) != 0, f'DictList.__init__:No arguments given'
        for arg in args:
            assert type(arg) is dict, f'DictList.__init__:{arg} is not a dictionary'
            self.dl.append(arg)
    
    def __len__(self):
        found = []
        result = 0
        for d in self.dl:
            for key in d:
                if key not in found:
                    found.append(key)
                    result += 1
        return result
    
    def __repr__(self):
        return f"DictList({str(self.dl).strip('[]')})"
    
    def __contains__(self, *keys):
        for key in keys:
            for d in self.dl:
                if key in d:
                    return True
    
    def __getitem__(self, key):
        cval = None; found = False
        for d in self.dl:
            if key in d:
                found = True
                cval = d[key]
        if not found: raise KeyError('DictList.__getitem__: Key not found')
        else: return cval
        
    def __setitem__(self, key, val):
        index = -1
        for i, d in enumerate(self.dl):
            if key in d:
                index = i
        if index != -1: self.dl[index][key] = val
        else: self.dl.append({key:val})
            
    
    def __call__(self, key):
        tups = []
        for index, d in enumerate(self.dl):
            if key in d:
                tups.append((index, self.dl[index][key]))
        return tups
    
    def __iter__(self):
        tempres = []
        index = None
        found = set()
        for d in self.dl:
            for key in d:
                if key not in found:
                    for i2, d2 in enumerate(self.dl):
                        if key in d2:
                            index = i2
                    tempres.append((key, self.dl[index][key], index))
                    found.add(key)
        tempres = sorted(sorted(tempres, key = lambda x: x[0]), key = lambda x: x[2], reverse = True)
        result = [(res[0], res[1]) for res in tempres]
        return iter(result)
    
    def __eq__(self, right):
        if type(right) is DictList:
            for d in self.dl:
                for key in d:
                    if self.__getitem__(key) != right.__getitem__(key):
                        return False
        elif type(right) is dict:
            keys = []
            for index, d in enumerate(self.dl):
                keys.extend(list(self.dl[index].keys()))
            if keys != list(right.keys()):
                return False
            for key in right:
                if self.__getitem__(key) != right[key]:
                    return False
        else: raise TypeError('DictList.__eq__: Must compare Dictlist to Dictlist or Dict')
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
