from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self,*args):
        self.dl = []
        for i in args:
            if type(i) is dict:
                self.dl.append(i)
            else:
                raise AssertionError("DictList.__init__: "+str(i)+" is not a dictionary.")
        if len(args) == 0:
            raise AssertionError()
    
    def __len__(self):
        count = 0
        d_keys = set()
        for i in self.dl:
            for j in i:
                if j not in d_keys:
                    count += 1
                d_keys.add(j)
        return count
    
    def __repr__(self):
        dls = "DictList("
        for i in self.dl:
            dls += str(i)+","
        dls = dls[:-1]
        dls += ")"
        return dls
    def __contains__(self,item):
        for i in self.dl:
            if item in i:
                return True
        return False
    def __getitem__(self,item):
        self.dl.reverse()
        for i in self.dl:
            for j,k in i.items():
                if item == j:
                    self.dl.reverse()
                    return k
        else:
            raise KeyError(str(item)+" appears in no dictionaries.")
    
    def __setitem__(self,key,value):
        if self.__contains__(key):
            self.dl.reverse()
            for i in self.dl:
                if key in i:
                    i[key] = value
                    self.dl.reverse()
                    break
        else:
            self.dl.append({key:value})            
            
    def __call__(self,item):
        iv = []
        for i in range(len(self.dl)):
            if item in self.dl[i]:
                iv.append((i,self.dl[i][item]))
        return iv
    
    def __iter__(self):
        d_list = []
        yl = []
        self.dl.reverse()
        for i in self.dl:
            for key,value in sorted(i.items(), key=lambda x: x[0]):
                if key not in d_list:
                    d_list.append(key)
                    yl.append((key,value))
        for k in yl:
            yield k
            
    def __eq__(self,right):
        if type(right) is DictList:
            for i in self.dl:
                for j in i:
                    if not right.__contains__(j) or self.__getitem__(j) != right.__getitem__(j):
                        return False
            return True
        
        elif type(right) is dict:
            for i in self.dl:
                for j in i:
                    if j not in right.keys() or self.__getitem__(j) != right[j]:
                        return False
            return True
                
        else:
            raise TypeError("Wrong Type.")
        
                
            
        
            
            



            
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
