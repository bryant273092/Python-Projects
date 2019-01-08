from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self, *args):
        self.dl = []

        for e in args:
            if (type(e) != dict):
                raise AssertionError
            self.dl.append(e)

            
    def __len__(self):
        count = 0
        unique = set()
        for d in self.dl:
            for key in d.keys():
                if key not in unique:
                    count += 1
                unique.add(key)
        return count
    
    def __repr__(self):
        s = ""
        for d in self.dl:
            s+="{"
            for k, v in d.items():
                s+=f"{k}:{v}"
            s+="}"
        return f"DictList({s})"
    
    def __contains__(self, key):
        for d in self.dl:
            for k in d.keys():
                if key == k:
                    return True
        return False
    
    def __getitem__(self, k):
        vk = ""
        highest = 0
        for d in self.dl:
            for key, value in d.items():
                if k == key:
                    if value > highest:
                        highest = value
                        vk = key
        if vk == "":
            raise KeyError
        return highest
     
    def __setitem__(self, k, v):
        for i in range(len(self.dl)-1, -1, -1):
            for key in self.dl[i].keys():
                if k == key:
                    self.dl[i][k] = v
    
    def __iter__(self):
        variables = set()
        for i in range(len(self.dl)-1, -1, -1):
            for key, value in sorted(self.dl[i].items()):
                if (key not in variables):
                    yield (key, value)
                variables.add(key)
    
    def __eq__(self, right):
        if (type(right) == DictList):
            for d in self.dl:
                for key, value in d.items():
                    if key not in [x for y in right.dl for x in y.keys()]:
                        return False
            return True
        elif (type(right) == dict):
            for d in self.dl:
                for key, value in d.items():
                    if key not in right:
                        return False
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
