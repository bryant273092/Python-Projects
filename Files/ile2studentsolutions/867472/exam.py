from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        if len(args) == 0:
            raise AssertionError('DictList.__init__: There are no dictionaries')
        else:
            for i in args:
                if type_as_str(i) != 'dict':
                    raise AssertionError(f'DictList.__init__: {i} is not a dictionary')
                
        self.dl = args

    def __len__(self):
        _dl_len = set()
        for k in self.dl:
            for keys in k:
                _dl_len.add(keys)
        return len(_dl_len)
    
    def __repr__(self):
        return f'DictList({self.dl})'
    
    def __contains__(self, item):
        for k in self.dl:
            for keys in k:
                if item == keys:
                    return True
        return False
     
    def __getitem__(self, item):
        _dl_key = dict()
        _index = 0
        for k in self.dl:
            for keys in k:
                if item == keys:
                    _dl_key[item] = _index
            _index += 1
        
        if len(_dl_key) == 0: # there is no keys found
            raise KeyError(f'DictList.__getitem__: {item} is not a key in the dictionary')
        elif len(_dl_key) == 1: # there is only 1 key found
            return self.dl[_dl_key[item]][item]
        elif len(_dl_key) >= 2: # there is more than 1 key found
            pass
     
    def __setitem__(self, item, right):
        _index = len(self.dl) - 1
        for k in self.dl[-1:]:
            if item in k.keys():
                self.dl[_index][item] = right
            elif item not in k.keys():
                self.dl[item] = right
            _index -= 1
            
    def __call__(self, item):
        _result = list()
        _index = 0  
        for keys in self.dl:
            for k in keys:
                if item == k:
                    _result.append((_index,keys[k]))
            _index += 1
        
        return _result
    
    def __iter__(self):
        _result = list()
        for d in self.dl[-1:]:
            for k,v in d:
                _result.append((k,v))
        return iter(_result)
     
    def __eq__(self, right):
        if (type_as_str(right) != 'exam.DictList') and (type_as_str(right) != 'dict'):
            raise TypeError(f'DictList.__eq__: {right} is neither a DictList nor a dict. {right} is {type_as_str(right)}')
        elif (type_as_str(right) == 'exam.Dictlist'):
            return self.dl == right.dl
        elif (type_as_str(right) == 'dict'):
            return self.dl == right
        return True
    
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
