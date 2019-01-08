from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl=[]
        assert len(args)!=0, 'no argument given'
        for arg in args:
            assert type(arg)==dict,str(arg)+' is not a dictionary'
            self.dl.append(arg)
            
    def __len__(self):
        temp=set()
        for i in self.dl:
            for k in i.keys():
                temp.add(k)
        return len(temp)
    
    def __repr__(self):
        temp=tuple(i for i in self.dl)
        return 'DictList'+str(temp)
    
    def __contains__(self, arg):
        for i in self.dl:
            for k in i.keys():
                if arg==k:
                    return True
        return False
    
    def __getitem__(self, k):
        test=False
        for i in reversed(self.dl):
            if k in i.keys():
                test=True
                return i[k]
        if test==False:
            raise KeyError
        
    def __setitem__(self, key, value):
        for i in reversed(self.dl):
            if key in i.keys():
                i[key]=value
                break
        test=False
        for i in self.dl:
            if key in i.keys():
                test=True
        if test==False:
            new=dict()
            new[key]=value
            self.dl.append(new)
        
    def __call__(self, arg):
        result=[]
        for i,j in enumerate(self.dl, 0):
            for k,v in j.items():
                if arg==k:
                    result.append((i,v))
        return result
        
    def __iter__(self):
        temp=set()
        for i in reversed(self.dl):
            for k,v in i.items():
                if not k in temp:
                    yield(k,v)
                    temp.add(k)
                    
    def __eq__(self, other):
        if type(other)==DictList:
            key1=set()
            key2=set()
            for i in self.dl:
                for k in i.keys():
                    key1.add(k)
            for j in other.dl:
                for key in j.keys():
                    key2.add(key)
            if key1==key2:
                for n in key1:
                    if self.__getitem__(n)!=other.__getitem__(n):
                        return False
                return True     
            else:
                return False
        elif type(other)==dict:
            key1=set()
            key2=other.keys()
            for i in self.dl:
                for k in i.keys():
                    key1.add(k)
            if key1==key2:
                for n in key1:
                    if self.__getitem__(n)!=other[n]:
                        return False
                return True   
            else:
                return False
        else:
            raise TypeError

    def __add__(self, other):
        if type(other)==DictList:
            new1=dict()
            new2=dict()
            for i in reversed(self.dl):
                for k,v in i.items():
                    if not k in new1.keys():
                        new1[k]=v 
            for j in reversed(other.dl):
                for key,val in j.items():
                    if not key in new2.keys():
                        new2[key]=val
            return DictList(new1,new2)     
        elif type(other)==dict:
            copyD=[i for i in self.dl]
            copyO=dict()
            for i,j in other.items():
                copyO[i]=j
            return DictList(*(i for i in copyD), copyO)
        else:
            raise TypeError
        
    def __radd__(self, other):
        if type(other)==DictList:
            new1=dict()
            new2=dict()
            for i in reversed(self.dl):
                for k,v in i.items():
                    if not k in new1.keys():
                        new1[k]=v 
            for j in reversed(other.dl):
                for key,val in j.items():
                    if not key in new2.keys():
                        new2[key]=val
            return DictList(new1,new2)     
        elif type(other)==dict:
            copyD=[i for i in self.dl]
            copyO=dict()
            for i,j in other.items():
                copyO[i]=j
            return DictList(copyO, *(i for i in copyD))
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
