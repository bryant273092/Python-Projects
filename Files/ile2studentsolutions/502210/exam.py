from goody import type_as_str, irange  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        assert len(args) != 0, "No dictionaries found"
        self.dl = []
        for i in args:
            assert type(i) == dict, "{} is not a dictionary".format(i)
            self.dl.append(i)
            
    def __len__(self):
        unique_keys = []
        for i in self.dl:
            for k in i.keys():
                if k not in unique_keys:
                    unique_keys.append(k)
        return len(unique_keys)
    
    def __repr__(self):
        return 'DictList{}'.format(tuple(self.dl))
    
    def __contains__(self, item):
        for i in self.dl:
            if item in i.keys():
                return True
        return False
    
    def __getitem__(self, item):
        value = None
        for i in self.dl:
            if item in i.keys():
                value = i[item]
        if value == None:
            raise KeyError("{} appears in no dictionaries".format(item))
        else:
            return value
        
    def __setitem__(self, item, value):
        to_change = None
        for i in range(len(self.dl)):
            if item in self.dl[i].keys():
                to_change = i
        if to_change == None:
            self.dl.append({item: value})
        else:
            self.dl[to_change][item] = value
            
    def __call__(self, key):
        call_list = []
        for i in range(len(self.dl)):
            if key in self.dl[i].keys():
                call_list.append((i, self.dl[i][key]))
        return call_list
    
    def __iter__(self):
        def dictlist_iter(dl):
            itered_keys = []
            for i in irange(len(dl) - 1, 0, -1):
                for k in sorted(list(dl[i].keys())):
                    if k not in itered_keys:
                        yield (k, dl[i][k])
                        itered_keys.append(k)
        return dictlist_iter(self.dl)
    
    def __eq__(self, other):
        unique_keys = []
        for i in self.dl:
            for k in i.keys():
                if k not in unique_keys:
                    unique_keys.append(k)
        if type(other) == DictList:
            for i in unique_keys:
                try:
                    if self[i] != other[i]:
                        return False
                except KeyError:
                    return False
            return True
        elif type(other) == dict:
            for i in unique_keys:
                if i not in other.keys():
                    return False
            for k in other.keys():
                if k not in unique_keys:
                    return False
                elif self[k] != other[k]:
                    return False
            return True
        else:
            raise TypeError("using == with DictList can only compare DictList with DictList or list, not {}".format(type_as_str(other)))
        
    def __add__(self, other):
        if type(other) == DictList:
            dict_one = {}
            dict_two = {}
            unique_keys = []
            for i in self.dl:
                for k in i.keys():
                    if k not in unique_keys:
                        unique_keys.append(k)
            for i in unique_keys:
                dict_one.update({i: self[i]})
            unique_keys.clear()
            for i in other.dl:
                for k in i.keys():
                    if k not in unique_keys:
                        unique_keys.append(k)
            for i in unique_keys:
                dict_two.update({i: other[i]})
            return DictList(dict_one, dict_two)
        elif type(other) == dict:
            new_dictlist = [i for i in self.dl]
            new_dictlist.append(dict(other))
            return DictList(*new_dictlist)
        else:
            raise TypeError("using + with DictList can only compare DictList with DictList or list, not {}".format(type_as_str(other)))
    
    def __radd__(self, other):
        if type(other) == DictList:
            dict_one = {}
            dict_two = {}
            unique_keys = []
            for i in self.dl:
                for k in i.keys():
                    if k not in unique_keys:
                        unique_keys.append(k)
            for i in unique_keys:
                dict_one.update({i: self[i]})
            unique_keys.clear()
            for i in other.dl:
                for k in i.keys():
                    if k not in unique_keys:
                        unique_keys.append(k)
            for i in unique_keys:
                dict_two.update({i: other[i]})
            return DictList(dict_one, dict_two)
        elif type(other) == dict:
            new_dictlist = [dict(other)]
            for i in self.dl:
                new_dictlist.append(i)
            return DictList(*new_dictlist)
        else:
            raise TypeError("using + with DictList can only compare DictList with DictList or list, not {}".format(type_as_str(other)))




            
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
