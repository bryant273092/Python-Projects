from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl = []
        if type(args) == None or len(args) == 0:
            raise AssertionError
        for i in args:
            if type(i) == dict:
                self.dl.append(i)
            else:
                raise AssertionError
    
    def __len__(self):
        result = set()
        for dic in self.dl:
            for i in dic.keys():
                result.add(i)
        return len(result)
    
    def __repr__(self):
        return ("DictList({})".format(",".join([str(i) for i in self.dl])))
    
    def __contains__(self,dest):
        for i in self.dl:
            if dest in i.keys():
                return True
        return False
    
    def __getitem__(self,value):
        for i in range(len(self.dl)):
            if value in self.dl[-1 - i].keys():
                return self.dl[-1 - i][value]
        raise KeyError
    
    def __setitem__(self,item,value):
        if self.__contains__(item):
            for i in range(len(self.dl)):
                if item in self.dl[-1 - i].keys():
                    self.dl[-1 - i][item] = value
                    break
                    
                    
        else:
            self.dl.append({item:value})
            
    def __call__(self, value):
        result = []
        if self.__contains__(value):
            for i in range(len(self.dl)):
                if value in self.dl[i].keys():
                    result.append((i,self.dl[i][value]))
            return result
        else:
            return []
        
    def __iter__(self):
        key = set()
        for i in range(len(self.dl)):
            for x in sorted(self.dl[-1 - i].keys()):
                if x not in key:
                    yield (x, self.dl[-1 - i][x])
                key.add(x)
                
    def __eq__(self,right):
        skey = set()
        fkey = set()
        first = False
        second = False
        
        for i in self.dl:
            for x in i.keys():
                fkey.add(x)
        
        
        if type(right) == DictList:
            for i in right.dl:
                for x in i.keys():
                    skey.add(x)
            first = all(self.__contains__(i) for i in skey)
            third = all(right.__contains__(i) for i in fkey)
            second = all(self.__getitem__(i) == self.__getitem__(i) for i in skey)
            fourth = all(right.__getitem__(i) == self.__getitem__(i) for i in fkey)
            
        elif type(right) == dict:
            first = all(self.__contains__(i) for i in right)
            third = all(i in right for i in fkey)
            if first:
                second = all(self.__getitem__(i) == right[i] for i in right)
                fourth = all(self.__getitem__(i) == right[i] for i in right)
                
        else:
            raise TypeError
            
        if first and second and third and fourth:
            return True
        else:
            return False
    
    
    def __add__(self,right):
        resulto = dict()
        resultt = dict()
        
        if type(right) == DictList:
            for i in self.dl:
                for x in i:
                    resulto[x] = self.__getitem__(x)
            
            for i in right.dl:
                for x in i:
                    resultt[x] = right.__getitem__(x)
            return DictList(resulto,resultt)
        
        elif type(right) == dict:
            return eval("DictList({},{})".format(",".join(str(i) for i in self.dl), right))
        else:
            raise TypeError
        
    def __radd__(self,left):
        resulto = dict()
        resultt = dict()
        if type(left) == DictList:
            for i in self.dl:
                for x in i:
                    resulto[x] = self.__getitem__(x)
            
            for i in right.dl:
                for x in i:
                    resultt[x] = left.__getitem__(x)
            return DictList(resulto,resultt)
        
        
        elif type(left) == dict:
            return eval("DictList({},{})".format(left, ",".join(str(i) for i in self.dl)))
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
