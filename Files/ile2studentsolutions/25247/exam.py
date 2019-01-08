from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self,*d):
        self.dl = []
        if len(d) == 0:
            raise AssertionError('DictList.__init__:'+"'"+str(d)+"' can not be empty")
        for i in d:
            assert type(i) is dict, 'DictList.__init__:'+"'"+str(i)+"' is not dictionary"
            self.dl.append(i)
    
    def __len__(self):
        l = set()
        for i in self.dl:
            for v in i:
                l.add(v)
        return len(l)

    def __repr__(self):
        return 'DictList('+','.join(str(i) for i in self.dl)+')'
    
    def __contains__(self,item):
        if type(item) is not str:
            return False
        for i in self.dl:
            for k in i:
                if item in k:
                    return True
        return False
    
    def __getitem__(self,key):
        for i in self.dl[::-1]:
            if key in i:
                return i[key]
        raise KeyError
    
    def __setitem__(self,key,value):

        a = False
        for i in self.dl[::-1]:
            if key in i:
                a = True
                i[key] = value
                break
        if a ==False:
            self.dl.append({key:value})        

    def __call__(self,item):
        result = []
        num = 0
        for i in self.dl:
            num +=1
            if item in i:
                result.append((num-1,i[item]))
        return result        
     
    @staticmethod
    def _gen(object):
        check = list()
        for i in object[::-1]:
            for k,v in i.items():
                if k not in check:
                    yield (k,v)  
                    check.append(k) 
                     
    def __iter__(self):   
        return DictList._gen(self.dl)
    
    def __eq__(self,right):
        if type(right) == type(self) or type(right) is dict:
            check = set()
            for i in self.dl:
                for k in i:
                    check.add(k)
            if type(right) == type(self):
                right_check = set()
                for i in right.dl:
                    for k in i:
                        right_check.add(k)
                if check != right_check:
                    return False
                else:
                    return all( self.__getitem__(i) == right.__getitem__(i) for i in check)
            else:
                right_check = set()
                for i in right:
                    right_check.add(i)
                if check != right_check:
                    return False
                else:                
                    return all( self.__getitem__(i) == right[i] for i in check)
        else:
            raise TypeError('The operand "==" not support '+type_as_str(self)[5:]+' with ' +type_as_str(right))    
        
    def __add__(self,right):
       
        if type(right) == type(self):
            first = dict()
            for i in self.dl:
                for k in i:
                    if k not in first:
                        first[k] = self.__getitem__(k)
            second = dict()
            for i in right.dl:
                for k in i:
                    if k not in second:
                        second[k] = right.__getitem__(k)
            return DictList(first,second)
        elif type(right) is dict:
            first = self.dl.copy()
            second = right.copy()
            return DictList(*first,second)
        else:
            raise TypeError('The operand "+" not support '+type_as_str(self)[5:]+' with ' +type_as_str(right))   
        
    def __radd__(self,left):    
        if type(left) == type(self): 
            return self.__add__(left)
        elif type(left) is dict:
            second = self.dl.copy()
            first = left.copy()
            return DictList(first,*second)
        else:
            raise TypeError('The operand "+" not support '+type_as_str(left)+' with ' + type_as_str(self)[5:]) 
        
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
