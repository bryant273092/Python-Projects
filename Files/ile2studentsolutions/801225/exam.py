from goody import type_as_str  # Useful in some exceptions

class DictList:
            

    def __init__(self, *kargs):
        assert len(kargs) > 0, 'DictList.__init__: "{}" is not a dictionary'.format(kargs)
        self.dl = []
        for i in kargs:
            assert type(i) is dict, 'DictList.__init__: "{}" is not a dictionary'.format(i)
            self.dl.append(i)


    def __len__(self):
        distinct = []
        for i in self.dl:
            for k, v in i.items():
                distinct.append(k)
        distinct = list(set(distinct))
        return len(distinct)
        
    def __repr__(self):
        contents = ''
        for i in self.dl:
            contents += '{}, '.format(i)
        contents = contents.strip(' ').strip(',')
        return "DictList(" + contents + ")"
            
    def __contains__(self, value):
        for i in self.dl:
            for k, v in i.items():
                if k == value:
                    return True
        return False
            
    def __getitem__(self, key):
        stuff = []
        keys = []
        for i in self.dl:
            for k, v in i.items():
                if k == key:
                    stuff.append(v)
                    keys.append(k)
        if key not in keys:
            raise KeyError("'{}' does not reside within any of the dictionaries".format(key))

        if len(stuff) is 0:
            raise KeyError("'{}' does not reside within any of the dictionaries".format(key))
        return max(stuff)
    
    def __setitem__(self, key, value):
#         print(key, value)
        cond = []
        for i in self.dl:
            if key not in i:
                cond.append(True)
            else:
                cond.append(False)
        if False not in cond:
            self.dl.append({key:value})
        
        stuff = []
        for i in self.dl:
            for k, v in i.items():
                if k == key:
                    stuff.append(v)
        for i in self.dl:
            for k, v in i.items():
                if v == max(stuff):
                    i[k] = value
            
    def __call__(self, key):
        result = []
        for num, i in enumerate(self.dl):
            if key in i:
                result.append((num, i[key]))
        return result
    
    def __iter__(self):
        keys = []
        values = []
        for i in reversed(self.dl):
            for k, v in i.items():
                if k not in keys:
                    keys.append(k)
                    values.append(v)
                    
        for i in zip(keys, values):
            yield i
        
    def __eq__(self, right):
        if type(right) is DictList:
            keys = set()
            for i in self.dl:
                for k, v in i.items():
                    keys.add(k)
            truth_values = []
            for i in list(keys):
                if self[i] == right[i]:
                    truth_values.append(True)
                else:
                    truth_values.append(False)
            if False in truth_values:
                return False
            else:
                return True
        
        if type(right) is dict:
            keys = []
            for i in self.dl:
                for k, v in i.items():
                    keys.append(k)
            for i in keys:
                if i not in right:
                    return False
            for i in keys:
                if self[i] != right[i]:
                    return False
            return True
        else:
            raise TypeError('"{}" is neither DictList or dict'.format(right))
        
    def __add__(self, right):
        pass
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
