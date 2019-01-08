from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        assert args != None, "Parameters must not be none"
        self.dl = []
        for i in args:
            assert type(i) == dict, "Parameters must be dict"
            self.dl.append(i)
            
        assert self.dl != [], "Number of arguments must be greater than 0"
        
    def __len__(self):
        list_of_keys = []
        for i in self.dl:
            for j in i:
                if(j not in list_of_keys):
                    list_of_keys.append(j)
        return len(list_of_keys)
    
    def __repr__(self):
        return("DictList(" + ",".join([str(i) for i in self.dl]) + ")")
    
    def __contains__(self, value):
        for i in self.dl:
            for j in i:
                if(value == j):
                    return True
        return False
            
    def __getitem__(self, value):
        for i in reversed(self.dl):
            for j in i:
                if(value == j):
                    return i[j]
        raise KeyError("The value is not in any of the dictionaries")
    
    def __setitem__(self, k, value):
        for i in reversed(self.dl):
            for j in i:
                if(k == j):
                    i[j] = value
                    return None
        newdict = dict()
        newdict[k] = value
        self.dl.append(newdict)
        
    def __call__(self, value):
        result = []
        for i in range(len(self.dl)):
            for j in self.dl[i]:
                if(value == j):
                    result.append((i,self.dl[i][j]))
        return result
    
    def __iter__(self):
        list_of_keys = []
        for i in reversed(self.dl):
            for j in i:
                if(j not in list_of_keys):
                    list_of_keys.append(j)
                    yield (j, i[j])
                    
    def __eq__(self, right):
        if(type(right) == DictList):
            list_of_keys = []
            for i in self.dl:
                for j in i:
                    if(j not in list_of_keys):
                        list_of_keys.append(j) 
                        
            for i in right.dl:
                for j in i:
                    if(j not in list_of_keys):
                        return False
                    
            for i in list_of_keys:
                if(self.__getitem__(i) != right.__getitem__(i)):
                    return False
            return True
        
        elif(type(right) == dict):
            for i in self.dl:
                for j in i:
                    if(j not in right):
                        return False
            for i in right:
                if(self.__getitem__(i) != right[i]):
                    return False 
            return True
        
        else:
            raise TypeError("Right value must be a DictList or dict")
        
        
    def __add__(self, right):
        if(type(right) == DictList):
            left_dict = dict()
            right_dict = dict()
            for i in self.dl:
                for j in i:
                    left_dict[j] = i[j]
            for i in right.dl:
                for j in i:
                    right_dict[j] = i[j]
            return DictList(left_dict, right_dict)

        
        elif(type(right) == dict):
            result = []
            for i in self.dl:
                result.append(i)
            result.append(right.copy())
            return DictList(*result)


        else:
            raise TypeError("Right value must be a DictList or dict")
        
    def __radd__(self, right):
        if(type(right) == dict):
            result = []
            result.append(right.copy())
            for i in self.dl:
                result.append(i)
            return DictList(*result)
        
        else:
            raise TypeError("Right value must be a DictList or dict")
        

            
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
