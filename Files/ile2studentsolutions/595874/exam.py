from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self, *dics):
        self.dl = []
        if len(dics) == 0:
            raise AssertionError('No argument')
        for dic in dics:
            if type(dic) != dict:
                raise AssertionError('Needs to be type dict')
            self.dl.append(dic)

    def __len__(self):
        unique = []
        for dic in self.dl:
            for key in dic:
                unique.append(key)
        unique = set(unique)
        return len(unique)
            
    def __repr__(self):
        return 'DictList{}'.format(tuple(self.dl))
            
    def __contains__(self, item):
        for dic in self.dl:
            for key in dic:
                if item == key:
                    return True
        return False
            
            
    def __getitem__(self, item):
        all_keys = []
        for dic in self.dl:
            for key in dic:
                all_keys.append(key)
        if item not in all_keys:
            raise KeyError("key not found")
        key_value = None
        new_index = -1
        for indx, dic in enumerate(self.dl):
            for key in dic:
                if key == item:
                    if indx > new_index:
                        new_index = indx
                        key_value = self.dl[indx][key]
        return key_value

    def __setitem__(self, item, value):
        all_keys = []
        for dic in self.dl:
            for key in dic:
                all_keys.append(key)
        if item not in all_keys:
            self.dl.append({item:value})
        else:
            key_value = None
            new_index = -1
            for indx, dic in enumerate(self.dl):
                for key in dic:
                    if key == item:
                        if indx > new_index:
                            new_index = indx
                            key_value = key
            self.dl[new_index][key_value] = value

            
    
    def __call__(self, item):
        all_keys = []
        result = []
        for dic in self.dl:
            for key in dic:
                all_keys.append(key)
        if item not in all_keys:
            return result
        
        for indx, dic in enumerate(self.dl):
            for key in dic:
                if key == item:
                    result.append((indx, self.dl[indx][key]))
        return result
        
    
    def __iter__(self):
        iter_list = []
        for dic in sorted(self.dl, key = lambda item:self.dl.index(item)):
            for key in dic:
                iter_list.append((key, self[key]))
        iter_list = set(iter_list)
        iter_list = list(iter_list)
        iter_list = sorted(iter_list, key = lambda item : item[0])
        return iter(iter_list)
        
        
    
    def __eq__(self, right):
        
        if type(right) == DictList:
            for dic in right.dl:
                for key in dic:
                    if self[key] != right[key]:
                        return False
            return True
                 
        if type(right) == dict:
            if len(right) < len(self):
                return False
            for key in right:
                if self[key] != right[key]:
                    return False
            return True
        else:
            raise TypeError("not type dict or DictList")
        
    
    
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
