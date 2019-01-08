from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        if not args:
            raise AssertionError("DictList.__init__:", args, "is not a dictionary.")
        for item in args:
            if type(item) is dict:
                self.dl.append(item)
            else:
                raise AssertionError("DictList.__init__:", type_as_str(item), "is not a dictionary.")
    
    def __len__(self):
        return_set = set()
        for x in self.__dict__["dl"]:
            for key in x.keys():
                return_set.add(key)
        return len(return_set)
    
    def __repr__(self):
        return_str = ", ".join(str(x) for x in self.dl)
        
        return "DictList(" + return_str + ")"
            
    
    def __contains__(self, item):
        return any(item in x.keys() for x in self.dl)
    
    
    def __getitem__(self, item):
        return_value = ""
        for x in range(len(self.dl)):
            if item in self.dl[x].keys():
                return_value = self.dl[x][item]
        if return_value == "":
            raise KeyError(item, "appears in no dictionaries")
        return return_value
    
    
    def __setitem__(self, item, value):
        find_value = False
        for x in range(len(self.dl)-1, -1, -1):
            if item in self.dl[x].keys():
                self.dl[x][item] = value
                find_value = True
                break
        if not find_value:
            self.dl.append({item: value})
        
    def __call__(self, item):
        return_list = []
        for x in range(len(self.dl)):
            if item in self.dl[x].keys():
                return_list.append((x, self.dl[x][item]))
        return return_list
    
    
    def __iter__(self):
        new_list = []
        exist_key = []
        for x in range(len(self.dl)-1, -1, -1):
            new_list.extend(sorted(self.dl[x].items()))
        for y in new_list:
            if y[0] not in exist_key:
                exist_key.append(y[0])
                yield y
    
    
    def __eq__(self, right):
        if type(right) is dict:
            self_key_set = set()
            for x in self.__dict__["dl"]:
                for key in x.keys():
                    self_key_set.add(key)
            right_key_set = set(right.keys())
            if all(x == y for x,y in zip(sorted(list(self_key_set)),sorted(list(right_key_set)))) and all(right[x] == self.__getitem__(x) for x in sorted(list(right_key_set))):
                return True
            else:
                return False
                         
        elif type(right) is DictList:
            self_key_set = set()
            for x in self.__dict__["dl"]:
                for key in x.keys():
                    self_key_set.add(key)
            right_key_set = set()
            for x in right.__dict__["dl"]:
                for key in x.keys():
                    right_key_set.add(key)
            if all(x == y for x,y in zip(sorted(list(self_key_set)),sorted(list(right_key_set)))) and all(right.__getitem__(x) == self.__getitem__(x) for x in sorted(list(right_key_set))):
                return True
            else:
                return False
        else:
            raise TypeError
        
        
    def __add__(self, right):
        
        if type(right) is DictList:
            self_dict = {}
            self_key_set = set()
            for x in self.__dict__["dl"]:
                for key in x.keys():
                    self_key_set.add(key)
            for x in sorted(list(self_key_set)):
                self_dict[x] = self.__getitem__(x)
            right_dict = {}
            right_key_set = set()
            for x in self.__dict__["dl"]:
                for key in x.keys():
                    right_key_set.add(key)
            for x in sorted(list(right_key_set)):
                right_dict[x] = right.__getitem__(x)
            return DictList(self_dict, right_dict)
            
       
        elif type(right) is dict:
            self_list = []
            for x in self.dl:
                self_list.append(x.copy())
            self_list.append(right.copy())
            return DictList(*self_list)
            
            
        else:
            NotImplemented
        
    
    def __radd__(self, left):
        if type(left) != dict:
            raise TypeError
        self_list = []
        self_list.append(left.copy())
        for x in self.dl:
            self_list.append(x.copy())
        return DictList(*self_list)

        



            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    adict = dict(a='one',b='two')
    print (adict+d1)
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
