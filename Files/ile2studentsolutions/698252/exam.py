

class DictList:
    def __init__(self,*args):
        self.dl = []
        if args == ():
            raise AssertionError
        for dict_ in args:
            if type(dict_) != dict:
                raise AssertionError("DictList.__init__:{} is not a dictionary".format(dict_))
            else:
                self.dl.append(dict_)
    
    def __len__(self):
        list_unique = []
        #print("self.dl = ", self.dl)
        for val in self.dl:
            #print("val = ", val)
            for k in val.keys():
                #print("k = ", k)
                if k not in list_unique:
                    list_unique.append(k)
        #print("list_unique = ", list_unique)
        return len(list_unique)
    
    def __repr__(self):
        #print("DictList{}".format(tuple(self.dl)))
        return "DictList{}".format(tuple(self.dl))
    
    def __contains__(self,arg):
        for val in self.dl:
            if arg in val.keys():
                return True
        return False
    
    def __getitem__(self,arg):
        num = 0
        #print("self.dl = ", self.dl)
        for val in self.dl:
            if arg in val.keys():
                num = val[arg] 
        if num == 0:
            raise KeyError
        else:
            return num
    def __setitem__(self,k,v):
        #print("k = ", k)
        #print("v = ", v)
        #print("self.dl = ", self.dl)
        count = -1
        for val in self.dl.__reversed__():
            #print("val = ", val)
            if k in val.keys():
                #print("Entered")
                #print("self.dl[count] = ", self.dl[count])
                self.dl[count][k] = v
                return
            count -= 1
        #print("None matched")
        self.dl.append({k:v})

    def __call__(self,k):
        listed = []
        count = 0
        for val in self.dl:
            for key, val in val.items():
                if k == key:
                    listed.append((count,val))
            count += 1
        return listed
    
    def __iter__(self):
        listed = {}
        for val in self.dl.__reversed__():
            for k,v in val.items():
                if k not in listed.keys():
                    listed[k] = v
                    yield(k,v)
        
                        
    
    def __eq__(self,arg):
        #print("Arg = ", arg)
        if isinstance(arg, DictList):
#             print("Entered DictList")
#             print("arg = ", arg)
#             print("self.dl = ", self.dl)
            for val in self.dl:
                for k,v in val.items():
                    if self.__getitem__(k) != arg.__getitem__(k):
                        return False
            for val in arg.dl:
                for k,v in val.items():
                    if self.__getitem__(k) != arg.__getitem__(k):
                        return False
        elif type(arg) == dict:
#             print("Entered dict")
            for val in self.dl:
                for k,v in val.items():
                    if k not in arg.keys():
                        return False
                    elif self.__getitem__(k) != arg[k]:
                        return False
        else:
            #print("Entered Error Statement")
            raise TypeError("Argument must be type DictList or dict")
        return True
    
    def __add__(self,arg):
        dict1 = {}
        dict2 = {}
        print("arg = ", arg)
        print("self.dl = ", self.dl)
        if isinstance(arg, DictList):
            print("Entered DictList")
            pass
        elif type(arg) == dict:
            print("Entered dict")
            for val in self.dl:
                for k,v in val.items():
                    if k in arg.keys():
                        dict1[k] = v
                        dict2[arg[k]] = arg[k]
        else:
            raise TypeError("Argument must be type DictList or dict")
    
        return "DictList{}".format(tuple((dict1,dict2)))
    
    def __radd__(self,arg):
        return self.__radd__(arg)
            
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
