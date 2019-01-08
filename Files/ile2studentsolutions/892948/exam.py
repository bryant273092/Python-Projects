from goody import type_as_str  # Useful in some exceptions
import prompt

class DictList:
    
    def __init__(self, *arg):
        self.dl = []
        for dic in arg:
            if type(dic) is dict: self.dl.append(dic)
            else: raise AssertionError(f"'{dic}' is not a dictionary")
        if self.dl == []: raise AssertionError('No Parameters Given')
            
    def __len__(self):
        keys = set()
        for d in self.dl:
            for key in d: keys.add(key)
        return len(keys)
    
    def __repr__(self):
        return "DictList(" + str([i for i in self.dl])[1:-1] + ")"
    
    def __contains__(self, name):
        for t in self.dl:
            for key in t:
                if key is name: return True
        return False
    
    def __getitem__(self, name):
        temp = self.dl[::-1]
        for res in temp:
            if name in res: return res[name]
        raise KeyError
    
    def __setitem__(self, name, val):
        try:
            self.__getitem__(name)
        except:
            self.dl.append({name:val})
        else:
            for i in self.dl[::-1]:
                if name in i: 
                    i[name]  = val
                    break
                
    def __call__(self, name):
        res = []
        count = 0
        for i in self.dl:
            if name in i: res.append((count, i[name]))
            count += 1
        return res
            
    def __iter__(self):
        res = []
        for d in self.dl[::-1]:
            for k in d:
                if k not in res:
                    res.append(k)
        for key in res:
            most = max(i[1] for i in self.__call__(key))
            yield (key, most)
    
    def __eq__(self, left):
        if type(left) is DictList:
            l_comp = [i for i in left]
            r_comp = [i for i in self]
            return set(l_comp) == set(r_comp)
        if type(left) is dict:
            l_comp = [i for i in DictList(left)]
            r_comp = [i for i in self]
            return set(l_comp) == set(r_comp)
        else: raise TypeError(f"'{left}' is not a DictList or dict type argument")              
            
            
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
