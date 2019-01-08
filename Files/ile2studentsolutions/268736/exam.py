from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        for a in args:
            if a == {}:
                raise AssertionError("DictList.__init__: '\
    {dl}' is an empty dictionary.")
            elif type(a) != dict:
                raise AssertionError("DictList.__init__: '\
    {dl}' is not a dictionary.")
            else:
                self.dl.append(a)
    
    def __len__(self):
        dict_list = []
        counter = 0
        for item in self.dl:
            for k in item.keys():
                if dict_list == []:
                    dict_list.append(k)
                elif k in dict_list:
                    pass
                else:
                    dict_list.append(k)
            
        return len(dict_list)
    
    def __repr__(self):
        return_str = ''
        for i in self.dl:
            return_str += str(i) + ', '
        r_str = return_str[:-2]
        return 'DictList(' + r_str + ')'
    
    def __contains__(self, left):
        dict_list = []
        for item in self.dl:
            for k in item.keys():
                if dict_list == []:
                    dict_list.append(k)
                elif k in dict_list:
                    pass
                else:
                    dict_list.append(k)
                    
        if left in dict_list:
            return True
        else:
            return False
        
    def __getitem__(self, letter):
        num_list = []
        dict_list = []
        
        for item in self.dl:
            for i in item.keys():
                dict_list.append(i)
                
        if letter not in dict_list:
            raise KeyError
                
        for item in self.dl:
            if letter in item.keys():
                num_list.append(item[letter])
            else:
                pass
        if len(num_list) == 1:
            for i in num_list:
                return i
        else:
            return max(num_list)
        
    def __setitem__(self, letter, new_v):
        dict_list = []
        
        for item in self.dl:
            for i in item.keys():
                dict_list.append(i)
        
        for item in self.dl:
            if letter in item.keys() and item[letter] == self.__getitem__(letter):
                item[letter] = new_v
                
        if letter not in dict_list:
            self.dl.append({letter: new_v})
            
    def __call__(self):
        pass
    
    def __iter__(self):
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
