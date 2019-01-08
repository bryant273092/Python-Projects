from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        #print(args)
        assert len(args) > 0, f'DictList.__init__: Expected 1 or more arguments, got 0'
        self.dl = []
        for arg in args:
            assert isinstance(arg, dict), f'DictList.__init__: {repr(arg)} is not a dictionary'
            self.dl.append(arg)
    
    def __len__(self):
        unique_keys = set()
        for dictionary in self.dl:
            unique_keys.update(dictionary.keys())
        return len(unique_keys)
    
    def __repr__(self):
        return f"DictList({', '.join(str(dictionary) for dictionary in self.dl)})"
    
    def __contains__(self, key):
        for dictionary in self.dl:
            if key in dictionary:
                return True
        return False
        
    def __getitem__(self, key):
        result = None
        for dictionary in self.dl:
            if key in dictionary:
                result = dictionary[key]
        if result is None:
            raise KeyError(f'{repr(key)} appears in no dictionaries')
        return result
    
    def __setitem__(self, key, value):
        for i in range(len(self.dl) - 1, -1, -1):
            if key in self.dl[i]:
                self.dl[i][key] = value
                break
        else:
            self.dl.append({key:value})
            
    def __call__(self, key):
        value_history = []
        for i in range(len(self.dl)):
            if key in self.dl[i]:
                value_history.append((i, self.dl[i][key]))
        return value_history
    
    def __iter__(self):
        def DictList_iter(dict_list: [{}]):
            yielded_keys = set()
            for i in range(len(dict_list) -1, -1, -1):
                for key, val in sorted(dict_list[i].items()):
                    if key not in yielded_keys:
                        yield (key, val)
                        yielded_keys.add(key)
                        
        return DictList_iter(self.dl)
    
    def __eq__(self, right):
        if type(right) is DictList or type(right) is dict:
            left_unique_keys = set()
            right_unique_keys = set()
            
            for dictionary in self.dl:
                left_unique_keys.update(dictionary.keys())
            
            if type(right) is DictList:
                for dictionary in right.dl:
                    right_unique_keys.update(dictionary.keys())
            else:
                right_unique_keys.update(right.keys())
                
            if left_unique_keys != right_unique_keys:
                return False
        
            for key in left_unique_keys:
                if self[key] != right[key]:
                    return False
                
            return True
            
        else:
            raise TypeError(f'DictList.__eq__: expected right argument to be a dictionary or dictlist'
                            f' got {repr(right)} instead')


            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    #d = DictList('abc')
    #d = DictList()
    #d = DictList([])
    #d = DictList(dict(a=1,b=2,c=3), dict(c=13,d=14,e=15), dict(e=25,f=26,g=27), 'cat')
#     d = DictList(dict(a=1,b=2,c=3), dict(c=13,d=14,e=15), dict(e=25,f=26,g=27))
#     print(len(d))
#     print(repr(d))
#     print(d)
#     g = repr(d)
#     print(g)
#     g = d.__iter__()
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     
#     
#     print('cat')
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
