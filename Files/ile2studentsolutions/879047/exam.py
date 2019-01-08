from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        assert args !=()
        for arg in args:
            assert type(arg) is dict
            self.dl.append(arg)
    def __len__(self):
        my_set = set()
        for my_dict in self.dl:
            for key in my_dict:
                my_set.add(key)
        return len(my_set)        
    def __repr__(self):
        return "DictList(" + ','.join(str(dicts) for dicts in self.dl)+")"    
    def __contains__(self, element):
        for my_dict in self.dl:
            for key in my_dict:
                if key == element:
                    return True
        return False
    def __getitem__(self, item):
        seen = False
        high = 0
        for my_dict in self.dl:
            if item in my_dict:
                seen = True
            for key, value in my_dict.items():
                #if key == item and value > high:
                if key == item:
                    if type(value) is int and value > high:
                        high = value
                    
        if seen == False:
            raise KeyError
        return high
    def __setitem__(self, item, value):
        done = False
        i = item
        for my_dict in reversed(self.dl):
        #for my_dict in sorted(self.dl, reverse = True):
            for key, values in my_dict.items():
                if key == item and done == False:
                    my_dict[key] = value
                    done = True
        if done == False:
            self.dl.append({item:value})           
    def __call__(self, item): 
        my_list = []
        i = 0
        for my_dict in self.dl:
            for key, value in my_dict.items():
                if key == item:
                    my_list.append((i,value))
            i+=1
        return my_list
    def __iter__(self):
        my_set = set()
        for my_dict in reversed(self.dl):
            for key, value in my_dict.items():
                if key not in my_set:
                    yield(key,value)
                    my_set.add(key)
    def __eq__(self, right):
        if type(right) not in (dict, DictList):
            raise TypeError
        elif type(right) is DictList:
            for my_dict in self.dl:
                for key in my_dict:
                    #print(right.__call__(key))
                    try:
                        if right.__call__(key) == []:
                            return False
                        if self.__getitem__(key) != right.__getitem__(key):
                            return False
                    except KeyError:
                        return False
        elif type(right) is dict:
            for my_dict in self.dl:
                for key, value in my_dict.items():
                    try:
                        if right[key] != self.__getitem__(key):
                            return False
                    except KeyError:
                        return False
        return True
    def __add__(self,right):
        if type(right) not in (dict, DictList):
            raise TypeError
        elif type(right) is DictList:
            dict1 = {}
            dict2 = {}
            for my_dict in self.dl:
                for key in my_dict:
                    dict1[key] = self.__getitem__(key)
            for my_dicts in right.dl:
                for keys, v in my_dicts.items():
                    if type(v) is int:
                        dict2[keys] = right.__getitem__(keys)
                    else: 
                        dict2[keys] = v
            return DictList(dict1, dict2)
        elif type(right) is dict:
            print(*(my_dict for my_dict in self.dl))
            return DictList(right,*(my_dict for my_dict in self.dl)) 
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
