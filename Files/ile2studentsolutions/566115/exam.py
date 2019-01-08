from goody import type_as_str  # Useful in some exceptions






class DictList:
    
    def __init__(*self):
        #match is expected to be a dictionary    
        # this init creates a DictList object with 3 dictionaries
        
        if not isinstance(self, dict) :
            raise AssertionError("argument is not a dictionary")
        
        

        
        
       
        
        
        
        
        
    def __len__(self,d):
        for i in self.d: # here im first inside the list
            for y in i:
                return len(i.keys())
            
#        29 c-->d = DictList(d0,d2)
#       *Error: previous command raised exception
#          exception: AssertionError
#          message  : argument is not a dictionary
#    
#            30 e-->len(d)-->6
#       *Error: previous command raised exception
#          exception: NameError
#          message  : name 'd' is not defined
    
    

    
    
    def __repr__(self):
        pass

    
    #########################################################
    def __contains__(self, word):
        for i in self.dl.keys():
            if word in i:
                return True
            else:
                return False
        
    def __getitem__(self,index):
        for i in self.dl:
            for y in i[index]:
                return i[index]
            
            
            
    def __setitem__(self, change):
        for i,j in self.dl:
            vals = j.values()
            return vals.replace(change)
            
            
    
    
#     
#     def __eq__(self, first_dict, second_dict):
#         if first_dict != DictList:
#             raise TypeError("msg")

            
             



            
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
