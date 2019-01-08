from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        assert len(args) != 0, "No dictionaries provided."
        for d in args:
            assert type(d) == dict, "{} is not a dictionary".format(d)
        self.dl = []
        for d in args:
            self.dl.append(d)

    def __len__(self):
        unique = set()
        count = 0
        for d in self.dl:
            for k in d:
                if k not in unique:
                    unique.add(k)
                    count += 1
        return count
    
    def __repr__(self):
        result = "DictList("
        for d in self.dl:
            result += str(d) + ", "
        result = result.rstrip(", ")
        result += ")"
        return result
            
    def __contains__(self, value):
        for d in self.dl:
            for k in d:
                if k == value:
                    return True
        return False
    
    def __getitem__(self, key):
        result = None
        for d in self.dl:
            for k in d:
                if key == k:
                    result = d[k]
        if result == None:
            raise KeyError("{} does not appear in the dictionaries.".format(key))
        return result
                               
    def __setitem__(self, key, value):
        if key in self:
            latestDict = -1
            for d in range(len(self.dl)):
                for k in self.dl[d]:
                    if key == k:
                        latestDict = d
            self.dl[latestDict][key] = value
        else:
            self.dl.append({key:value})
    
    def __call__(self, key):
        result = []
        for d in range(len(self.dl)):
            for k in self.dl[d]:
                if key == k:
                    result.append((d,self.dl[d][k]))
        return result
    
    def __iter__(self):
        copy = eval(self.__repr__())
        iterated = set()
        for d in range(len(copy.dl)-1,-1,-1):
            for k in copy.dl[d]:
                if k not in iterated:
                    iterated.add(k)
                    yield (k,copy.dl[d][k])
        iterated = set()
    
    def __eq__(self, value):
        if type(value) == DictList:
            keys = set()
            for d in self.dl:
                for k in d:
                    keys.add(k)
                    if k not in value:
                        return False
            for d2 in value.dl:
                for k2 in d2:
                    if k2 not in self:
                        return False
            for k in keys:
                if self[k] != value[k]:
                    return False
            return True
        elif type(value) == dict:
            for k in value.keys():
                if k not in self:
                    return False
            for d2 in self.dl:
                for k2 in d2:
                    if k2 not in value.keys():
                        return False
            for k in value.keys():
                if self[k] != value[k]:
                    return False
            return True
        else:
            raise TypeError("{} is not of type dict or DictList.".format(value))
        
    def __add__(self, value, flipped = False):
        if type(value) == DictList:
            d1 = {}
            d2 = {}
            for d in self.dl:
                for k in d:
                    d1.update({k:d[k]})
            for d in value.dl:
                for k2 in d:
                    d2.update({k2:d[k2]})
            return DictList(d1,d2)
        elif type(value) == dict:
            if flipped:
                result = DictList(value)
                for d in self.dl:
                    result.dl.append(d)
                return result
            else:
                result = eval(self.__repr__())
                result.dl.append(dict(value))
                return result
        else:
            raise TypeError("{} is not of type dict or DictList".format(value))
    
    def __radd__(self,value):
        return self.__add__(value, True)
    
            
            



            
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
