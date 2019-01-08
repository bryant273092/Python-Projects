from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        assert len(args) > 0, "Must not be zero lenght args"
        for argdict in args:
            assert type(argdict) == dict, "Invalid argument must all be dict {}".format(args)
            self.dl.append(argdict)

    def __len__(self):
        key_set = set()
        for dict in self.dl:
            for key in dict:
                key_set.add(key)
        return len(key_set)

    def __repr__(self):
        return "DictList("+ ",".join(str(x) for x in self.dl) +")"

    def __contains__(self, value):
        key_set = set()
        for dict in self.dl:
            for key in dict:
                key_set.add(key)
        return value in key_set

    def __getitem__(self, item):
        if not self.__contains__(item):
            raise KeyError("{} does not exist in any dict".format(item))
        ditem = None
        for idict in self.dl:
            for key in idict:
                if key == item:
                    ditem = idict[key]
        return ditem

    def __setitem__(self, key, value):
        if self.__contains__(key):
            highest_dict = 0
            for i in range(len(self.dl)):
                if key in self.dl[i].keys():
                    highest_dict = i
            self.dl[highest_dict][key] = value
        else:
            self.dl.append({key: value})

    def __iter__(self):
        used_kets = set()
        kv_set = set()
        kv_list = []
        for idict in reversed(self.dl):
            for item in idict.items():
                if item[0] in used_kets:
                    continue
                used_kets.add(item[0])
                kv_set.add(item)
            kv_list.append(sorted(list(kv_set)))
            kv_set = set()
        for dict_itms in kv_list:
            for items in dict_itms:
                yield items

    def __eq__(self, other):
        if type(other) in (dict, DictList):
            self_key_set = set()
            for idict in self.dl:
                for key in idict:
                    self_key_set.add(key)
            if type(other) == DictList:
                other_key_set = set()
                for idict in other.dl:
                    for key in idict:
                        self_key_set.add(key)
                if self_key_set == other_key_set:
                    for value in list(self_key_set):
                        if self[value] != other[value]:
                            return False
                    return True
                else:
                    return False
            elif type(other) == dict:
                if self_key_set == other.keys():
                    for key in other.keys():
                        if self[key] != other[key]:
                            return False
                    return True
                else:
                    return False
            
        else:
            raise TypeError("operand must be dict or DictList")

    def __call__(self, key):
        index_list = []
        if self.__contains__(key):
            for i in range(len(self.dl)):
                if key in self.dl[i]:
                    index_list.append((i, self.dl[i][key]))
        return index_list

if __name__ == '__main__':
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
