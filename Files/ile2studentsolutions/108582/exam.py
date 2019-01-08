from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        for arg in args:
            if type(arg) != dict:
                raise AssertionError('DictList.__init__: {} is not a dictionary'.format(arg))
            elif len(arg) == 0:
                raise AssertionError('DictList.__init__ requires dictionaries')
            else:
                self.dl = args

                
    def __len__(self):
        keys = []
        for item in self.dl:
            for key in item.keys():
                if key not in keys:
                    keys.append(key)
        return len(keys)
    
    def __repr__(self):
        dl_str = ''
        for item in self.dl:
            if self.dl.index(item) == -1:
                dl_str += str(item)
            else:
                dl_str += str(item) + ','
        return 'DictList({})'.format(dl_str)
    
    def __contains__(self, key):
        return key in [item for item in set([key for item in self.dl for key in item.keys()])]
    
    def __getitem__(self, key):
        for item in self.dl:
            try:
                return item[key]
            except:
                raise KeyError('{} appears in no dictionaries'.format(key))
    
    def __setitem__(self, key, val):
        for item in self.dl:
            if key in item.keys():
                for k, v in item.items():
                    if key == k:
                        item[key] = val
                        return self.dl
                    else:
                        pass
  
    def __call__(self, key):
        for item in self.dl:
            if key not in item.keys():
                return []
    
    def __iter__(self):
        for item in self.dl:
            for elem in item:
                yield (elem, item[elem])
    
    def __eq__(self, right):
        if type(self) not in [DictList, dict] and type(right) not in [DictList, dict]:
            raise TypeError('Arguments are invalid types')
        elif type(self) not in [DictList, dict] or type(right) not in [DictList, dict]:
            raise TypeError('Argument is invalid type')
        elif type(self) == DictList and type(right) == dict:
            self_keys = []
            for item in self.dl:
                for key in item.keys():
                    if key not in self_keys:
                        self_keys.append(key)
            return self_keys == list(right.keys())
        elif type(self) == dict and type(right) == dict:
            return list(self.keys()) == list(right.keys())
        elif type(self) == DictList and type(right) == DictList:
            self_keys = [set([key for item in self.dl for key in item.keys()])]
            right_keys = [set([key for item in right.dl for key in item.keys()])]
            return self_keys == right_keys
            
                        
        
                





            
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
