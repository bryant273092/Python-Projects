from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        assert len(args) != 0
        for i in args:
            assert type(i) is dict
        self.dl = []
        for i in args:
            self.dl.append(i)
            
    def __len__(self):
        lst = []
        for i in self.dl:
            for k,v in i.items():
                if k not in lst:
                    lst.append(k)
        return len(lst)
                    
    def __repr__(self):
        lst = []
        for i in self.dl:
            lst.append(str(i))
        return "DictList({})".format(", ".join(lst))
    
    def __contains__(self, ltr):
        for i in self.dl:
            for k in i.keys():
                if k == ltr:
                    return True
        return False
    
    def __getitem__(self, ltr):
        for i in self.dl: 
            for k,v in i.items():
                if ltr == k:
                    return v
        raise KeyError
    
    def __setitem__(self, item, value):
        for i in self.dl:
            for k,v in i.items():
                if item == k:
                    i[item] = value
                if item not in k:
                    self.dl.append({item:value})
                    
    def __call__(self, ltr):
        lst = []
        for i in self.dl:
            x = list(enumerate(i))
            for k,v in i.items():
                if ltr in k:
                    for idx in x:
                        if ltr in idx[1]:
                            lst.append((idx[0],v))
                        
        return lst
        
    def __eq__(self, right):
        lst1 = []
        lst2 = [] 
        lst3 =[] 
        for x in self.dl:
            for k in x.keys():
                if k not in lst1:
                    lst1.append(k)
            for y in right.dl:
                for r in y.keys():
                    if r not in lst2:
                        lst2.append(r)
        if type(right) != DictList:
            raise TypeError
        if type(right) == dict:
            for x in right.keys():
                if x not in lst3:
                    lst3.append(x)
            return lst1 == lst3
        return lst1 == lst2
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
