from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        assert len(args) > 0
        for arg in args:
            if type(arg) is dict:
                self.dl.append(arg)
            else: raise AssertionError("DictList.__init__:'" + str(arg) + "' is not a dictionary")
    
    def __len__(self):
        distinct = set()
        for dic in self.dl:
            for key in dic: distinct.add(key)
        return len(distinct)
    
    def __repr__(self):
        args = ''
        for dic in self.dl:
            args += str(dic) + ', '
        return 'DictList(' + args.rstrip(',') + ')'
    
    def __contains__(self, key):
        found = False
        for dic in self.dl:
            if key in dic.keys(): found = True
        return found
    
    def __getitem__(self, key):
        values = []
        for dic in self.dl:
            if key in dic: values.append(dic[key])
        if len(values) == 0: raise KeyError("DictList.__getitem__:'" + str(key) + "' appears in no dictionaries")
        else: return values[-1]
    
    def __setitem__(self, name, value):
        found = False
        count = -1
        for dic in self.dl[::-1]:
            if name in dic: 
                self.dl[count][name] = value
                found = True
                break
            count -= 1
        if not found: self.dl.append({name:value})
    
    def __call__(self, key):
        result = []
        for n in range(len(self.dl)):
            if key in self.dl[n]: result.append((n, self.dl[n][key]))
        return result
    
    def __iter__(self): 
        used = set()
        count = -1
        for dic in self.dl[::-1]:
            for key in dic:
                if key not in used:
                    used.add(key)
                    yield (key, self.dl[count][key])
            count -=1
    
    def __eq__(self, right):
        if type(right) is dict:
            self_keys = set(key for dic in self.dl for key in dic)
            right_keys = set(right.keys())
            if len(self_keys) != len(right_keys): return False
            for key in self_keys:
                if self.__getitem__(key) != right[key]: return False
            return True
        elif type(right) is DictList:
            self_keys = set(key for dic in self.dl for key in dic)
            right_keys = set(key for dic in right.dl for key in dic)
            if len(self_keys) != len(right_keys): return False
            for key in self_keys:
                if self.__getitem__(key) != right.__getitem__(key): return False
            return True  
        else: raise TypeError("DictList.__eq__:'" + str(right) + "' is not a DictList or dictionary and is of type " + type_as_str(right))

    
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
