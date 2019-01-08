from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*dicts):
        self.dl=[]
        if dicts ==():
            raise AssertionError
        for i in dicts:
            assert type(i) is dict,"the argument is expected to be a dictionary"
            self.dl.append(i)
    def __len__(self):
        emplist=[]
        for i in self.dl:
            for j in i.keys():
                emplist.append(j)
        return len(set(emplist))
    def __repr__(self):
        
        result=""
        result+= "("
        for i in self:
            result+= str(i)
            result+= ","
        return result
    def __contains__(self,keytofind):
        empty=[]
        for i in self.dl:
            for j in i.keys():
                empty.append(j)
        if keytofind in empty:
            return True
        else:
            return False
    def __getitem__(self,valuetofind):
        empty=[]
        for i in self.dl:
            for j in i.keys():
                empty.append(j)
        result=int
        for i in self.dl:
            for j in i.keys():
                if j==valuetofind:
                    result= i[j]
                if valuetofind not in empty:
                    raise KeyError
        return result
    def __setitem__(self,key,value):
        empty=[]
        emptydict={}
        dict2={}
        for i in self.dl:
            for j in i.keys():
                empty.append(j)
        if key not in empty:
            emptydict[key]=int
            emptydict[key]=value
            self.dl.append(emptydict)
        if key in empty:
            for i in self.dl:
                if key in i.keys():
                    pass
    def __call__(self,thing_to_call):
        empty=[]
        item=int
        result =[]
        result2 =[]
        t=()
        kens=0
        for i in self.dl:
            item=0
            for k,v in i.items():
                item=0
                for n in range(len(i)):
                    kens+=1
                    result.append( (n, v))
        for i in result:
            if thing_to_call== i[1]:
                result2.append((i[0],i[2]))
    
        for i in self.dl:
            for j in i.keys():
                empty.append(j)
        if thing_to_call not in empty:
            return []
        else:
            return result
    def __iter__(self):
        result2=[]
        for i in self.dl:
            for j,k in i.items():
                result2.append((j,k))
        for i in result2:
            yield i
    def equal(self,dict1):
        if type(dict1) is int or list:
            raise TypeError
        empty=[]
        empty2=[]
        for i in self:
            for j in i.keys():
                empty.append(j)
        if empty==empty2:
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
