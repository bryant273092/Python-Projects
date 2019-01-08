from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        if len(args) == 0:
            raise AssertionError('No dictionaries in the initialization')
        for item in args:
            if type(item) == dict:
                self.dl.append(item)
            else:
                raise AssertionError("'{itemm}' is not a dictionary".format(itemm = str(item)))
            
    def __len__(self):
        count = 0 
        checked_list =[]
        for dictt in self.dl:
            for key in dictt.keys():
                if key not in checked_list:
                    count += 1
                    checked_list.append(key)
        return count
    
    def __repr__(self):
        return 'DictList({dictt})'.format(dictt = ','.join(str(x) for x in self.dl))
    
    def __contains__(self, item):
        for dictt in self.dl:
            for key in dictt.keys():
                if item == key:
                    return True
        return False
    
    def __getitem__(self, item):
        for itemm in self.dl[::-1]:
            if item in itemm.keys():
                return itemm[item]
        raise KeyError("'{it}' appears in no dictionary".format(it = str(item)))
    
    def __setitem__(self, item, value):
        count = 0
        for itemm in self.dl[::-1]:
            if item in itemm.keys():
                itemm[item] = value
                break
            else:
                count += 1
        if count == len(self.dl):
            self.dl.append({item:value})
            
    def __call__(self, key):
        answer_list = []
        for index, dictt in enumerate(self.dl):
            for inner_key in dictt.keys():
                if key == inner_key:
                    answer_list.append((index, dictt[key]))
        return sorted(answer_list)
    
    def __iter__(self):
        checked_keys = []
        for dictt in self.dl[::-1]:
            for key in sorted(dictt.keys()):
                if key not in checked_keys:
                    checked_keys.append(key)
                    yield (key, dictt[key])
                    
    def __eq__(self, right):
        if type(right) == dict:
            checked_keys = []
            for dictt in self.dl[::-1]:
                for key in dictt.keys():
                    if key not in checked_keys:
                        checked_keys.append(key)
                        if key in right.keys():
                            if dictt[key] != right[key]:
                                return False
                        else:
                            return False
            return len(checked_keys) == len(right.keys())
        elif type(right) == DictList:
            dict_to_compare = dict()
            for dictt in self.dl[::-1]:
                for key in dictt.keys():
                    if key not in dict_to_compare.keys():
                        dict_to_compare[key] = dictt[key]
            second_dict_to_compare = dict()
            for second_dict in right.dl[::-1]:
                for second_key in second_dict.keys():
                    if second_key not in second_dict_to_compare.keys():
                        second_dict_to_compare[second_key] = second_dict[second_key]
            return second_dict_to_compare == dict_to_compare
        else:
            raise TypeError("'{item}' is not a type Dictlist or type dict".format(item = str(right)))
        
    def __add__(self, right):
        if type(right) == DictList:
            dict_to_add = dict()
            for dictt in self.dl[::-1]:
                for key in dictt.keys():
                    if key not in dict_to_add.keys():
                        dict_to_add[key] = dictt[key]
            second_dict_to_add = dict()
            for second_dict in right.dl[::-1]:
                for second_key in second_dict.keys():
                    if second_key not in second_dict_to_add.keys():
                        second_dict_to_add[second_key] = second_dict[second_key]
            return DictList(dict_to_add, second_dict_to_add)
        elif type(right) == dict:
            return DictList((x for x in self.dl), right)
        else:
            raise TypeError("'{item}' is not a type DictList or type Dict".format(item = str(right)))
        
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
