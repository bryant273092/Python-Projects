from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *everything):
        self.everything = everything
        self.dl = []
        
        for stuff in self.everything:
            if type(stuff) != dict or len(stuff) == 0:
                raise AssertionError
            
            elif type(stuff) == dict or len(stuff) != 0:
                self.dl.append(stuff)
#                 for key in stuff.items():
#                     self.dl.append(key)
#             
            else:
                raise AssertionError
            
        if len(self.everything) == 0:
            raise AssertionError 
           
  #     print(self.dl)
# c-->d0 = dict(a=1,b=2,c=3)
# c-->d1 = dict(c=13,d=14,e=15)
# c-->d2 = dict(e=25,f=26,g=27)
# 
# # Test __len__
# c-->d = DictList(d0)
# e-->len(d)-->3
# c-->d = DictList(d0,d1)
# e-->len(d)-->5
# c-->d = DictList(d0,d2)
# e-->len(d)-->6
# c-->d = DictList(d0,d1,   
    def __len__(self):
        result = []
        for stuff in self.everything:
            for key,value in stuff.items():
                if key not in result:
                    result.append(key)
                    
        return len(result)
        
        

    def __repr__(self):
        for stuff in self.dl:
            return 'DictList({})'.format(stuff)
        
# c-->d0 = dict(a=1,b=2,c=3)
# c-->d1 = dict(c=13,d=14,e=15)
# c-->d2 = dict(e=25,f=26,g=27)     
   
# c-->d = DictList(dict(a=1,b=2,c=3),dict(c=13,d=14,e=15))
# e-->'b' in d-->True
# e-->'d' in d-->True
# e-->'f' in d-->False
    def __contains__(self,item):
        for stuff in self.everything:
#             for key,value in stuff.items():
            if item in stuff:
                 return True
            elif item not in stuff:
                return False
            else:
                return False
        
#         if item in DictList:
#             return True
#         return False
#         
# 
#         for stuff in self.dl:
#             for key,value in stuff.items():
#                 if item in DictList:
#                     return True
#                 return False
#            

    def __getitem__(self,item):
        for stuff in self.dl:
            for key,value in stuff.items():
                if item == key:
                    self.dl[item] = int(value)
                    
                elif key not in stuff:
                    raise KeyError
                else:
                    raise KeyError
   
    def __setitem__(self,item,value):
        
        for stuff in self.dl:
            for key in stuff.items():
                if item in key:
                    self.dl[item][key] = value
                else:
                    raise KeyError
                    
        
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
