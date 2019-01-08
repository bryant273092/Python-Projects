from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        
        assert args != ()
        for i in args:
            assert type(i) == dict, f"DictList.__init__:{i} not a dictionary"
            self.dl.append(i)
            
    def __len__(self):
        result = set()
        for i in self.dl:
            for j, k in i.items():
                result.add(j)
        return len(result)
    
    def __repr__(self):
        result = ''
        for i in self.dl:
            result+=f"{i},"
        return "DictList(" + result.strip(',') + ")"
    
    def __contains__(self, item):
        check = False
        for i in self.dl:
            if item in i:
                return True
        return check
    
    def __getitem__(self, item):
        check = False
        result = None
        for i in self.dl:
            if item in i:
                check = True
                result = i[item]
        if check is False:
            raise KeyError("Key was not in any of the dictionaries")
        elif check is True:
            return result
        
    def __setitem__(self, item, value):
        check = False
        list1 = list(self.dl.__reversed__())
        for i in list1:
            if item in i:
                check = True
                i[item] = value
                break
        list2 = list(list1.__reversed__())
        if check==False:
            list2.append({item:value})
        self.dl = list2
        
    def __call__(self, item):
        result = []
        for i in range(len(self.dl)):
            if item in self.dl[i]:
                result.append((i,self.dl[i][item]))
        return result
    
    def __iter__(self):
        check = set()
        list1 = list(self.dl.__reversed__())
        for i in list1:
            for j,k in sorted(i.items()):
                if j not in check:
                    check.add(j)
                    yield ((j,k))
                    
    def __eq__(self, item):
        if type(item) == DictList:
            set1 = set()
            set2 = set()
            for i in self.dl:
                for j, k in i.items():
                    set1.add(j)
            for i in item.dl:
                for j, k in i.items():
                    set2.add(j)
            if set1 == set2:
                for i in set1:
                    if self.__getitem__(i) != item.__getitem__(i):
                        return False
                else:
                    return True
            else:
                return False
        elif type(item) == dict:
            set1 = set()
            for i in self.dl:
                for j, k in i.items():
                    set1.add(j)
            if set1 == set(item.keys()):
                for i in set1:
                    if self.__getitem__(i) != item[i]:
                        return False
                else:
                    return True
            else:
                return False
        else:
            raise TypeError('right operand is not a DictList or dict object')
        
    def __add__(self, item): 
        if type(item) == DictList:
            dict1 = {}
            dict2 = {}
            for i in self.dl:
                for j,k in i.items():
                    if j in dict1:
                        del dict1[j]
                        dict1.update({j:k})
                    else:
                        dict1.update({j:k})
            for i in item.dl:
                for j,k in i.items():
                    if j in dict2:
                        del dict2[j]
                        dict2.update({j:k})
                    else:
                        dict2.update({j:k})
            return DictList(dict1, dict2)
                 
        elif type(item) == dict:
            x = []
            copied = self.dl.copy()
            for i in copied:
                x.append(i)
            return DictList(*x, item)
            
        else:
            raise TypeError('right operand is not a DictList or dict object')
        
    def __radd__(self, item):
        return self + item
                    
        
                
                
                    



            
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
