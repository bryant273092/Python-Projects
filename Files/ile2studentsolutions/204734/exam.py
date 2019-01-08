from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *dicts):
        self.dl = []
        if len(dicts) == 0:
            raise AssertionError ("Must have a dict")
        for single_dict in dicts:
            assert type(single_dict) == dict, "Must be of type dict"
            self.dl.append(single_dict)
            
    def __len__(self):
        distinct = 0
        key_list = []
        for diff_dicts in self.dl:
            for single_key,single_value in diff_dicts.items():
                if single_key not in key_list:
                    key_list.append(single_key)
                    distinct += 1
        return distinct

    def __repr__(self):
        dict_repr = "DictList("
        for single_dict in self.dl:
            dict_repr += str(single_dict) +","
        dict_repr.rstrip(",")
        dict_repr += ")"
        return dict_repr
            
    def __contains__(self,check_key):
        for single_dict in self.dl:
            if check_key in single_dict.keys():
                return True
        return False
    
    def __getitem__(self,check_key):
        for single_dict in self.dl[-1::-1]:
            if check_key in single_dict.keys():
                return single_dict[check_key]
        raise KeyError ("The argument must be a key in dictlist")
    
    def __setitem__(self,check_key,newvalue):
        for single_dict in self.dl[-1::-1]:
            if check_key in single_dict.keys():
                single_dict[check_key] = newvalue
                break
            elif single_dict == self.dl[0] and check_key not in single_dict.keys():
                self.dl.append({check_key:newvalue})
            else:
                continue
                
    def __call__(self,check_key):
        tuple_list = []
        index = 0
        for single_dict in self.dl:
            if check_key in single_dict.keys():
                value = single_dict[check_key]
                key_value_tuple = (index, value)
                tuple_list.append(key_value_tuple)
            index += 1
        return sorted(tuple_list)
    
    def __iter__(self):
        def itergen(dict_list):
            key_list = []
            for single_dict in dict_list.dl[-1::-1]:
                sorted_dict = sorted(single_dict)
                for key,value in sorted_dict.items():
                    if key not in key_list:
                        key_list.append(key)
                        yield (key,value)
        return itergen(self.dl)
#         iterable_dl = iter(self.dl)
#         try:
#             while True:
 
#         except:
#             StopIteration
                
    def __eq__(self,right):
        if type(right) != dict and type(right) != DictList:
            raise TypeError ("Must compare the dictlist to a dict or another dictlist")
        key_list = []
        key_list2 = []
        for single_dict in self.dl: #put all keys of left operand into a list
            for keys in single_dict.keys():
                key_list.append(keys)
        if type(right) == DictList:
            for single_dict in right.dl: #put all keys of right operand into a list
                for keys in single_dict.keys():
                    key_list2.append(keys)
        elif type(right) == dict:
            for keys in right.keys():
                key_list2.append(keys)
   
        for keys in key_list:
            if keys in key_list2: #checks that the key is in key_list2
                if self.__getitem__(keys) != right.__getitem__(keys):
                    return False
            else:
                return False
        return True
    
    def __add__(self,right):
        if type(right) != DictList and type(right) != dict:
            return NotImplemented
        if type(right) == DictList:
            dictlist0 = {}
            dictlist1 = {}
            for single_dict in self.dl:
                for key,value in single_dict.items():
                    if key not in dictlist0.keys():
                        dictlist0[key] = self.__getitem__(key)
            for single_dict in right.dl:
                for key,value in single_dict.items():
                    if key not in dictlist1.keys():
                        dictlist1[key] = right.__getitem__(key)   
            return DictList(dictlist0,dictlist1)
        elif type(right) == dict:
            return DictList(*self.dl,right)
        
    def __radd__(self,left):
        if type(left) != dict:
            raise TypeError ("Must add a dict or dictlist to a dictlist")
        else:
            return DictList(left,*self.dl)
            
                
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test


    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
    driver.default_show_exception=True
    driver.default_show_exception_message=True
    driver.default_show_traceback=True
    driver.driver()
