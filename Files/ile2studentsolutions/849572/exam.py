from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self, *dicts):
        self.dl = []
        if len(dicts) != 0:
            for arg_dict in dicts:
                if isinstance(arg_dict, dict):
                    self.dl.append(arg_dict)
                else:
                    raise AssertionError("DictList.__init__: {} is not a dictionary".format(arg_dict))
        else:
            raise AssertionError("DictList.__init__: {} is not a dictionary")

    def __len__(self):
        unique_keys = set()
        for d in self.dl:
            for key in d:
                unique_keys.add(key)
        return len(unique_keys)
    
    def __repr__(self):
        return "DictList({})".format(", ".join([str(d) for d in self.dl]))
    
    def __contains__(self, item):
        for d in self.dl:
            if item in d:
                return True
        return False
    
    def __getitem__(self, item):
        latest = None
        for d in self.dl:
            for key, val in d.items():
                if key == item:
                    latest = val
        if latest is not None:
            return latest
        else:
            raise KeyError
    
    def __setitem__(self, item, val):
        latest = None
        for i in range(len(self.dl)):
            if item in self.dl[i]:
                latest = i
        if latest is not None:
            self.dl[latest][item] = val
        else:
            self.dl.append({item: val})
    
    def __call__(self, item):
        hist = []
        for i in range(len(self.dl)):
            if item in self.dl[i]:
                hist.append((i, self.dl[i][item]))
        return hist
    
    def __iter__(self):
        called = {}
        prior = set()
        for i in range(len(self.dl)):
            index = -(i + 1)
            for key, val in self.dl[index].items():
                if key not in prior:
                    called[key] = (val, i)
                prior.add(key)
        for pair in sorted(called, key=lambda x: called[x][1]):
            yield (pair, called[pair][0])
            
    
    def __eq__(self, item):
        if isinstance(item, dict):
            if len(item) != len(self):
                return False
            for key in item:
                if key not in self or self[key] != item[key]:
                    return False
        elif isinstance(item, DictList):
            if len(item) != len(self):
                return False
            for key in item:
                if key[0] not in self or self[key[0]] != item[key[0]]:
                    return False
        else:
            raise TypeError("DictList.__eq__: {} is not dictionary or DictList".format(item))
        return True
    
    def __add__(self, item):
        if isinstance(item, DictList):
            self_pairs = {}
            for pair in self:
                self_pairs[pair[0]] = pair[1]
            item_pairs = {}
            for pair in item:
                item_pairs[pair[0]] = pair[1]
            new = DictList(self_pairs, item_pairs)
        elif isinstance(item, dict):
            self_pairs = {}
            for pair in self:
                self_pairs[pair[0]] = pair[1]
            new = DictList(self_pairs, item)
        else:
            raise TypeError("DictList.__add__: Invalid item type - must be dictionary or DictList")
        return new
        



            
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
    
