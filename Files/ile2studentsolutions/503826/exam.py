from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        if len(args) == 0:
            raise AssertionError('Must have at least one dict parameter')
        for i in args:
            if type(i) != dict:
                raise AssertionError(str(i) + ' is not a dict')
            else:
                self.dl.append(i)
    
    def __len__(self):
        unique_list = []
        for i in self.dl:
            for key in i.keys():
                if key not in unique_list:
                    unique_list.append(key)
        return len(unique_list)
    
    def __repr__(self):
        output = type(self).__name__ + '('
        for i in self.dl:
            output += str(i) + ', '
        return output[0:len(output)-1] +')'
    
    def __contains__(self, key):
        for i in self.dl:
            if key in i.keys():
                return True
        return False
        
    def __getitem__(self, key):
        key_value = None
        for i in self.dl:
            for test in i.keys():
                if key == test:
                    key_value = i[key]
        if key_value == None:
            raise KeyError('Key does not exist')
        else:
            return key_value
        
    def __setitem__(self, key, value):
        dicts_with_key = []
        for i in range(len(self.dl)):
            if key in self.dl[i].keys():
                dicts_with_key.append(i)
        if len(dicts_with_key) == 0:
            d = {}
            d[key] = value
            self.dl.append(d)
        else:
            self.dl[dicts_with_key[-1]][key] = value 
    
    def __call__(self, k):
        output = []
        for i in range(len(self.dl)):
            if k in self.dl[i].keys():
                output.append((i, self.dl[i][k]))
        return output
    
    def __iter__(self):
        i = len(self.dl) - 1
        while i >= 0:
            for key in sorted(self.dl[i].keys()):
                repeat = False
                for j in range(len(self.dl)):
                    if key in self.dl[j].keys() and j > i:
                        repeat = True
                if repeat != True:
                    yield (key, self.dl[i][key])
            i -= 1
    
    def __eq__(self, right):
        key_val_dict = {}
        for i in self.dl:
            for key in i.keys():
                key_val_dict[key] = self[key]
        if type(right) == dict:
            return right == key_val_dict
        elif type(right) == DictList:
            right_key_val_dict = {}
            for i in right.dl:
                for key in i.keys():
                    right_key_val_dict[key] = right[key]
            return right_key_val_dict == key_val_dict                   
        else:
            raise TypeError('Must be equated to a dict or dictlist') 
    
    def __add__(self, to_add):
        copy_self = eval(repr(self))
        key_val_dict = {}
        for i in copy_self.dl:
            for key in i.keys():
                key_val_dict[key] = copy_self[key]
           
        if type(to_add) == dict:
            args = []
            for i in copy_self.dl:
                args.append(i)
            args.append(to_add)
            return DictList(*args)
        elif type(to_add) == DictList:
            right_key_val_dict = {}
            for i in to_add.dl:
                for key in i.keys():
                    right_key_val_dict[key] = to_add[key]
            return DictList(key_val_dict, right_key_val_dict)                   
        
        raise TypeError('Must be equated to a dict or dictlist')
    
    def __radd__(self, to_add):
        copy_self = eval(repr(self))
        if type(to_add) != dict:
            raise TypeError('Must be a dict')
        else:
            args = []
            args.append(to_add)
            for i in copy_self.dl:
                args.append(i)
            return DictList(*args)
    
            
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
