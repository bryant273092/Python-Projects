from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        for item in args :
            if type(item) != dict or item == {} :
                raise AssertionError(item + 'is not a dictionary.')
            if type(item) == dict :
                self.dl.append(item)
            
    def __len__(self):
        num_keys = 0  # self.dl is list 
        for i in self.dl :
            for key in i :
                if key in i :
                    if i == key :
                        num_keys = 0
                    num_keys += len(key)
        return num_keys
    
    def __repr__(self):
        empty_str = ''
        for i in self.dl :
            empty_str = 'DictList (' + ','.join(str(i)) + ')'
        return empty_str
    
    def __contains__(self):
        for i in self.dl :
            for j in self.dl[i] :
                if self.dl[i][j] == self.dl[i+1][j+1] :
                    return True
                return False

        
    def __getitem__(self):
        for i in self.dl :
            for j in self.dl[i] :
                if self.dl[i][j] not in self.dl[i+1][j+1] :
                    raise KeyError(self.dl[i][j] + 'appears in no dictionaries.')
                return self.dl[i][j]
            
                
    def __setitem__(self):
        pass
    
    def __call__(self):
        pass
    
    def __iter__(self):
        pass
    
    def __eq__(self, right):
        if type(self) == type(right) :
            return True
        return False
    
            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    #d = DictList({'a' : 1, 'b' : 2, 'c' : 3}, {'c' : 13, 'd' : 14, 'e' : 15}, {'e' : 25, 'f' :26, 'g' : 27})
    

    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
