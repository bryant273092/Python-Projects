from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        for arg in args:
            assert type(arg) is dict, str(arg) + " is not a dictionary"
            self.dl.append(arg)
        assert self.dl!= []
    
    def __len__(self):
        result = []
        for d in self.dl:
            for key in d:
                result.append(key)
        return len(set(result))
    
    def __repr__(self):
        result = ','.join(str(a) for a in self.dl)
        return "DictList(" + result + ')'
    def __contains__(self, arg):
        for dict in self.dl:
            if arg in dict:
                return True
        return False
    def __getitem__(self, arg):
        if self.__contains__(arg) == True:
            result = []
            for dict in self.dl:
                if arg in dict:
                    result.append(dict[arg])
            return max(result)
        else:
            raise KeyError()
    def __setitem__(self, arg, value):
        if self.__contains__(arg) == True:
            result = []
            for d in range(len(self.dl)):
                if arg in self.dl[d]:
                    result.append(d)
            self.dl[max(result)][arg] = value
        else:
            self.dl.append(dict([(arg,value)]))
    def __call__(self, arg):
        result = []
        for d in range(len(self.dl)):
            if arg in self.dl[d]:
                result.append((d, self.dl[d][arg]))
        return result
    def __iter__(self):
        result = []
        for d in self.dl[::-1]:
            for key in d:
                if key not in result:
                    result.append(key)
                    yield (key, d[key])
    def __eq__(self, right):
        if type(right) not in (DictList, dict):
            raise TypeError()
        else:
            result = []
            result2 = []
            if type(right) is dict:
                for d in self.dl:
                    for key in d:
                        result.append(key)
                for a in right:
                    result2.append(a)
                if set(result) == set(result2):
                    for b in result:
                        if self.__getitem__(b) == right[b]:
                            pass
                        else:
                            return False
                    return True
                else:
                    return False
            elif type(right) is DictList:
                for d in self.dl:
                    for key in d:
                        result.append(key)
                for c in right.dl:
                    for key2 in c:
                        result2.append(key2)
                if set(result) == set(result2):
                    for b in result:
                        if self.__getitem__(b) == right.__getitem__(b):
                            pass
                        else:
                            return False
                    return True
                else:
                    return False
    def __add__(self, right):
        if type(right) not in (dict,DictList):
            raise TypeError()
        else:
            if type(right) is DictList:
                result = []
                result2 = []
                result3 = []
                for d in self.dl:
                    for key in d:
                        result.append(key)
                for a in set(result):
                    result2.append((a, self.__getitem__(a)))
                result = []
                for d2 in right.dl:
                    for key2 in d2:
                        result.append(key2)
                for b in set(result):
                    result3.append((b, right.__getitem__(b)))
                return DictList(dict(result2), dict(result3))
            
                        
            
                    
                    
                

        


            
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
