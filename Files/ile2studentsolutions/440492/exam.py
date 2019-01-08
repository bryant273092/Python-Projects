from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        if args is ():
            raise AssertionError("Can't be none")

        for arg in args:
            if type(arg) != dict:
                raise AssertionError('{} is not a dict'.format(arg))
    
        self.dl = []
        for i in args:
            self.dl.append(i)
            
    def __len__(self):
        unq_keys = []
        for dict_obj in self.dl:
            for key in dict_obj.keys():
                unq_keys.append(key)
        
        return len(set(unq_keys))
    
    def __repr__(self):
        rtrn_str = 'DictList('
        
        for dict_obj in self.dl:
            rtrn_str += str(dict_obj) + ','
        
        rtrn_str = rtrn_str[:-1] + ')'
        
        return rtrn_str
    
    def __contains__(self,input_key):
        for dict_obj in self.dl:
            for key in dict_obj.keys():
                if input_key == key:
                    return True
        
        return False
    
    def __getitem__(self,input_key):
        item = None
        for dict_obj in self.dl:
            for key in dict_obj.keys():
                if input_key == key:
                    item = dict_obj[key]
        
        if item == None:
            raise KeyError('{} is not in any dictionary'.format(input_key))
        else:
            return item
        
    
    def __setitem__(self,input_key,new_value):
        counter_list = []
        counter = 0
        for dict_obj in self.dl:
            counter += 1
            for key in dict_obj.keys():
                if input_key == key:
                    counter_list.append(counter)
        
        if counter_list == []:
            self.dl.append({input_key:new_value})
        else:
            self.dl[counter_list[-1]-1][input_key] = new_value
            
    
    def __call__(self,input_key):
        return_list = []
        counter = 0
        for dict_obj in self.dl:
            counter += 1
            for key in dict_obj.keys():
                if input_key == key:
                    return_list.append((counter-1,dict_obj[key]))
        
        return return_list
    
    def __iter__(self):
        keys_returned = []
        for i in range(len(self.dl),0,-1):
            for item in self.dl[i-1]:
                for key in sorted(item):
                    if key not in keys_returned:
                        keys_returned.append(key)
                        yield (key,self.dl[i-1][key])
                        
    
    def __eq__(self,DictLizt):
        self_unq_keys = []
        for dict_obj in self.dl:
            for key in dict_obj.keys():
                self_unq_keys.append(key)
                    
        if type(DictLizt) == DictList:
            unq_keys = []
            for dict_obj in DictLizt.dl:
                for key in dict_obj.keys():
                    unq_keys.append(key)
        
        elif type(DictLizt) == dict:
            unq_keys = set(DictLizt.keys())
            
        else:
            raise TypeError('{} is not dict or DictList'.format(DictLizt))
        
        if set(self_unq_keys) == set(unq_keys):
            for item in set(unq_keys):
                if self[item] != DictLizt[item]:
                    return False
            return True
            
        else:
            return False
            
        
        
        


            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d = DictList({'a':1,'d':6,'e':2},{'b':2},{'c':3},{'a':6})
    print(repr(d))
    d['a'] = 2
    print(d)
    for i in d:
        print(i)
        
    print(d == {'a':2,'b':2,'c':3,'d':6,'e':2})
        
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
