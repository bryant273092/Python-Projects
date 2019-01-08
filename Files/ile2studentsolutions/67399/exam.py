from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *kargs):
        assert len(kargs) > 0, "DictList.__init__: length of kargs must be greater than 0"
        for i in kargs:
            if type(i) != dict:
                raise AssertionError(f"DictList.__init__: {i} is not a dictionary")
        self.dl = [i for i in kargs]
        
    def __len__(self):
        x = set()
        for i in self.dl:
            for item in i.keys():
                x.add(item)
        return len(x)
    
    def __repr__(self):
        return f"DictList({self.dl})"
    
    def __contains__(self, arg):
        return any(arg in i for i in self.dl)
    
    def __getitem__(self, value):
        x = []
        if any(value in i for i in self.dl) == False:
            raise KeyError(f"DictList.__getitem__: {value} appears in no dictionaries")
        else:
            for i in self.dl[::-1]:
                if value in i:
                    if value not in x:
                        x.append(value)
                        return i[value]
    
    def __setitem__(self, item, value):
        x = []
        for i in self.dl[::-1]:
            if item in i:
                if item not in x:
                    x.append(item)
                    i[item] = value
        if item not in x:
            self.dl.append({item: value})
    
    def __call__(self, value):
        l = []
        for i in self.dl:
            if value in i:
                l.append((self.dl.index(i), i[value]))
        return l
    
    def __iter__(self):
        x = []
        for i in self.dl[::-1]:
            for j in i:
                if j not in x:
                    x.append(j)
                    yield (j, i[j])
    
    def __eq__(self, right):
        l = []
        if type(right) == DictList:
            if self.dl == right.dl:
                return True
            else:
                for i in self.dl[::-1]:
                    for j in i:
                        if any(j in x for z in right.dl for x in z) == True:
                            return True
                            
            return False
        elif type(right) == dict:
            for i in self.dl[::-1]:
                for j in i:
                    if j in right:
                        return True
            return False
        else:
            raise TypeError(f"DictList.__eq__: {right} was type {type_as_str(right)} but should only be DictList or dict.")


            
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
