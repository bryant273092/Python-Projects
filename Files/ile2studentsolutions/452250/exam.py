from goody import type_as_str  # Useful in some exceptions
# from Tools.scripts.parse_html5_entities import temp_fname

class DictList:
    def __init__(self, *kwargs):
        self.kwargs = kwargs
        self.dl = []
        assert len(kwargs) != 0
#         assert type(ele for ele in kwargs) ==dict
        for ele in kwargs:
            self.dl.append(ele)
            
        
#             
#             


        
    def __len__ (self):
        
        temp = set()
        for small_dic in self.dl:
            for k in small_dic.keys():
                temp.add(k)
        return len(temp)
            
            
    def __repr__ (self):
        print ('self.dl is', self.dl)
        return ' "DictList( ' + '{}'.format(ele for ele in self.dl) + ')"'
    
    
    def __contains__(self, value):
#         print (self.dl, '3333333333333333')
        for small_dict in self.dl:
            print (small_dict)
            if value in small_dict.keys():
                return True
            else:
                return False
        
        
    def __getitem__(self, value):
        if value in self.dl[len(self.dl)-1].keys():
            return self.dl[len(self.dl)-1][value]
        elif value in self.dl[len(self.dl) -2].keys():
            return self.dl[len(self.dl)-2][value]
        elif value in self.dl[len(self.dl) -3].keys():
            return self.dl[len(self.dl)-3][value]
        else:
            raise KeyError
    def __set__item(self,key, value):
        temp = dict()
        for small_dict in self.dl[0:]:
            if key in small_dict.keys():
                small_dict[key] = value
            else:
                temp[key] = value
                self.dl.append(temp)
                
                
    def __call__(self,key, value):
        temp = []
        if key in self.dl[len(self.dl)-1].keys():
            outcome = (len(self.dl)-1, self.dl[len(self.dl)-1][key])
            temp.append(outcome) 
            return temp 
        elif key in self.dl[len(self.dl)-2].keys():
            outcome = (len(self.dl) -2, self.dl[len(self.dl)-2][key])
            temp.append (outcome)
            return temp
        elif key in self.dl[len(self.dl)-3].keys():
            outcome = (len(self.dl) -3, self.dl[len(self.dl)-3][key])
            temp.append(outcome)
            return temp
        else:
            return temp 
        
#     def __eq__(self, right):
#         for small_dict in self.dl:
#             for small_dict2 in right.dl:
#                 if small_dict['a'] == small_dict2['a']:
#                     return True 
#                 elif small_dict.__getitem__ == small_dict2.__getitem__:
#                     return True 
#                 else:
#                     return False 

        
        
    
                


            
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
