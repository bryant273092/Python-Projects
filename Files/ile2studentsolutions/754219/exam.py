from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*dicts):
        self.dl = []
        if dicts == ():
            raise AssertionError
        for x in dicts:
            if type(x) != dict:
                raise AssertionError('DictList.__init__: ' + str(x) + 'is not a dictionary.')
            self.dl.append(x)
    
    def __len__(self):
        distinct = []
        for x in self.dl:
            for y in x.keys():
                if y not in distinct:
                    distinct.append(y)
        return len(distinct)
    
    def __repr__(self):
        beginning = 'DictList('
        for x in self.dl:
            beginning += str(x) + ','
        beginning = beginning.rstrip(',')
        beginning += ')'
        return beginning
    
    def __contains__(self, key):
        for x in self.dl:
            if key in x.keys():
                return True
        return False
    
    def __getitem__(self,key):
        in_dict = False
        for x in self.dl:
            if key in x.keys():
                in_dict = True
                result = x[key]
        if in_dict == False:
            raise KeyError('DictList.__getitem__: ' + str(key) + 'is not a valid key in any dictionary.')
        return result
    
    def __setitem__(self,key,value):
        last_index = 0
        save_index = -1
        for x in self.dl:
            if key in x.keys():
                save_index = last_index
            last_index += 1
        if save_index == -1:
            self.dl.append({key:value})
        else:
            self.dl[save_index][key] = value
    
    def __call__(self, key):
        result = []
        index = 0
        for x in self.dl:
            if key in x.keys():
                result.append((index, x[key]))
            index += 1
        return result
    
    def __iter__(self):
        result = []
        new_result = []
        keys = []
        for x in self.dl:
            for y in x.keys():
                if y not in keys:
                    keys.append(y)
        for x in keys:
            result.append((x, self.__getitem__(x)))
        length = len(self.dl) - 1
#         for x in range(len(self.dl)):
#             for y in self.dl[length].keys():
#                 counter = 0
#                 for z in result:
#                     if y == z[0]:
#                         new_result.append(z[counter])
#                     counter +=1
#             length += -1
        return iter(result)
    
    def __eq__(self,right):
        if type(right) != DictList and type(right) != dict:
            raise TypeError("DictList.__eq__: " + str(type(right)) + 'is not of type dict or DictList.')
        if type(right) == dict:
            right = DictList(right)
        keys1 = []
        keys2 = []
        for x in self.dl:
            for y in x.keys():
                if y not in keys1:
                    keys1.append(y)
        for x in right.dl:
            for y in x.keys():
                if y not in keys2:
                    keys2.append(y)
        if sorted(keys1) != sorted(keys2):
            return False 
        for x in keys1:
            if self.__getitem__(x) != right.__getitem__(x):
                return False
        return True
    
    def __add__(self, right):
        if type(right) != dict and type(right) != DictList:
            raise TypeError('DictList.__add__: ' + str(type(right)) + 'is not of type dict or DictList.')
        dict1 = {}
        dict2 = {}
        if type(right) == DictList:
            for x in self.dl:
                for y in x.keys():
                    dict1[y] = self.__getitem__(y)
            for x in right.dl:
                for y in x.keys():
                    dict2[y] = right.__getitem__(y)
            return DictList(dict1, dict2)
        if type(right) == dict:
            right = DictList(right)
            list_dict1 = []
            list_dict2 = []
            test = tuple()
            for x in self.dl:
                print(x)
                test.add(x)
                print(test)
            for x in self.dl:
                list_dict2.append(x)
            list_dict1.extend(list_dict2)
            return DictList(dict(list_dict1))
            
            




            
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
