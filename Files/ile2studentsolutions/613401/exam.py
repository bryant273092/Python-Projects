from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        for a in args:
            if a == None:
                raise AssertionError
        for a in args:
            if type(a) != dict:
                raise AssertionError
        self.dl = []
        for a in args:
            self.dl.append(a)
            
    def __len__(self):
        key_set = set()
        for x in self.dl:
            for i in x:
                key_set.update(i)
        return len(key_set)
    
    def __repr__(self):
        return ('DictList(' + ','.join(str(c) for c in self.dl) + ')')
    
    def __contains__(self, arg):
        for x in self.dl:
            for i in x.keys():
                if arg == i:
                    return True
          
    def __getitem__(self, k):
        key_list = []
        for i in self.dl:
            for x in i.keys():
                key_list.append(x)
        if k not in key_list:
            raise KeyError
        for x in self.dl[-1:]:
            return x[k]
                
                            
    def __setitem__(self, k, v):
        for x in self.dl:
            if k in x.keys():
                for i in self.dl[-1:]:
                    x[k] = v

                         
    def __call__(self, k):
        list_call = []
        for i in self.dl:
            if k in i.keys():
                list_call.append((self.dl.index(i), i[k]))
        return list_call

#     
#     
         
            




            
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
