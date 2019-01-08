from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *arg):
        assert arg != (), f'DictList.__init__: {arg} should not be empty'
        for i in arg:
            assert type(i) is dict, f'DictList.__init__: {i} is not a dictionary.'
        self.dl = list()
        for i in arg:
            self.dl.append(i)
    
    def __len__(self):
        temp = set()
        for i in range(len(self.dl)):
            for j in self.dl[i].keys():
                temp.add(j)
        return len(temp)
    
    def __repr__(self):
        templ = list()
        for i in range(len(self.dl)):
            templ.append(repr(self.dl[i]))
        temps = ', '.join((i for i in templ))
        return f'DictList({temps})'
    
    def __contains__(self, arg):
        for i in range(len(self.dl)):
            if arg in self.dl[i].keys():
                return True
        return False
    
    def __getitem__(self, arg):
        if arg not in self: raise KeyError(f'DictList.__getitem__: {arg} not in the list')
        index = list()
        for i in range(len(self.dl)):
            if arg in self.dl[i].keys():
                index.append(i)
        return self.dl[max(index)][arg]
    
    def __setitem__(self, key, value):
        if key not in self:
            self.dl.append(dict([(key, value)]))
        else:
            index = list()
            for i in range(len(self.dl)):
                if key in self.dl[i].keys():
                    index.append(i)
            self.dl[max(index)][key] = value
            
    def __call__(self, arg):
        if arg not in self:
            return []
        result = list()
        for i in range(len(self.dl)):
            if arg in self.dl[i].keys():
                result.append((i, self.dl[i][arg]))
        return result
    
    def __iter__(self):
        record = set()
        for i in range(-1, -len(self.dl)-1, -1):
            for j in sorted(self.dl[i].keys()):
                if j not in record:
                    yield (j, self.dl[i][j])
                    record.add(j)
    
    def __eq__(self, other):
        if type(other) not in (DictList, dict):
            raise TypeError(f'DictList.__eq__: {other} is in wrong type.\n  It was {type_as_str(other)}, should be dict or DictList.')
        
        def keyset(arg):
            temp = set()
            for i in range(len(arg.dl)):
                for j in arg.dl[i].keys():
                    temp.add(j)
            return temp
        # create a set including all the keys
        temp1 = keyset(self)
        if type(other) is DictList:
            temp2 = keyset(other)
        else:
            temp2 = set(other.keys())
        # compare
        if temp1 != temp2: return False
        for i in temp1:
            if self[i] != other[i]: return False
        else: return True
        
    def __add__(self, other):
        if type(other) not in (DictList, dict):
            raise TypeError(f'DictList.__eq__: {other} is in wrong type.\n  It was {type_as_str(other)}, should be dict or DictList.')
        
        def keyset(arg):
            temp = set()
            for i in range(len(arg.dl)):
                for j in arg.dl[i].keys():
                    temp.add(j)
            return temp
        
        temp1 = keyset(self)
        list1 = list()
        for i in temp1:
            list1.append((i, self[i]))
        
        list2 = list()  
        if type(other) is DictList:
            temp2 = keyset(other)
        else:
            temp2 = set(other.keys())
        for i in temp2:
            list2.append((i, other[i]))
        
        return DictList(dict(list1), dict(list2))
    
    def __radd__(self, other):
        if type(other) is not dict:
            raise TypeError(f'DictList.__eq__: {other} is in wrong type.\n  It was {type_as_str(other)}, should be dict.')
        
        temp1 = set()
        for i in range(len(self.dl)):
            for j in self.dl[i].keys():
                temp1.add(j)
        list1 = list()
        for i in temp1:
            list1.append((i, self[i]))
        
        list2 = list()  
        temp2 = set(other.keys())
        for i in temp2:
            list2.append((i, other[i]))
        
        return DictList(dict(list2), dict(list1))
            
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
