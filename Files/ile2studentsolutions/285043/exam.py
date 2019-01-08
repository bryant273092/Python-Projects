from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl = []
        if args == ():
            raise AssertionError("empty argument")
        for arg in args:
            if type(arg) != dict:
                raise AssertionError("argument not a dict")
        for arg in args:
            self.dl.append(arg)
    
    def __len__(self):
        answer = set()
        for item in self.dl:
            for key in item.keys():
                answer.add(key)
        return len(answer)
    
    def __repr__(self):
        return "DictList(" + ",".join(str(d) for d in self.dl) + ')'
    
    def __contains__(self,key):
        for d in self.dl:
            if key in d.keys():
                return True
        return False
    
    def __getitem__(self,key):
        if key not in self:
            raise KeyError("Key not in dictionary")
        for dict1 in self.dl[::-1]:
            if key in dict1:
                return dict1[key]
    
    def __setitem__(self, key, value):
        if key in self:
            for dict1 in self.dl[::-1]:
                if key in dict1.keys():
                    dict1[key] = value
                    break
        else:
            self.dl.append({key:value})
    
    def __call__(self, key):
        answer = []
        for item in range(len(self.dl)):
            if key in self.dl[item]:
                answer.append((item, self.dl[item][key]))
        return answer
    
    def __iter__(self):
        once_key = set()
        for dict1 in self.dl[::-1]:
            for k,v in sorted(dict1.items()):
                if k not in once_key:
                    once_key.add(k)
                    yield(k,v)
                    
    def __eq__(self,right):
        if type(right) not in (DictList,dict):
            raise TypeError("argument must be a dictlist object or dict")
        for key,value in self:
            if key not in right or right[key] != value:
                return False
        return True
    
    def __add__(self,right):
        if type(right) not in (DictList,dict):
            raise TypeError
        if type(right) is DictList:
            return DictList(dict(item for item in self), dict(item for item in right))
        elif type(right) is dict:
            return DictList(*self.dl,right)
    
    def __radd__(self,right):
        if type(right) not in (DictList,dict):
            raise TypeError
        return DictList(right,*self.dl)
        

if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test


    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()
