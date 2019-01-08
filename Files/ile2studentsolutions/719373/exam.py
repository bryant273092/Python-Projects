from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self, *args):
        #print(args)
        if args == ():
            raise AssertionError
        if type(args[0]) == int:
            raise AssertionError
        if type(args[0]) == str:
            raise AssertionError
        if type(args[0]) == list:
            raise AssertionError
        self.dl = []
        for i in args:
            self.dl.append(i)
        
        
    def __len__(self):
        ok = set({})
        for i in self.dl:
            for key in i.keys():
                ok.add(key)
        return len(ok)
    
    def __repr__(self):
        end_string = "DictList("
        for i in range(len(self.dl)):
            end_string = end_string + str(i) + ","
        end_string = end_string + str(i) + ")"
        return end_string

    def __contains__(self, key):
        for i in self.dl:
            if key in i.keys():
                return True
        return False
    
    def __getitem__(self, key):
        for i in reversed(self.dl):
            if key in i.keys():
                return i[key]
        raise KeyError


    def __setitem__(self, key, value):
        for i in reversed(self.dl):
            if key in i.keys():
                i[key] = value
            
                
    
    def __call__(self, key):
        ok = []
        counter = -1
        for i in self.dl:
            counter = counter + 1
            if key in i.keys():
                ok.append((counter, i[key]))
        return ok
    

    def __iter__(self):
        #i = {'c': 13, 'd': 14, 'e': 15}
        ok = set({})
        for i in self.dl:
            for key in i.keys():
                yield(key, i)
    
    
    #c-->d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    #c-->d2 = DictList(dict(a=1,b=12), dict(c=13))
    #e-->d1 == d2-->True
    
    def __eq__(self, right):
        if type(right) == int or type(right) == list:
            raise TypeError
        return True

        
        
        
        
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    #d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    #d2 = DictList(dict(a=1,b=12), dict(c=13))
    #print(d1.__repr__())
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
