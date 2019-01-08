from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *kargs):
        if kargs == None or kargs == () or kargs == {}:
            raise AssertionError
        try:
            self.dl = []
            for arg in kargs:
                if type_as_str(arg) != 'dict':
                    raise AssertionError
                else:
                    self.dl.append(arg)
        except TypeError:
            raise AssertionError
        
    def __len__(self):
        length_list = []
        for d in self.dl:
            for key in d.keys():
                if key not in length_list:
                    length_list.append(key)
        return len(length_list)
    
    def __repr__(self):
        string = 'DictList('
        for d in self.dl:
            string += '{'
            for key, value in d.items():
                string += "'{}':{}, ".format(key, value)
            string += '}, '
        string.rstrip(', ')
        string += ')'
        return string
    
    def __contains__(self, arg):
        for d in self.dl:
            for key in d.keys():
                if arg == key:
                    return True
        return False
    
    def __getitem__(self, arg):
        item = None
        for d in self.dl:
            for key, value in d.items():
                if arg == key:
                    item = value
        if item == None:
            raise KeyError
        else:
            return item
        
    def __setitem__(self, k, v):
        last_key_in = None
        for d in self.dl:
            for key in d.keys():
                if k == key:
                    last_key_in = self.dl.index(d)
        if last_key_in == None:
            self.dl.append(dict([(k, v)]))
        else: 
            self.dl[last_key_in][k] = v
    
    def __call__(self, arg):
        tuple_list = []
        for d in self.dl:
            for key, value in d.items():
                if arg == key:
                    tuple_list.append((self.dl.index(d), value))
        return tuple_list
    
    def __iter__(self):
        iter_list = []
        for d in reversed(self.dl):
            for key, value in d.items():
                replaced = False
                for (a, b) in iter_list:
                    if key == a:
                        index = iter_list.index((a, b))
                        iter_list[index] = (key, value)
                        replaced = True
                if replaced == False:
                    iter_list.append((key, value))
        for item in iter_list:
            yield item
            
    def __eq__(self, right):
        eq = 0
        if type_as_str(right) == 'dict':
            for d in self.dl:
                for key, value in d.items():
                    for k, v in right.items():
                        if key == k:
                            if value == v:
                                eq += 1
            if len(right.keys()) == eq:
                return True
            else:
                return False
        elif type_as_str(right) == 'exam.DictList':
            right_len = 0
            right_keys = []
            for d in self.dl:
                for (k, v) in right:
                    if k not in right_keys:
                        right_len += 1
                        right_keys.append(k)
                    for key, value in d.items():
                        if k == key:
                            if v == value:
                                eq += 1
            if right_len == eq:
                return True
            else:
                return False
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
