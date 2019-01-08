from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl=[]
        assert len(args)!=0
        for i in args:
            assert type(i)==dict
            self.dl.append(i)


       
    def __len__(self):
        set1=set()
        count=0
        for i in self.dl:
            for k in i.keys():
                if k not in set1:
                    count+=1
                    set1.update(k)
        del set1
        return count
                
    def __repr__(self):
        return "DictList"+str(tuple(self.dl))+""
        
                               
    def __contains__(self,key1):
        for i in self.dl:
            for k in i.keys():
                if k==key1:
                    return True
        return False      
    def __getitem__(self,item):
        find=None
        for i in self.dl:
            for k,v in i.items():
                if k==item:
                    find=v
        if find==None:
            raise KeyError
        else:
            return find
        
    def __setitem__(self,item,value):
        find=None
        loc=None
        for i in range(len(self.dl)):
            for k,v in self.dl[i].items():
                if item==k:
                    find=v
                    loc=i
        if find==None:
            self.dl.append({item:value})
        else:
            self.dl[loc][item]=value

    def __call__(self,key):
        list1=[]
        for i in range(len(self.dl)):
            for k,v in self.dl[i].items():
                if k==key:
                    list1.append((i,v))
        return list1
    
    
    def __iter__(self):
        set1=[]
        set2=set()
        x=reversed(self.dl)
        
        for i in range(len(self.dl)):
            for k,v in sorted(next(x).items()):
                if k not in set2:
                    set2.add(k)
                    set1.append((k,v))

        for j in set1:
            yield j
    
    
    def __eq__(self,other):
        if type(other)==DictList or type(other)==dict:
            for i in range(len(self.dl)):
                for k in self.dl[i].keys():
                    if k in other:
                        if self[k]!=other[k]:
                            return False
                        else:
                            pass
                        
                    else:
                        return False
                   
            return True
        else:
            raise TypeError
    
    def __add__(self,other):
        
        
        def steady(dlist):
            setish=set()
            listish={}
            for i in dlist:
                for k,v in i.items():
                    if k in listish.keys():
                        if listish[k]<v:
                            listish[k]=v

                    else: 
                        listish.update({k:v})
            return listish
        
        if type(other) is dict and type(self) is DictList:
            return DictList(steady(self.dl),steady(DictList(other).dl))
        elif type(self) is dict and type(other) is DictList:
            return DictList(steady(DictList(self).dl),steady(other.dl))
        elif type(self) is DictList and type(other) is DictList:
            return DictList(steady(self.dl),steady(other.dl))
        else: 
            raise TypeError
        
    


            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d0= dict(a=1,b=2,c=3)
    d1 = dict(c=13,d=14,e=15)
    d  = DictList(d0,d1)

    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
