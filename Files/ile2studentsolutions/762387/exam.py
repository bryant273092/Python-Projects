from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        assert len(args) >= 1
        dictlist = []
        for e in args:
            if type(e) != dict:
                raise AssertionError
            else:
                dictlist.append(e)
        
        self.dl = dictlist
    
    def __len__(self):
        lenset = set()
        
        for e in self.dl:
            for k in e.keys():
                lenset.add(k)
        
        return len(lenset)
    
    def __repr__(self):
        result = "DictList("
        
        for d in self.dl:
            result += str(d) + ','
        
        #result += ")\n"
        final_result = result[:-1] + ")\n"
        #print(result)
        #print(final_result)
        return final_result
    
    def __contains__(self, key):
        for d in self.dl:
            if key in d:
                return True
        
        return False
    
    def __getitem__(self, key):
        
        for i in range(len(self.dl) -1, -1, -1): #sorted(self.dl, reverse = True):
            for k,v in self.dl[i].items():
                if k == key:
                    return self.dl[i][k]
        
        raise KeyError
    
    def __setitem__(self, key, value):
        for i in range(len(self.dl) -1, -1, -1): #sorted(self.dl, reverse = True):
            if key in self.dl[i]:
                self.dl[i][key] = value
                break
        
        condition = False
        
        for d in self.dl:
            if key in d:
                condition = True
                
        if condition == False:        
            self.dl.append({key:value})
    
    def __call__(self, key):
        result = []
        
        for i in range(len(self.dl)):
            for k,v in self.dl[i].items():
                if k == key:
                    result.append((i, v))
        
        return sorted(result, key = lambda x: x[0])
            
    
    def __iter__(self):
        result = []
        
        list_of_keys = []
        #print(list_of_keys)
        for i in range(len(self.dl) - 1, -1, -1): 
            for k,v in self.dl[i].items():
                if k in list_of_keys:
                    pass
                else:
                    list_of_keys.append(k)
                    result.append((k,v))
            
        
        return iter(result)
    
    def __eq__(self, right):
        if type(right) == dict:
            set_of_keys = {k for d in self.dl for k in d}
            converted = sorted(list(set_of_keys))
            #print(converted)
            
            try:
                #condition = False
                for k in converted:
                    #print("LEFT", self.__getitem__(k))
                    #print("RIGHT", right[k])
                    if self.__getitem__(k) != right[k]:
                        return False
                    
                        
                return True
            except KeyError:
                #print("TEST DICT")
                return False
        elif type(right) == DictList:
            try:
                set_of_keys = [k for d in self.dl for k in d]
                converted = list(set_of_keys)
                
                for k in converted:
                    #print(self.__getitem__(k))
                    if self.__getitem__(k) != right.__getitem__(k):
                        return False
                
                return True
            except KeyError:
                #print("TEST DICTLIST")
                return False
        else:
            raise TypeError
    
    def __add__(self, right):
        if type(right) == dict:
            result = [d for d in self.dl]
            right_copy = right.copy()
            result.append(right_copy)
            return DictList(*result)
        elif type(right) == DictList:
            left_dict = dict()
            right_dict = dict()
            
            for i in range(len(self.dl) - 1, -1, -1): 
                for k,v in self.dl[i].items():
                    if k not in left_dict:
                        left_dict[k] = v
            #print(left_dict)
            for i in range(len(right.dl) - 1, -1, -1): 
                for k,v in right.dl[i].items():
                    if k not in right_dict:
                        right_dict[k] = v
            #print(left_dict, right_dict)
            result = [left_dict, right_dict]
            
            return DictList(*result)
        else:
            raise TypeError
        
    #__radd__ = __add__
    def __radd__(self, right):
        if type(right) == dict:
            result = []#[d for d in self.dl]
            right_copy = right.copy()
            
            result.append(right_copy)
            
            for d in self.dl:
                result.append(d)
            return DictList(*result)
        elif type(right) == DictList:
            left_dict = dict()
            right_dict = dict()
            
            for i in range(len(self.dl) - 1, -1, -1): 
                for k,v in self.dl[i].items():
                    if k not in left_dict:
                        left_dict[k] = v
            #print(left_dict)
            for i in range(len(right.dl) - 1, -1, -1): 
                for k,v in right.dl[i].items():
                    if k not in right_dict:
                        right_dict[k] = v
            #print(left_dict, right_dict)
            result = [right_dict, left_dict]
            
            return DictList(*result)
        else:
            raise TypeError
        
        
    
            
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
