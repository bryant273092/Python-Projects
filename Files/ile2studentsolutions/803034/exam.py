
class DictList:
    def __init__(self, *args):
        if len(args) == 0 or not all([type(i) == dict for i in args]):
            raise AssertionError
        self.dl = [i for i in args if type(i) == dict]
        
    def keys_helper(self):
        uniq = set()
        for d in self.dl:
            for key in d.keys():
                uniq.add(key)
        return uniq
        
    def __len__(self):
        uniq = self.keys_helper()
        return len(uniq)

    def __repr__(self):
        return f"DictList({','.join([str(i) for i in self.dl])})"
    
    def __contains__(self, key):
        ans = []
        for d in self.dl:
            ans += [key in d] 
        return any(ans)
        
    
    def __getitem__(self, key):
        has = []
        if not self.__contains__(key): raise KeyError(f"'{key}' appears in no dictionary")
        for d in self.dl:
            if key in d:
                has.append([d, key, d[key]])
        return sorted(has, key = lambda x: x[2])[-1][2]
    
    def __setitem__(self, key, val):
        has = []
        if not self.__contains__(key):
            self.dl.append({key:val})
            return
        for d in self.dl:
            if key in d:
                has.append(d)
        has[-1].update({key:val})
        
    def __call__(self, key):
        if not self.__contains__(key):
            return []
        has = []
        for d in self.dl:
            if key in d:
                has.append((self.dl.index(d), d[key])) 
        return has      
    
    def __iter__(self):
        ans = []
        all_k = self.keys_helper()
        for key in all_k:
            ans.append([key, max(self.__call__(key), key = lambda x: x[1])])
        for i in sorted(ans, key=(lambda x: (-x[1][0], x[0]))):
            yield (i[0], i[1][1])
            
    def __eq__(self, right):
        eqs = []
        if type(right) not in [dict, DictList] : raise TypeError(f"{right} is type {type(right).__name__}, should be DictList")
        keys_helper = self.keys_helper()
        right_keys = right.keys_helper() if type(right) == DictList else {i for i in right.keys()}
        if keys_helper != right_keys: return False
        for key in keys_helper:
            eqs.append(self.__getitem__(key) == right.__getitem__(key))
        return all(eqs)


            
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
