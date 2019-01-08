from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,dit):
        if type(dit) != dict:
            raise AssertionError('Not a dictionary')
        else:
            self.dl = dit
    def __len__(self):
        checker = []
        for coin in self.dl:
            for val in coin:
                checker.append(val)
        checker = set(checker)
        return len(checker)
    
    def __repr__(self):
        pass
    
    def __contains__(self):
        for val in self.dl:
            if val in val.keys():
                return True
            else:
                return False
    def __getitem__(self,val):
        for val in self.dl():
            if val in val.keys():
                final = val.value()
            else:
                continue
        if final == '':
            raise KeyError(val,"appears in no dictionaries")
        else:
            return final
    
    def __setitem__(self,ind, passed):
        for c in self.db():
            if ind in c.keys():
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
