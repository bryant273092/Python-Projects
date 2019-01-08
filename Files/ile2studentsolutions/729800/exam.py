from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        if not args:
            raise AssertionError('DictList.__init__:{failed} is not a dictionary'.format(failed = args))
        for i in args:
            if type(i) is not dict:
                raise AssertionError('DictList.__init__:{failed} is not a dictionary'.format(failed = args))      
        self.dl = [i for i in args]
    def __len__(self):
        dict_set = set()
        for dic in self.dl:
            for element in dic.keys():
                dict_set.add(element)
        return len(dict_set)
    def __repr__(self):
        return 'DictList'+str(tuple((i for i in self.dl)))
    def __contains__(self, key):
        for dictionary in self.dl:
            if key in dictionary.keys():
                return True
        return False
    def __getitem__(self, key):
        if not self.__contains__(key):
            raise KeyError('DictList.__get__item.{key} does not exist in dictionary'.format(key=key))
        found_values = []
        for dictionary in self.dl:
            if key in dictionary.keys():
                found_values.append(dictionary[key])
        try: 
            return max(found_values)
        except:
            return self.dl[-1][key]
    def __setitem__(self,key, value):    
        if not self.__contains__(key):
            new_dict = {}
            new_dict[key]=value
            self.dl.append(new_dict)
        else:
            for dictionary in self.dl:
                for key1, element in dictionary.items():
                    if element == self.__getitem__(key) and key1 == key:
                        dictionary[key1] = value
    def __call__(self, key):
        tuple_list = []
        for i in range(len(self.dl)):
            if key in self.dl[i].keys():
                tuple_list.append((i, self.dl[i][key]))      
        return tuple_list
    def __iter__(self):
        tuple_set = set()
        for dictionary in self.dl:
            for key, item in sorted(dictionary.items(), key = lambda key: key):
                tuple_set.add((key,self.__getitem__(key) )) 
        for i in tuple_set:
            yield i 
    def __eq__(self, right):
        if type(right) is not DictList and type(right) is not dict :
            raise TypeError('Error, inappropriate type comparison')
        elif type(right) is dict:
            for key, item in right.items():
                if not self.__contains__(key):
                    return False
            return True
        print(type(right))
        for dictionary in right.dl:
            for key, item in dictionary.items():
                if not self.__contains__(key):
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
