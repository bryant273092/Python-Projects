from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self,*args):
        assert len(args) != 0, 'No argument was given'
        self.dl = []
        for dicts in args:
            assert type(dicts) == dict, str(dict) + 'is not a dictionary'
            self.dl.append(dicts)
    
    def __len__(self):
        set1 = set()
        for dicts in self.dl:
            for key in dicts: set1.add(key)
        return len(set1)
    
    def __repr__(self):
        return 'DictList(' + ", ".join(str(dicts) for dicts in self.dl) + ')'
    
    def __contains__(self, key):
        for dicts in self.dl:
            if key in dicts: return True
        return False
    
    def __getitem__(self, key):
        for dicts in range(len(self.dl)-1,-1,-1):
            if key in self.dl[dicts]: return self.dl[dicts][key]
        raise KeyError(str(key) + ' appears in no dictionaries')
    
    def __setitem__(self,key,value):
        confirm = 0
        for dicts in range(len(self.dl)-1,-1,-1):
            if key in self.dl[dicts]: 
                self.dl[dicts][key] = value
                confirm = 1
                break
        if confirm == 0: self.dl.append({key:value})
        
    
    def __call__(self,key):
        list1 = []
        for i in range(len(self.dl)):
            if key in self.dl[i]: list1.append((i,self.dl[i][key]))
        return list1
    
    def __iter__(self):
        set1 = set()
        for i in range(len(self.dl)-1,-1,-1):
            for key,value in self.dl[i].items():
                if key not in set1: yield (key, value)
                set1.add(key)
    
    def __eq__(self,other):
        if type(other) != DictList and type(other) != dict: raise TypeError(str(other) + ' is not a DictList or dict')
        if type(other) == DictList:
            if self.__len__() != other.__len__(): return False
            for i in range(len(self.dl)-1,-1,-1):
                for key in self.dl[i]:
                    if not other.__contains__(key) or self.__getitem__(key) != other.__getitem__(key): return False
        else: 
            if self.__len__() != len(other): return False
            for i in range(len(self.dl)-1,-1,-1):
                for key in self.dl[i]:
                    if key not in other or self.__getitem__(key) != other[key]: return False
        return True
            



            
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
