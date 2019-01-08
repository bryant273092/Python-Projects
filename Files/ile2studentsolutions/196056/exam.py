# Useful in some exceptions

class DictList:
    def __init__(self, *args):
        assert len(args) != 0, 'DictList.__init__:' + str(args) + 'is not a dictionary'
        for arg in args:
            if type(arg) != dict:
                raise AssertionError
            assert type(arg) == dict , 'DictList.__init__:' + str(args) + 'is not a dictionary'  
        self.dl = [arg for arg in args]

    def __len__(self):
        unique_keys = set()
        for d in self.dl:
            for key in d:
                unique_keys.add(key)
        return len(unique_keys)
    
    def __repr__(self):
        return 'DictList('+','.join(str(d) for d in self.dl)+')'

    def __contains__(self, index):
        for d in self.dl:
            if index in d:
                return True
        return False

    def __getitem__(self, index):
        value = None
        for d in self.dl:
            if index in d:
                value = d[index]
        if value == None:
            raise KeyError('Key does not exist')
        else:
            return value
        
    def __setitem__(self, index, value):
        for n in range(1, len(self.dl)+1):
            if index in self.dl[-n]:
                self.dl[-n][index] = value
                return;
        self.dl.append({index: value})
                    
    def __call__(self, index):
        key_dl = []
        for n in range(len(self.dl)):
            if index in self.dl[n]:
                key_dl.append((n, self.dl[n][index]))
        return key_dl
    
    def __iter__(self):
        keys_iterated = []
        list_to_yield = []
        for n in range(1, len(self.dl)+1):
            for key in self.dl[-n]:
                if key in keys_iterated:
                    pass
                else:
                    keys_iterated.append(key)
                    list_to_yield.append((key, self.dl[-n][key]))
        for x in list_to_yield:
            yield x
    def __eq__(self, right):
        if type(right) == DictList:
            final_val_self = dict()
            final_val_right = dict()
            for n in range(len(self.dl)):
                for k in self.dl[n]:
                    final_val_self[k] = self.dl[n][k]
            for n in range(len(right.dl)):
                for k in right.dl[n]:
                    final_val_right[k] = right.dl[n][k]
            return final_val_self == final_val_right
            for key in final_val_self:
                if key not in final_val_right or final_val_self[key] != final_val_right[key]:
                    return False
                return True
        elif type(right) == dict:
            final_val_self = {}
            for n in range(len(self.dl)):
                for k in self.dl[n]:
                    final_val_self[k] = self.dl[n][k]
            for key in final_val_self:
                if key not in right or final_val_self[key] != right[key]:
                    return False
            return True
        else:
            raise TypeError('DictList must compare to DictList or dict')
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
