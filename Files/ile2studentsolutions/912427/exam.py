from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        if len(args) != 0:
            for a_dict in args:
                assert type(a_dict) == dict, str(a_dict) + "is not a dictionary"
                self.dl.append(a_dict)
        else:
            raise AssertionError("There are no parameters specified")
        
    def __len__(self):
        test_set = set()
        for a_dict in self.dl:
            for key, value in a_dict.items():
                test_set.add(key)
        return len(test_set)
    
    def __repr__(self):
        new_string = ""
        new_string += "DictList("
        for a_dict in self.dl:
            new_string += str(a_dict) + ", "
        new_string = new_string.rstrip()
        new_string += ")"
        return new_string
    
    def __contains__(self, item):
        for a_dict in self.dl:
            if item in a_dict:
                return True
        return False
    
    def __getitem__(self, item):
        return_value = ""
        for a_dict in self.dl:
            if item in a_dict.keys():
                return_value = a_dict[item]
        if return_value != "":
            return return_value
        else:
            raise KeyError(str(item) + " appears in no dictionaries")
    
    def __setitem__(self, item, value):
        highest_index = ""
        for a_dict in self.dl:
            if item in a_dict:
                highest_index = self.dl.index(a_dict)
        if highest_index == "":
            new_dict = {}
            new_dict[item] = value
            self.dl.append(new_dict)
        else:
            self.dl[highest_index][item] = value
            
    def __call__(self, item):
        return_list = []
        for a_dict in self.dl:
            if item in a_dict:
                return_list.append((self.dl.index(a_dict), a_dict[item]))
        return return_list
            
    def __iter__(self):
        new_set = set()
        for a_dict in self.dl:
            for key in a_dict:
                new_set.add(key)
        final_return = []
        for a_dict in self.dl.__reversed__():
            is_true = False
            for item in new_set:
                if item in a_dict:
                    is_true = True
            if is_true == True:
                sorted_dict = sorted(a_dict)
                for item in sorted_dict:
                    if item in new_set.copy():
                        new_set.remove(item)
                        final_return.append((item, a_dict[item]))
        for x in final_return:
            yield x              
    
    def __eq__(self, dict_object):
        if type(dict_object) == dict:
            new_list = []
            for key, value in dict_object.items():
                new_list.append((key,value))
            for a_dict in self.dl:
                for item in new_list.copy():
                    if item[0] in a_dict and a_dict[item[0]] == item[1]:
                        new_list.remove(item)
            if new_list == []:
                return True
            else:
                return False
        elif type(dict_object) == DictList:
            new_list = []
            for a_dict in dict_object.dl:
                for key, value in a_dict.items():
                    new_list.append((key,value))
            for a_dict in self.dl:
                for item in new_list.copy():
                    if item[0] in a_dict and a_dict[item[0]] == item[1]:
                        new_list.remove(item)
            if new_list == []:
                return True
            else:
                return False
        else:
            raise TypeError(str(dict_object) + " is not a DictList or dict")
        




            
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
