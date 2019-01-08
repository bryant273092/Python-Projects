from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *dl):
        if len(dl) == 0:
            assert type(dl) is dict, 'DictList.__init__: ' + repr(dl) + ' is not a dictionary.'
        elif len(dl) == 1:
            assert type(dl[0]) is dict, 'DictList.__init__: ' + repr(dl[0]) + ' is not a dictionary.'
            self.dl = [dl[0]]
        else:
            self.dl = []
            for d in dl:
                assert type(d) is dict, 'DictList.__init__: ' + repr(d) + ' is not a dictionary.'
                self.dl.append(d)
    
    def __len__(self):
        unique = []
        for d in self.dl:
            for k in d.keys():
                if k not in unique:
                    unique.append(k)
        return len(unique)
    
    def __repr__(self):
        return 'DictList(' + ','.join([repr(d) for d in self.dl]) + ')'
    
    def __contains__(self, index):
        for d in self.dl:
            if index in d.keys():
                return True
        return False
    
    def __getitem__(self, index):
        for i in range(len(self.dl)-1, -1, -1):
            d = self.dl[i]
            if index in d.keys():
                return d[index]
        raise KeyError(repr(index)+' appears in no dictionaries.')
    
    def __setitem__(self, index, value):
        in_dict = False
        for i in range(len(self.dl)-1, -1, -1):
            if index in self.dl[i].keys():
                self.dl[i][index] = value
                in_dict = True
                break
        if not in_dict:
            self.dl.append({index:value})
           
    def __call__(self, index):
        result = []
        for i in range(len(self.dl)-1, -1, -1):
            if index in self.dl[i].keys():
                result.append((i, self.dl[i][index]))
        return sorted(result)
    
    def __iter__(self):
        dliterable = []
        added_indecies = []
        for i in range(len(self.dl)-1, -1, -1):
            elements = []
            for index,value in self.dl[i].items():
                elements.append((index, value))
            for element in sorted(elements):
                if element[0] not in added_indecies:
                    dliterable.append(element)
                    added_indecies.append(element[0])
        return iter(dliterable)
    
    def __eq__(self, right):
        left_keys = set()
        for d in self.dl:
            for k in d.keys():
                left_keys.add(k)
        
        if type(right) is DictList:
            right_keys = set()
            for d in right.dl:
                for k in d.keys():
                    right_keys.add(k)

            if left_keys != right_keys:
                return False
            
            for k in left_keys:
                if self[k] != right[k]:
                    return False
            return True
        
        elif type(right) is dict:
            right_keys = set(right.keys())
            
            if left_keys != right_keys:
                return False
            for k in left_keys:
                if self[k] != right[k]:
                    return False
            return True

        else:
            raise TypeError('DictList.__eq__: ' + repr(right) + ' is not a DictList or dictionary.')
        
    def __add__(self, right):
        if type(right) is DictList:
            a = list(self.dl)
            b = list(right.dl)
            a.extend(b)
            return DictList(*a)
        elif type(right) is dict:
            a = list(self.dl)
            b = a.append(dict(right))
            return DictList(*a)
        
    
    

            
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
