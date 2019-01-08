from goody import type_as_str  # Useful in some exceptions
from collections import defaultdict
class DictList:
    def __init__(self, *arg):
        self.dl = []
        self.arg = arg
        if len(arg) > 0:
            for a in arg:
                if type(a) != dict:
                    raise AssertionError(f"DictList.__init__: '{a} is not a dictionary")
                else:
                    self.dl.append(a)
        else:
            raise AssertionError(f"DictList.__init__: '{arg} is not a dictionary")

    def __len__(self):
        s = set()
        for item in self.dl:
            for k in item.keys():
                s.add(k)
        return len(s)
    def __repr__(self):
        return f'DictList{self.arg}'
    def __contains__(self, item):
        if any(item in val for val in self.dl):
            return True
        return False
    def __getitem__(self,item):
        a = defaultdict(dict)
        if self.__contains__( item):
           
            for val in self.dl:
                
                if val.get(item, None) != None:
                    a[item] = val[item]
            return a[item]
        else:
            raise KeyError(f"DictList.__getitem__: '{item} is not a key")
    def __setitem__(self, key, value):
        if self.__contains__(key):
            for item in self.dl[::-1]:
                if key in item:
                    item[key] = value
                    break
        else:
            self.dl.append({key:value})
            
    def __call__(self, value):
        num = -1
        lst = []
        if self.__contains__(value):
            for item in self.dl:
                num += 1
                if value in item:
                    
                    lst.append((num, item[value]))
            return lst
        else:
            return []
        
    def __iter__(self):
        repeat = []
        lst = []
        print(self.dl)
        for i in self.dl[::-1]:
            for k,v in i.items():
                if k not in repeat:
                    lst.append((k,v))
                    repeat.append((k,v))
            lst = sorted(lst)
        return iter(lst)
    def __eq__(self, right):
        val = True
        if type(right) == DictList:

            for dic in self.dl:
                for k,v in dic.items():
                    if right.__contains__(k) and self.__getitem__(k) == right.__getitem__(k): # the key in left is in right\
                        val =  True
                    else:
                        val = False
                        return val
            return val
        elif type(right) == dict:
            for dic in self.dl:
                for k,v in dic.items():
                    if k in right and self.__getitem__(k) == right[k]:
                        val = True
                    else:
                        val = False
                        return val
            return val
        else:
            raise TypeError(f"DictList.__eq__: '{right} is not type dict of DictList, it is type{type(right)}")
        
        
    def __add__(self, right):
        if type(right) == DictList:
            empty = {}
            right_empty = {}

            for d in self.dl:
                for k,v in d.items():
                    
                    empty[k] = v
            for r in right.dl:
                for k,v in r.items():
                    right_empty[k] = v
            return DictList(empty, right_empty)
        elif type(right) ==  dict:
            empty = {}
            for d in self.dl:
                for k,v in d.items():
                    
                    empty[k] = v
            return f'{DictList(right, empty)}'
        else:
            raise TypeError("in __add__: type of right is not Dictlist or Dict, can't add together, it is type {type(right)}")
            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    #driver tests
    '''
    d = DictList({'a': 1, 'b': 2}, {'b': 12, 'c': 13})
    d1 = {'a': 'one', 'b': 'two'}
    print(d + d1)
   # print(repr(d))
   '''
   
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
