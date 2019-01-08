from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        for d in args:
            if type(d) is not dict:
                raise AssertionError('DictList.__init__:' + str(d) + 'is not a dictionary')
            elif type(d) is dict: 
                if len(d) == 0:
                    raise AssertionError('DictList.__init__: dictionary contains no keys')
                else:
                    self.dl.append(d)

        if len(self.dl) == 0:
            raise AssertionError
            
    def __len__(self):
        dict_length = []
        for d in self.dl:
            for key in d:
                if key not in dict_length:
                    dict_length.append(key)
                    
        return len(dict_length)

    def __repr__(self):
        return 'DictList(' + ','.join(str(each) for each in self.dl) + ')'
    
    def __contains__(self, char):
        for d in self.dl:
            if char in d:
                return True
            
        return False
    
    def __getitem__(self, char):
        for d in self.dl[::-1]:
            if char in d:
                return d[char]
            
        raise KeyError
            
    def __setitem__(self, char, value):
        for d in self.dl[::-1]:
            if char in d:
                d[char] = value
                return
            
        self.dl.append({char:value})
        
        
    def __call__(self, char):
        list_of_tup = []
        for d in self.dl:
            if char in d:
                list_of_tup.append((self.dl.index(d),d[char]))
                
        if len(list_of_tup) != 0:
            return list_of_tup
        else:
            return []
        
        
    def __iter__(self):
        get_dict = dict()
        ordered_list = []
        
        for d in self.dl:
            for key, value in d.items():
                if key not in get_dict:
                    get_dict[key] = value
                else:
                    if value > get_dict[key]:
                        get_dict[key] = value
                 
        sort_dict = sorted(get_dict.items(), key=lambda x: x[0])                
        
        for d in self.dl[::-1]:
            for k, v in d.items():
                for (key, value) in sort_dict:
                    if key == k and v == value:
                        ordered_list.append((key, value))
        
        return iter(ordered_list)
                

    def __eq__(self, right):
        get_dict = []
        get_dict_2 = []
        for d in self.dl:
            for key, value in d.items():
                get_dict.append((key, value))
                
        if type(right) is dict:        
            for k, v in right.items():
                get_dict_2.append((k, v))
                if (k, v) not in get_dict:
                    return False
            
            get_dict.sort()
            get_dict_2.sort()
            
            if get_dict != get_dict_2:
                return False
            
        elif type(right) is DictList:
            for d in right:
                get_dict_2.append(d)
                
            get_dict.sort()
            get_dict_2.sort()
            
            if get_dict != get_dict_2:
                return False
            
        elif type(right) is not dict and type(right) is not DictList:
            raise TypeError
        
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
