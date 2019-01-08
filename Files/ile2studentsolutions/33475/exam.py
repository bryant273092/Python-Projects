from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        if len(args) == 0:
            raise AssertionError
        for arg in args:
            if not isinstance(arg, dict):
                raise AssertionError("DictList.__init__: " + str(arg) + "is not a dictionary.")
        self.dl = [arg for arg in args]
    
    def __len__(self):
        results = set()
        for item in self.dl:
            for k in item:
                results.add(k)
        return len(results)

    def __repr__(self):
        outStr = ""
        for item in self.dl:
            outStr += (str(item) + ", ")
        outStr = outStr[:-2]
        return "DictList(" + outStr + ")"
    
    def __contains__(self, item):
        cont = False
        for d in self.dl:
            for k in d:
                if k == item:
                    cont = True
        return cont
    
    def __getitem__(self, item):
        result = "no" 
        for d in self.dl:
            for k in d:
                if k == item:
                    result = d[k]
        if result == "no":
            raise KeyError("Get Item Error! " + str(item) + " is not a key in any dictionaries in this DictList")
        return result
    
    def __setitem__(self, item, value):
        index = "no"
        for i in range(len(self.dl)):
            for k in self.dl[i]:
                if k == item:
                    index = i
        if index != "no":
            self.dl[index][item] = value
        else:
            self.dl.append({item:value})
            
    def __call__(self, item):
        tupList = []
        for i in range(len(self.dl)):
            for k in self.dl[i]:
                if k == item:
                    tupList.append((i,self.dl[i][k]))
        return sorted(tupList, key = lambda x: x[0])
    
    def __iter__(self):
        rev = []
        for i in range(len(self.dl), 0, -1):
            rev.append(self.dl[i - 1])
            
        def gen(rev):
            used = set()
            for item in rev:   
                for k in sorted(item):
                    if k not in used:
                        yield (k, item[k])
                        used.add(k)
        return gen(rev)
    
    def __eq__(self, other):
        if not isinstance(other, dict) and not isinstance(other, DictList):
            raise TypeError
        else:
            eq = True
            for item in self.dl:
                for k in item:
                    if k not in other:
                        eq = False
                    elif self.__getitem__(k) != other.__getitem__(k):
                        eq = False     
        return eq
    
    def __add__(self, other):
        if not isinstance(other, dict) and not isinstance(other, DictList):
            raise TypeError("Addition Error! Cannot add DictList and " + type_as_str(other))
        else:
            if isinstance(other, DictList):
                bigD1 = {}
                for item in self.dl:
                    for k,v in item.items():
                        bigD1.update({k:v})
                bigD2 = {}
                for item in other.dl:
                    for k,v in item.items():
                        bigD2.update({k:v})
                return DictList(bigD1,bigD2)
            elif isinstance(other, dict):
                bigDlist = ""
                for item in self.dl:
                    #print(item)
                    bigDlist += (str(dict(item)) + ",")
                bigDlist = bigDlist[:-1]
                return eval("DictList( " + (bigDlist) + ", dict(other))")
        
    def __radd__(self, other):
        if not isinstance(other, dict) and not isinstance(other, DictList):
            raise TypeError("Addition Error! Cannot add DictList and " + type_as_str(other))
        else:
            if isinstance(other, DictList):
                bigD1 = {}
                for item in self.dl:
                    for k,v in item.items():
                        bigD1.update({k:v})
                bigD2 = {}
                for item in other.dl:
                    for k,v in item.items():
                        bigD2.update({k:v})
                return DictList(bigD2,bigD1)
            
            elif isinstance(other, dict):
                bigDlist = ""
                for item in self.dl:
                    bigDlist += (str(dict(item)) + ",")
                bigDlist = bigDlist[:-1]
                return eval("DictList( dict(other), " + (bigDlist) + " )")
        
        
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
