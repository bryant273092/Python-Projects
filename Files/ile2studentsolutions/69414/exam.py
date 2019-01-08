class DictList:
    def __init__(self, *args):
        self.dl = []
        if (len(args) == 0):
            raise AssertionError('DictList.__init__: no dictionaries entered')
        for item in args:
            if type(item) is not dict:
                raise AssertionError('DictList.__init__:\'{}\'is not a dictionary'.format(item))
            else:
                self.dl.append(item)
        
    def __len__(self):
        num = set()
        for item in self.dl:
            for k,v in item.items():
                num.add(k)
        return len(num)
    
    def __repr__(self):
        dict_str = 'DictList('
        for item in self.dl:
            if item == self.dl[-1]:
                dict_str += str(item)
            else:
                dict_str += str(item) + ',' 
        dict_str += ')'
        return dict_str
    
    def __contains__(self, arg):
        for item in self.dl:
            if arg in item.keys():
                return True
        return False
    
    def __getitem__(self, arg):
        new_dict = {}
        for item in self.dl:
            for k,v in item.items():
                new_dict[k] = v
                
        if arg not in new_dict.keys():
            raise KeyError('DictList.__getitem__: key not in dict')
        return new_dict[arg]
    
    def __setitem__(self, key, value):
        indexer = 0
        count = 0
        for item in self.dl:
            for k,v in item.items():
                if key == k:
                    indexer = self.dl.index(item)
                    count += 1
        if count == 0:
            self.dl.append({key: value})
        else:
            self.dl[indexer][key] = value
            
    def __call__(self, arg):
        return_list = []
        for item in self.dl:
            for k,v in item.items():
                if arg == k:
                    return_list.append((self.dl.index(item), v))
                    
        return return_list
    
    def __iter__(self):
        letter_set = set()
        new_list = iter(self.dl[-1::-1])
        for item in new_list:
            for k,v in item.items():
                if k not in letter_set:
                    yield (k,v)
                    letter_set.add(k)
                else:
                    pass

        return
    
    def __eq__(self, right):
        if type(right) not in (DictList, dict):
            raise TypeError('DictList.__eq__: right operand must be type DictList or dict')
        
        if type(right) is DictList:
            for item in self.dl:
                for k in item:
                    try:
                        if self.__getitem__(k) == right.__getitem__(k):
                            pass
                        else:
                            return False
                    except KeyError:
                        return False
            return True
        
        elif type(right) is dict:
            for item in self.dl:
                for k in item:
                    try:
                        if self.__getitem__(k) == right[k]:
                            pass
                        else:
                            return False
                    except KeyError:
                        return False
            return True
    
    def __add__(self, right):
        dict1 = {}
        dict2 = {}
        
        if type(right) not in (DictList, dict):
            raise TypeError('DictList.__add__: right operand must be type DictList or dict')
        
        if type(right) is DictList:
            for item in self.dl:
                for k, v in item.items():
                    dict1[k] = v
            for item in right.dl:
                for k, v in item.items():
                    dict2[k] = v
            return DictList(dict1, dict2)
        
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
