from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self, *args):
        if len(args) == 0:
            raise AssertionError("Argument is empty")
        if type(args) != dict:
            raise AssertionError("Argument is not a dictionary")
        else:
            self.dl.append(args)
    def __len__(self):
        emptyset = set()
        for k in self.dl:
            for keys in k:
                emptyset.add(keys)
        return len(emptyset)
                 
             
              
    def __repr__(self):
        pass
     
    def __contains__(self, right):
        for k in self.dl:
            for key in k:
                if key == right:
                    return False
        else:
            return True
           
    def __getitem__(self,item):
        pass
    
    def __setitem__(self):
        pass
    
    def __call__(self, item):
        result = []
        count = 0
        for k in self.dl:
            for kays in k:
                if kays == item:
                    result.append(kays,count)
        return result
                    
    def __iter__(self):
        pass
    def __eq__(self, right):
        if type(right) == int:
            raise TypeError
        if type(self.dl) == type(right):
            return False
        else:
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
