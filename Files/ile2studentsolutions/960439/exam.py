from goody import type_as_str  # Useful in some exceptions
from collections import defaultdict
from unittest.mock import right
class DictList:
    def __init__(self, *args):
        if len(args) == 0:
            raise AssertionError('DictList.__init__: must have at least one argument to create DictList object')
        self.dl = []
        for argument in args:
            if type(argument) != dict:
                raise AssertionError(f'DictList.__init__:{argument} is not a dictionary')
            else:
                self.dl.append(argument)
    
    def __len__(self):
        dict_of_keys = dict()
        for dic in self.dl:
            for key in dic:
                dict_of_keys[key] = 1
        return sum(dict_of_keys.values())
            
    def __repr__(self):
        return 'DictList('+ ','.join([str(i) for i in self.dl]) + ')'

    def __contains__(self, search):
        return search in [key for dic in self.dl for key in dic]
    
    def __getitem__(self,search):
        
        result = None
        for item in self.dl:
            for key in item:
                if search == key:
                    result = item[key]
                    
        if result == None:
            raise KeyError(f'DictList.__getitem__:Key to be searched for ({search}) was not in the DictList')
        else:
            return result

    def __setitem__(self, the_key, value):
        a = None
        for item in self.dl:
            for key in item:
                if the_key == key:
                    a = (self.dl.index(item), key)
        if a != None:
            self.dl[a[0]][a[1]] = value
        else:
            self.dl.append({the_key: value})
    
    def __call__(self, search):
        result = []
        first = []
        second = []
        for item in self.dl:
            for key in item:
                if search == key:
                    result.append((self.dl.index(item), item[key]))
        return result
    
    def __iter__(self):
        checker = []
        for i in reversed(self.dl):
            for key in sorted(i):
                if key not in checker:
                    yield (key, i[key])
                    checker.append(key)
    
    def __eq__(self, right):
        def helper1(the_dictlist):
            dict_of_keys = {}
            for dic in the_dictlist.dl:
                for key in dic:
                    dict_of_keys[key] = dic[key]
            return dict_of_keys
        
        if type(right) is dict:
            return helper1(self) == right
#             for key in helper1(self):
#                 if DictList.__getitem__(self, key) != right[key]:
#                     return False
#             return sorted(helper1(self)) == sorted(right.keys()) 
        
        elif type(right) is DictList:
            
            return helper1(self) == helper1(right)
        else:
            raise TypeError(f'DictList.__eq__: right value must be of type dict or DictList, not {type(right)}')
    
    
            
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

