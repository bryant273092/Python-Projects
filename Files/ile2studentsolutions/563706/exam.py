from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*arg):
        if len(arg)==0:
            raise AssertionError
        dict_list=[]
        for param in arg:
            if type(param)!=dict:
                raise AssertionError
            else:
                dict_list.append(param)
        self.dl=dict_list
    
    def __len__(self):
        valid_list=[]
        for dict in self.dl:
            for key,value in dict.items():
                if key not in valid_list:
                    valid_list.append(key)
        return(len(valid_list))
    
    def __repr__(self):
        return_str= 'DictList('
     
        for dict in self.dl:
            return_str+= repr(dict)
            return_str+= ', '
               
            
        final= return_str[:-1]
        yes = final[:-1]
        yes += ')'
        return yes
    
    def __contains__(self, arg):
        for dict in self.dl:
            if arg in dict:
                return True
        return False
    
    def __getitem__(self,arg):
        return_num=0
        is_in=False
        for dict in self.dl:
            for key,value in dict.items():
                if arg==key:
                    is_in=True
        if is_in==False:
            raise KeyError
        
        for dict in self.dl:
            for key,value in dict.items():
                if arg==key:
                    if value>return_num:
                        return_num=value
        return return_num
    
    def __setitem__(self, k, v):
        
        return_num=0
        is_in=False
        for dict in self.dl:
            for key,value in dict.items():
                if k==key:
                    is_in=True
        if is_in:
            for dict in self.dl:
                for key,value in dict.items():
                    if k == key:
                        if value>return_num:
                            return_num=value
                            
            for dict in self.dl:
                for key,value in dict.items():
                    if key==k and return_num==value:
                        dict[key]=v
        
        else:
            self.dl.append({k:v})
            
    def __call__(self, key):
        return_list=[]
        index_counter=0
        for dict in self.dl:
            for k,v in dict.items():
                if key==k:
                    return_list.append((index_counter, v))
            index_counter+=1
        return return_list
    

    
    def __eq__(self,right):
        first_key=[]
        second_key=[]
        if type(right) != DictList and type(right) != dict:
            raise TypeError('WrongType')
        
        if type(right)== DictList:
            '''
            for dictionary in self:
                for key in dictionary.keys():
                    if key not in first_key:
                        first_key.append(key)
                        
            for dictionary in right:
                for key in dictionary.keys():
                    if key not in second_key:
                        second_key.append(key)
                        
                       
            for keys in first_key:
                if keys not in second_key:
                    return False
            '''
            return False       
        
        elif type(right) == dict:
            '''
            for dictionary in self:
                for key,value in dictionary.items():
                    if key not in first_key:
                        first_key.append(key)
            
            for key in first_key:
                if key not in right.keys():
                        return False
                return True  
            '''
            return True
      
               
        
        if type(right) not in (DictList,dict):
            raise TypeError
        
        
                
    def __iter__(self):
        pass




            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d0 = dict(a=1,b=2,c=3)
    d1= dict(c=13,d=14,e=15)
    d    = DictList(d0,d1)
    print(repr(d))

    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
