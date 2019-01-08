
class DictList:
    def __init__(self, *args: dict):
        dict_list = []
        if len(args) == 0:
            raise AssertionError("Must include one argument")
        for arg in args:
            if type(arg) != dict:
                raise AssertionError(str(arg) + " must be a dictionary")
            else:
                dict_list.append(arg)
        self.dl = dict_list
    def __len__(self):
        key_list = set()
        for dic in self.dl:
            for key in dic:
                key_list.add(key)
        return len(key_list)
    def __repr__(self):
        result = ""
        for dic in self.dl:
            result += str(dic) + ", "
        result = "DictList(" + result + ")"
        return result
    def __contains__(self, value):
        for dic in self.dl:
            if value in dic:
                return True
        return False
    def __getitem__(self, key):
        in_dic = False
        for dic in self.dl:
            if key in dic:
                value = dic[key]
                in_dic = True
        if in_dic == False:
            raise KeyError(str(key) + " appears in no dictionaries")
        return value
    def __setitem__(self, key, value):
        highest_index = -1
        for num in range(len(self.dl)):
            if key in self.dl[num]:
                highest_index = num
        if highest_index == -1:
            self.dl.append({key: value})
        else:
            self.dl[highest_index][key] = value
    def __call__(self, key):
        tuple_list = []
        for num in range(len(self.dl)):
            if key in self.dl[num]:
                tuple_list.append((num, self.dl[num][key]))
        return tuple_list
    def __iter__(self):
        check_str = ""
        reversed_list = self.dl
        reversed_list.reverse()
        for dic in reversed_list:
            for key in dic:
                if key not in check_str:
                    yield (key, dic[key])
                check_str += str(key)
    def __eq__(self, value):
        key_list = []
        for dic in self.dl:
            for key in dic:
                key_list.append(key)
        if type(value) not in (DictList, dict):
            raise TypeError("Inappropriate type")
        elif type(value) == DictList:
            for num in range(len(value.dl)):
                for key in value.dl[num]:
                    if key not in key_list:
                        return False
                    if self.__getitem__(key) != value.__getitem__(key):
                        return False
            return True
        elif type(value) == dict:
            for key in key_list:
                if key not in value:
                    return False
            for key in value:
                if key not in key_list:
                    return False
                if value[key] != self.__getitem__(key):
                    return False
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
