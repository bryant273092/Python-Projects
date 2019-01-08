from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        if len(args) == 0:
            raise AssertionError('Expected one or more dictionaries')
        for arg in args:
            if type(arg) is not dict:
                raise AssertionError('Valid parameter must consist of one or more dictionaries')
        self.dl = [arg for arg in args]
    
    def __len__(self):
        result = set()
        for element in self.dl:
            for key in element.keys():
                result.add(key)
        return len(result)
    
    def __repr__(self):
        result = 'DictList('
        for element in self.dl:
            result += (str(element) + ', ')
        result = result[:-2] + ')'
        return result
    
    def __contains__(self, item):
        for element in self.dl:
            for key in element.keys():
                if key == item:
                    return True
        return False
    
    def __getitem__(self, item):
        for element in reversed(self.dl):
            for key in element.keys():
                if key == item:
                    return element[key]
        raise KeyError('Element not found')
    
    def __setitem__(self, item, value):
        for element in reversed(self.dl):
            for key in element.keys():
                if key == item:
                    element[key] = value
                    return
        self.dl.append({item:value})
        
    def __call__(self, item):
        result = []
        for index, element in list(enumerate(self.dl)):
            for key, value in element.items():
                if key == item:
                    result.append((index, value))
        return result
    
    def __iter__(self):
        result = []
        for element in reversed(self.dl):
            temp = []
            for key, value in element.items():
                temp.append((key, value))
            for tup in sorted(temp):
                result.append(tup)
        unique = []
        for element in result:
            if element[0] not in [i[0] for i in unique]:
                unique.append(element)
        for i in unique:
            yield i
                
    
    def __eq__(self, right):
        if type(right) not in [DictList, dict]:
            raise TypeError('Expected DictList or dict object')
        if type(right) is DictList:
            self_uniques = set()
            right_uniques = set()
            for element in self.dl:
                for key in element.keys():
                    self_uniques.add(key)
            for element in right.dl:
                for key in element.keys():
                    right_uniques.add(key)
            if self_uniques == right_uniques:
                pass
            else:
                return False
            for key in self_uniques:
                if self.__getitem__(key) != right.__getitem__(key):
                    return False
            return True
        else:
            self_uniques = set()
            for element in self.dl:
                for key in element.keys():
                    self_uniques.add(key)
            right_uniques = set(right.keys())
            if self_uniques == right_uniques:
                pass
            else:
                return False
            for key in self_uniques:
                if self.__getitem__(key) != right[key]:
                    return False
            return True
            
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
