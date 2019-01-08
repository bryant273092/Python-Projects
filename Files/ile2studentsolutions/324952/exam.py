from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *d):
        if len(d) == 0:
            raise AssertionError('There are no dictionaries')
        for i in d:
            if type(i) != dict:
                raise AssertionError(f'{i} is not a dictionary')
        self.dl = d
        
    def __len__(self):
        result = set()
        for i in self.dl:
            for k in i:
                if k not in result:
                    result.add(k)
        return len(result)
    
    def __repr__(self):
        lst = []
        for i in self.dl: lst.append(str(i))
        return f'DictList({",".join(lst)})'
    
    def __contains__(self, item):
        for i in self.dl:
            for k in i:
                if item == k:
                    return True
        return False
    
    def __getitem__(self, item):
        result = None
        for i in self.dl:
            for k,v in i.items():
                if item == k:
                    result = v
        if result == None:
            raise KeyError
        return result
    
    def __setitem__(self, item, value):
        result = {}
        for i in range(len(self.dl)):
            for k,v in self.dl[i].items():
                if item == k:
                    result[k] = i
        if result != {}:
            for k,v in result.items():
                self.dl[v][k] = value
        else:
            result.update({item:value})
            
                
    
    def __call__(self, item):
        result = []
        for i in range(len(self.dl)):
            for k,v in self.dl[i].items():
                if item == k:
                    result.append((i,v))
        return result
    
    def __iter__(self):
        already_used = set()
        lst_of_tple = []
        for i in range(len(self.dl)):
            lst_of_tple.append([])
            for k,v in self.dl[i].items():
                if k not in already_used:
                    if (i,v) != self.__call__(k)[-1]:
                        pass
                    else:
                        already_used.add(k)
                        lst_of_tple[-1].append((k,self.__getitem__(k)))
        for i in sorted(lst_of_tple, reverse = True):
            for j in sorted(i):
                yield j
    
                    
    
    def __eq__(self, right):
        if type(right) == dict or type(right) == DictList:
            for i in self.dl:
                for k,v in i.items():
                    if k not in right:
                        return False
                    elif right[k] != self.__getitem__(k):
                        return False
            return True
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
