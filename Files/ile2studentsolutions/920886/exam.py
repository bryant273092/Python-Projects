from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        assert len(args) >= 1
        for x in args:
            assert type(x) is dict, "DictList.__init__: " + str(x) + " is not a dictionary."
            self.dl.append(x)
            
    def __len__(self):
        result = set()
        for x in self.dl:
            for y in x.keys():
                result.add(y)
        return len(result)
    
    def __repr__(self):
        return "DictList(" + str(self.dl).strip('[').strip(']') + ")"
    
    def __contains__(self, arg):
        for x in self.dl:
            if arg in x.keys():
                return True
            
    def __getitem__(self, item):
        result = {}
        for x in self.dl:
            for k,v in x.items():
                result[k] = v
        if item in result:
            return result[item]
        else:
            raise KeyError(str(item) + " is not in the DictList.")
            
    def __setitem__(self, k, v):
        for x in range(len(self.dl) - 1, -1, -1):
            if k in self.dl[x]:
                self.dl[x][k] = v
            elif k not in self.dl[x]:
                self.dl.append({k:v})
                
    def __call__(self, k):
        result = []
        for x in range(len(self.dl)):
            if k in self.dl[x]:
                result.append((x, self.dl[x][k]))
        return result
    
    def __iter__(self):
        for x in range(len(self.dl) - 1, -1, -1):
            for k, v in sorted(self.dl[x].items()):
                yield (k, v)
    
    def __eq__(self, right):
        if type(right) is DictList:
            for x in self.dl:
                for y in right.dl:
                    for k in x:
                        for k2 in y:
                            if k in y and k2 in x and self[k] == right[k] and right[k2] == self[k2]:
                                return True
        elif type(right) is dict:
            for x in self.dl:
                for k in x:
                    if k in right and self[k] == right[k]:
                        return True
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
