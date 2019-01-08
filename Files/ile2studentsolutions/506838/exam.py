from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *dictionaries):
        if len(dictionaries) == 0:
            raise AssertionError('DictList cannot be initialized without any dictionaries.')
        self.dl = list()
        for item in dictionaries:
            assert type(item) == dict, 'DictList.__init__: \'' + str(item) + '\' is not a dictionary.'
            self.dl.append(item)
    
    def __len__(self):
        temp_set = set()
        for item in self.dl:
            for key in item:
                temp_set.add(key)
        return len(temp_set)
    
    def __repr__(self):
        return 'DictList(' + ', '.join([str(item) for item in self.dl]) + ')'
    
    def __contains__(self, key):
        for item in self.dl:
            if key in item:
                return True
        return False
    
    def __getitem__(self, key):
        for item in self.dl[::-1]:
            if key in item:
                return item[key]
        raise KeyError('DictList does not contain ' + str(key))
        
    def __setitem__(self, key, value):
        try:
            temp_value = self.__getitem__(key)
            for item in self.dl[::-1]:
                if key in item and temp_value == item[key]:
                    item[key] = value
        except KeyError:
            self.dl.append({key:value})
                
    def __call__(self, key):
        temp_list = list()
        for item in self.dl:
            if key in item:
                temp_list.append((self.dl.index(item), item[key]))
        return sorted(temp_list, key = lambda x: x[0])
    
    def __iter__(self):
        def _gen(master_list):
            for i in master_list:
                yield i
        
        master_list = list()
        temp_list = list()
        temp_set = set()
        for item in self.dl[::-1]:
            for key in item:
                if key not in temp_set:
                    temp_set.add(key)
                    temp_list.append((key, item[key]))
            master_list.extend(sorted(temp_list, key = lambda x: x[0]))
            temp_list = []        
        return _gen(master_list)
    
    def __eq__(self, right):
        if type(right) not in [dict, DictList]:
            raise TypeError('The item being compared is not a dictionary nor a DictList, therefore it cannot be compared.')
        else:
            for item in self.dl:
                for key in item:
                    if key not in right:
                        return False
                    elif key in right and self[key] != right[key]:
                        return False
            return True
    
    def keys(self):
        temp_set = set()
        for item in self.dl:
            for key in item:
                temp_set.add(key)
        return list(temp_set)
    
    def __add__(self, right):
        if type(right) == DictList:
            temp_dict_1 = {key: self[key] for key in self.keys()}
            temp_dict_2 = {key: right[key] for key in right.keys()}
            return DictList(temp_dict_1, temp_dict_2)
        elif type(right) == dict:
            return eval(self.__repr__().rstrip(')') + ', ' + str(right) + ')')
        else:
            raise TypeError('You cannot add anything to a DictList that is not a dictionary nor a DictList')
            
    def __radd__(self, left):
        if type(left) == DictList:
            return self + left
        elif type(left) == dict:
            return eval('DictList(' + str(left) + ', ' + self.__repr__().strip('DictList('))
        else:
            raise TypeError('You cannot add anything to a DictList that is not a dictionary nor a DictList')


            
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
