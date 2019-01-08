from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        if len(args) == 0:
            assert False, ('DictList.__init__: ' + str(args) + 'is not a dictionary')
        if len(args) > 1:
            for i in args:
                if type(i) == dict:
                    self.dl = [i]
        for i in args:
            if type(i) != dict:
                assert False, ('DictList.__init__: ' + str(args) + 'is not a dictionary')
            else:
                self.dl = [i]


    
    def __len__(self):
        count = 0
        for i in self.dl:
            count += len(i)
        return count
    
    def __repr__(self):
        return 'DictList(' + str(self.d) + ')'
    
    def __contains__(self, item):
        print(self.dl)
        for i in self.dl:
            print(i)
            if item in i.keys():
                return True
            else:
                return False
            
    def __getitem__(self, index):
        for i in self.dl:
            for j in i:
                if index != j:
                    raise KeyError(str(index) + 'appears in no dictionaries')
            else:
                self.dl[index]
    
    def __setitem__(self, item):
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
