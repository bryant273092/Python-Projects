from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self, *args):
        
        self.dl = [args]
        
        for arg in self.dl:
            if type(arg) != dict or arg == None:
                raise AssertionError("Dictlist.__init__:" + '"' + str(arg) + '"' + "is not a dictionary")
            self.dl.append(arg)
            
    def __len__(self):
        return sum([len(x) for x in self.dl])
    
    def __repr__(self):
        
        string = "DictList(" 
        for d in self.dl:
            string += str(d) + ","
        string = string[0:-1]
        string += ")"
        return string
        
    def __contains__(self, arg):
        for key in self.dl:
            if arg in self.dl or self.dl[key]:
                return True
        return False
        
    def __getitem__(self):
        pass


            
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
