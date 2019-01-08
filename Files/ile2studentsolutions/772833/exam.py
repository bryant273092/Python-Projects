from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self, *arg):
        self.dl = []
        
        if type(arg) is not tuple or len(arg) == 0:
            raise AssertionError()
        else:
            for element in arg:
                self.dl.append(dict(element))
    
    def __len__(self):
        set1 = set()
        for dictionary in self.dl:
            for key, value in dictionary.items():
                set1.add(key)
        return len(set1)
    
    def __repr__(self):
        return 'DictList' + str((d) for d in self.dl) 
    
    def __contains__(self, arg):
        keys = []
        for dict1 in self.dl:
            for key in dict1.keys():
                keys.append(key)
        
        if arg in keys:
            return True
        else:
            return False
        
    def __getitem__(self, index):
        keys = []
        for dict1 in self.dl:
            for key in dict1.keys():
                keys.append(key)
        
        for dict1 in self.dl:
            if index not in keys:
                raise KeyError
            else:
                return dict1[index]
        
    def __setitem__(self, k, v):
        for dict1 in self.dl:
            if k in dict1.keys():
                self.dl[-1][k] = 'new1'
                return dict1[k]
            
    def __call__(self, index):
        list1 = []
        for dict1 in self.dl:
            for keys, values in dict1.items():
                if index in keys:
                    list1.append((0, values))
        return list1
    
    def __eq__(self, right):
        for dict1 in self.dl:
            if dict1 == right:
                return True
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
