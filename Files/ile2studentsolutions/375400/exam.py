from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self, *kargs):
        if len(kargs) == 0:
            raise AssertionError
        for arg in kargs:
            if not type(arg) is dict:
                raise AssertionError(f"DictList.__init: '{arg}' is not a dictionary")
        self.dl = []
        for arg in kargs:
            self.dl.append(arg)
            
    def __len__(self):
        result = set()
        for d in self.dl:
            for k in d:
                result.add(k)
        return len(result)
    
    def __repr__(self):
        msg = []
        for d in self.dl:
            msg.append(str(d))
        return f"DictList({','.join(msg)})"
    
    def __contains__(self, key):
        for d in self.dl:
            for k in d:
                if k == key:
                    return True
        return False
    
    def __getitem__(self, index):
        if all(index not in d for d in self.dl):
            raise KeyError(f"'{index} appears in no dictionaries'")
        for d in self.dl:
            if index in d:
                answer = d[index]
        return answer
    
    def __setitem__(self, index, value):
        if all (index not in d for d in self.dl):
            new_dict = dict()
            new_dict[index] = value
            self.dl.append(new_dict)
        else:
            for d in self.dl[::-1]:
                if index in d:
                    d[index] = value
                    break
        
    def __call__(self, index):
        result = []
        for i in range(len(self.dl)):
            if index in self.dl[i]:
                result.append((i,self.dl[i][index]))
        return result
    
    def __iter__(self):
        history = []
        for d in self.dl[::-1]:
            for k, v in sorted(d.items()):
                if k not in history:
                    yield (k,v)
                    history.append(k)
    
    def __eq__(self, right):
        if type(right) is DictList:
            keys = set()
            right_keys = set()
            for d in self.dl:
                for k in d:
                    keys.add(k)
            for d in right.dl:
                for k in d:
                    right_keys.add(k)
            if keys != right_keys:
                return False
            else:
                for k in list(keys):
                    if self[k] != right[k]:
                        return False
                return True
        elif type(right) is dict:
            keys = set()
            for d in self.dl:
                for k in d:
                    keys.add(k)
            if keys != set(right.keys()):
                return False
            else:
                for k in list(keys):
                    if self[k] != right[k]:
                        return False
                return True
        else:
            raise TypeError(f"{right} is {type_as_str(right)}, is not a DictList or dict")
        
    def __add__(self,right):
        if type(right) is DictList:
            new_dict_1 = dict()
            keys = set()
            for d in self.dl:
                for k in d:
                    keys.add(k)
            for k in list(keys):
                new_dict_1[k] = self[k]
            
            new_dict_2 = dict()
            keys_2 = set()
            for d in right.dl:
                for k in d:
                    keys_2.add(k)
            for k in list(keys_2):
                new_dict_2[k] = right[k]
            return DictList(new_dict_1, new_dict_2)
        elif type(right) is dict:
            new_dict_tuple = (d.copy() for d in self.dl.copy())
            return DictList(*(new_dict_tuple),right.copy())
        else:
            raise TypeError(f"{right} is not a dict or DictList")
        
    def __radd__(self, left):
        if type(left) is dict:
            new_dict_tuple = (d.copy() for d in self.dl.copy())
            return DictList(left.copy(), *(new_dict_tuple))
        else:
            raise TypeError(f"{left} is not a dict or DictList")
            
        
            


            
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
