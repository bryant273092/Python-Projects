from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        if args == (): raise AssertionError
        for argument in args:
            if type(argument) is not dict:
                raise AssertionError(type_as_str(DictList) +'.__init__', argument, 'is not a dictionary')
            self.dl.append(argument)
    
    def __len__(self):
        dict_set = set()
        for d in self.dl:
            for k in d:
                dict_set.add(k)
        return len(dict_set)
    
    def __repr__(self):
        result = 'DictList('
        elements_list = [str(d) for d in self.dl]
        return result + ','.join(elements_list) + ')'
                
    
    def __contains__(self, item):
        for d in self.dl:
            if item in d: return True
        return False
    
    def __getitem__(self, item):
        highest_value = 0
        for d in self.dl:
            if d == self.dl[-1] and highest_value == 0 and item not in d: raise KeyError
            if item in d and d[item] > highest_value:
                highest_value = d[item]
        return highest_value
    
    def __setitem__(self, key, value):
        highest_value = 0 
        highest_index = None
        
        for d in self.dl:
            if key not in d:
                pass
            if key in d and d[key] > highest_value:
                highest_value = d[key]
                highest_index = self.dl.index(d)
                
        if highest_index == None:
            self.dl.append({key: value})
        else:
            self.dl[highest_index][key] = value 
            
    def __call__(self, value):
        values = []
        for d in self.dl:
            if value in d:
                values.append((self.dl.index(d), d[value]))
        return values
    
    def __iter__(self):
        returned_values = set()
        for d in self.dl[::-1]:
            d_keys = sorted(d)
            for k in d_keys:
                if k in returned_values:
                    pass
                else:
                    returned_values.add(k)
                    yield (k, d[k])
    
    def __eq__(self, right):
        if type(right) is not DictList and type(right) is not dict: raise TypeError
        
        if type(right) is dict:
            for d in self.dl:
                for k in d:
                    if k not in right.keys() and d == self.dl[-1]: return False
                    if d[k] != right[k] and d == self.dl[-1]: return False
            return True
        
        if type(right) is DictList:
            for d in self.dl:
                for d_2 in right.dl:
                    for k in d:
                        if d_2 == right.dl[-1] and k not in d_2: return False
            
            for d in self.dl:
                for k in self.dl:
                    for d_2 in right.dl:
                        if k in d_2 and d[k] != d_2[k]: return False
            
            return True
#             self_values = [], right_values = []
#             for d in self.dl:
#                 for k in d:
#                     if (k ,self.__getitem__(k)) not in self_values: 
#                         self_values.append((k, self.__getitem__(k)))
#             for d_2 in right.dl:
#                 for k_2 in d_2:
#                     if (k_2 ,right.__getitem__(k_2)) not in right_values: 
#                         right_values.append((k_2, right.__getitem__(k_2)))
#             return self_values == right_values
        




            
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
