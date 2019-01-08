from copy import deepcopy

class DictList:
    def __init__(self, *args):
        self.dl = []
        assert args != (), f"DictList.__init__: arguments({args}) should not be empty"
        for arg in args:
            assert type(arg) == dict, f"DictList.__init__: argument({arg}) is not a dictionary"
            self.dl.append(arg)
    
    def __len__(self):
        len_set = set()
        for dt in self.dl:
            for key in dt:
                len_set.add(key)
        return len(len_set)

    def __repr__(self):
        return f"DictList{tuple(self.dl)}"
    
    def __contains__(self, key):
        for dt in self.dl:
            for dt_key in dt:
                if dt_key == key:
                    return True
        return False
    
    def __getitem__(self, key):
        latest = dict()
        for dt in self.dl:
            for dt_key in dt:
                latest[dt_key] = dt[dt_key]
        if key in latest:
            return latest[key]
        else:
            raise KeyError(f"DictList.__getitem__: key({key}) is not valid")
        
    def __setitem__(self, key, value):
        key_set, location = set(), []
        for dt in self.dl:
            for tem_key in dt:
                key_set.add(tem_key)
                 
        if key in key_set:
            for dt in self.dl:
                for dt_key in dt:
                    if dt_key == key:
                        location.append(self.dl.index(dt))
            tem_dict = deepcopy(self.dl[location[-1]])
            tem_dict[key] = value
            self.dl[location[-1]] = tem_dict
        else:
            self.dl.append({key:value})

    def __call__(self, key):
        call_list = []
        for dt in self.dl:
            for dt_key in dt:
                if key == dt_key:
                    call_list.append((self.dl.index(dt), dt[dt_key]))
        return call_list
    
    def __iter__(self):
        gen_list = []
        def gen(bins):
            for dt in bins[::-1]:
                for dt_key in dt:
                    if dt_key not in gen_list:
                        gen_list.append(dt_key)
                        yield (dt_key, dt[dt_key])
        return gen(self.dl)
    
    def __eq__(self, right):
        if type(right) not in [dict, DictList]:
            raise TypeError(f"DictList.__eq__: right({right}) must be dict or DictList")
            
        latest, right_latest = dict(), dict()
        for tem_dt in self.dl:
            for tem_key in tem_dt:
                latest[tem_key] = tem_dt[tem_key]
        if type(right) == DictList:
            for tem_right_dt in right.dl:
                for tem_right_key in tem_right_dt:
                    right_latest[tem_right_key] = tem_right_dt[tem_right_key]
        else:
            for tem_right_key in right:
                right_latest[tem_right_key] = right[tem_right_key]
                
        if set(latest) == set(right_latest):
            for dt_key in latest:
                if latest[dt_key] != right[dt_key]:
                    return False
            return True
        else:
            return False

    def __add__(self, right):
        args_list = []
        if type(right) in [DictList, dict]:
            tem_self = deepcopy(self.dl)
            for left_dt in tem_self:
                args_list.append(left_dt)
                
            if type(right) == dict:
                tem_right = deepcopy(right)
                args_list.append(tem_right)
            else:
                for right_dt in right.dl:
                    args_list.append(right_dt)
        else:
            raise TypeError(f"DictList.__add__: right({right}) must be dict or DictList")
        return DictList(*args_list)
    
    def __radd__(self, left):
        args_list = []
        if type(left) == dict:
            tem_self, tem_left = deepcopy(self.dl), deepcopy(left)
            args_list.append(tem_left)
            for dt in tem_self:
                args_list.append(dt)
        else:
            raise TypeError(f"DictList.__add__: left({left}) must be dict")
        return DictList(*args_list)
        
        
            
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
