from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self, *args):
        self.dl = []
        assert len(args) > 0, "There are no arguments."
        for i in args:
            assert type(i) == dict, f"{i} is not a dictionary."
            self.dl.append(i)
            
    def __len__(self):
        u_keys = set()
        for d in self.dl:
            for k, v in d.items():
                u_keys.add(k)
                
        return len(u_keys)
    
    def __repr__(self):
        total_str = 'DictList('
        for i in self.dl:
            dict_str = 'dict('
            for k, v in i.items():
                kv_str = f"{k}={v},"
                dict_str += kv_str
            dict_str = dict_str[:-1] + '),'
            total_str += dict_str
        total_str = total_str[:-1] + ')'
        return total_str
            
    def __contains__(self, arg):
        for i in self.dl:
            if arg in i:
                return True
        return False
    
    def __getitem__(self, arg):
        for i in sorted(self.dl, key=lambda x: self.dl.index(x) , reverse=True):
            if arg in i:
                return i[arg]
        raise KeyError
    
    def __setitem__(self, arg, value):
        for i in sorted(self.dl, key=lambda x: self.dl.index(x) , reverse=True):
            if arg in i:
                i[arg] = value
                return
        new_dict = {f'{arg}': value}
        self.dl.append(new_dict)

    def __call__(self, arg):
        tl = []
        for i in range(len(self.dl)):
            if arg in self.dl[i]:
                tl.append((i, self.dl[i][arg]))
        return tl

    def __iter__(self):
        check = set()
        for i in sorted(self.dl, key=lambda x: self.dl.index(x) , reverse=True):
            for k, v in sorted(i.items()):
                if k not in check:
                    check.add(k)
                    yield (k,v)
                    
    def __eq__(self, right):
        if type(right) == DictList:
            for k,v in right:
                try:
                    if v != self.__getitem__(k):
                        return False
                except KeyError:
                    return False
            for k,v in self.__iter__():
                try:
                    if v != right.__getitem__(k):
                        return False
                except KeyError:
                    return False
            return True
        elif type(right) == dict:
            for k, v in right.items():
                try:
                    if v != self.__getitem__(k):
                        return False
                except KeyError:
                    return False
            for k, v in self.__iter__():
                try:
                    if v != right[k]:
                        return False
                except KeyError:
                    return False    
            return True
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
