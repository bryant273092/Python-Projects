from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self, *args):
        self.dl = []
        
        assert len(args) > 0, "args must have 1 or more items"
        
        for arg in args:
            assert type(arg) == dict, f"{arg} is not a dictionary"
            self.dl.append(arg)
            
    def __len__(self):
        count = 0
        used = set()
        for d in self.dl:
            for key in d:
                if key not in used:
                    count += 1
                    used.add(key)
        return count
    
    def __repr__(self):
        result = "DictList("
        for d in self.dl:
            result += str(d)
            result += ", "
        return result + ")"

    def __contains__(self, arg):
        for d in self.dl:
            for key in d:
                if key == arg:
                    return True
        return False

    def __getitem__(self, arg):
        in_there = False
        for d in self.dl:
            for key in d:
                if key == arg:
                    result = d[key]
                    in_there = True
        if in_there == False:
            raise KeyError
            
        return result
    
    def __setitem__(self, key, val):
        if self.__contains__(key) == True:
            for i in range(len(self.dl)):
                if key in self.dl[i]:
                    last = i
            self.dl[last][key] = val
            
        else:
            self.dl.append( {key: val} )
            
    def __call__(self, arg):
        result = []
        if self.__contains__(arg) == False:
            return result
        
        else:
            for i in range(len(self.dl)):
                for key in self.dl[i]:
                    if key == arg:
                        result.append( (i, self.dl[i][key]) )
                        
        return result
    
    def __iter__(self):
        result = []
        mini_result = []
        keys = set()
        
        for i in range(-1, -len(self.dl)-1, -1):
            for key in self.dl[i]:
                keys.add(key)
                
            for k in keys:
                mini_result.append( (k, self.__getitem__(k)))
            keys = set()
            
            for item in sorted(mini_result, key=lambda x: x[0]):
                if item in result:
                    continue
                result.append(item)
            mini_result = []
       
        for item in result:
            yield item
            
    def __eq__(self, right):
        self_keys = set()
        right_keys = set()
        
        if type(right) == DictList:
            for i in range(len(self.dl)):
                for key in self.dl[i]:
                    self_keys.add(key)
            for i in range(len(right.dl)):
                for key in right.dl[i]:
                    right_keys.add(key)
            if self_keys != right_keys:
                return False
            
            self_keys = list(self_keys)
            right_keys = list(right_keys)
            for i in range(len(self_keys)):
                if self.__getitem__(self_keys[i]) != right.__getitem__(right_keys[i]):
                    return False
                
            return True
            
        
        elif type(right) == dict:
            for i in range(len(self.dl)):
                for key in self.dl[i]:
                    self_keys.add(key)
            for key in right:
                right_keys.add(key)
            if self_keys != right_keys:
                return False
            
            self_keys = list(self_keys)
            right_keys = list(right_keys)
            for i in range(len(self_keys)):
                if self.__getitem__(self_keys[i]) != right[right_keys[i]]:
                    return False
            
            return True
        
        else:
            raise TypeError('right must be types DictList or dict')
            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
#     d0 = dict(a=1,b=2,c=3)
#     d1 = dict(c=13,d=14,e=15)
#     d2 = dict(e=25,f=26,g=27)
#     d  = DictList(d0,d1,d2)
#     produced = [i for i in d]
#     print(produced)

    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
