from goody import type_as_str  # Useful in some exceptions
from collections import defaultdict

class DictList:
    def __init__(self, *dicts):
        self.dl = []
        for dictionary in dicts:
            assert type(dictionary) == dict, 'DictList.__init__: {} is not a dictionary'.format(dictionary)
            self.dl.append(dictionary)
        if self.dl == []:
            raise AssertionError('DictList.__init__: None is not a dictionary')
    def __len__(self):
        length = defaultdict(int)
        for dic in self.dl:
            for k, v in dic.items():
                length[k] += 1
        return len(length)
    def __repr__(self):
        string = 'DictList('
        for dictionary in self.dl:
            stri = str(dictionary) + ', '
            string += stri
        return string[:-2] + ')'
    def __contains__(self, value):
        for dictionary in self.dl:
            if value in dictionary:
                return True
        return False
    def __getitem__(self, k):
        for dictionary in reversed(self.dl):
            if k in dictionary:
                return dictionary[k]
        raise KeyError('DictList.__getitem__: that is not a valid key')
    def __setitem__(self, k, v):
        for dictionary in reversed(self.dl):
            if k in dictionary:
                dictionary[k] = v
                return
        self.dl.append({k: v})
    def __call__(self, k):
        assoc = []
        for num, dictionary in enumerate(self.dl, 0):
            for value in dictionary.keys():
                if k == value:
                    assoc.append((num, dictionary[k]))
        return assoc
    def __iter__(self):
        app = []
        for dictionary in reversed(self.dl):
            for k, v in sorted(dictionary.items()):
                if k not in app:
                    app.append(k)
                    yield(k, v)
    def __eq__(self, right):
        if type(right) == dict:
            for dictionary in reversed(self.dl): 
                for k, v in dictionary.items():
                    try:
                        if self.__getitem__(k) == right[k]:
                            pass
                        else:
                            return False
                    except:
                        return False
            
            return True
        elif type(right) == type(self):
            if len(right) == len(self):
                for dictionary in reversed(self.dl):
                    for k, v in dictionary.items():
                        try:
                            if self.__getitem__(k) == right[k]:
                                pass
                            else:
                                return False
                        except:
                            return False
                    
                return True
            else:
                return False
        else:
            raise TypeError('DictList.__eq__: not a dict or DictList')
    def __add__(self, right):
        if type(right) == dict:
            return DictList(self.dl.copy(), right)
        elif type(right) == type(self):
            li = [dictionary for dictionary in self.dl.copy()] + [dictionary for dictionary in right.dl.copy()]
            return DictList(tuple([dictionary for dictionary in self.dl.copy()] + [dictionary for dictionary in right.dl.copy()])) 
            
        else:
            raise TypeError('DictList.__add__: cannot add')      
    def __radd__(self, left):
        return left + self  

            
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
