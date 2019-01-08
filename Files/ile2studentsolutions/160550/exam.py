from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *kargs):
        self.dl = list(kargs)
        if len(kargs) == 0:
            raise AssertionError("There are no dictionaries in argument")
        for i in kargs:
            if type(i) != dict:
                raise AssertionError("Argument is not type dict")

    
    def __len__(self):
        result = []
        for i in self.dl:
            for j in i.keys():
                result.append(j)
        num = len(set(result))
        return num
 
    def __repr__(self):
            return "DictList{}".format(tuple(self.dl))
     
    def __contains__(self, item):
        for i in self.dl:
            for j in i.keys():
                if item == j:
                    return True
        return False
     
    def __getitem__(self, key):
        new_dict = dict()
        for i in self.dl:
            for j, k in i.items():
                new_dict.update({j:k})
        if key in new_dict.keys():
            return new_dict[key]
        raise KeyError("'{}' appears in no dictionaries".format(key))
    
    def __setitem__(self, key, value):
        new_dict = dict()
        for i in self.dl:
            for j, k in i.items():
                new_dict.update({j:k})
        if key in new_dict.keys():
            for i in self.dl:
                for j, k in i.items():
                    if new_dict[key] == k:
                        i[key] = value
        for i in self.dl:
            if key in i.keys():
                return
        self.dl.append({key:value})
        
        
    def __call__(self, key):
        result = []
        for i in range(len(self.dl)):
            if key in self.dl[i].keys():
                result.append((i,self.dl[i][key]))
        return result
        
        
        
    def __iter__(self):
        new_dict = dict()
        for i in self.dl:
            for j, k in i.items():
                new_dict.update({j:k})
        def gen(bins):
            for x, y in bins.items():
                yield (x, y)
        return gen(new_dict)
    
    
    def __eq__(self, item):
        if type(item) != dict and type(item) != DictList:
            raise TypeError
        new_dict = dict()
        for i in self.dl:
            for j, k in i.items():
                new_dict.update({j:k})
        return new_dict == item
            

            
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
