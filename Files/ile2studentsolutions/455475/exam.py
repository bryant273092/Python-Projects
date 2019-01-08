from goody import type_as_str  # Useful in some exceptions


class DictList:
    def __init__(self,*args):
        self.dl=[]
        assert args!=(),'DictList.__init__:None is not a dictionary'
        for i in args:
            assert type(i) is dict,'DictList.__init__:{name} is not a dictionary'.format(name=i)
            self.dl.append(i)
            
    def __len__(self):
        result=[]
        for i in self.dl:
            for key in i.keys():
                result.append(key)
        return len(set(result))
    
    def __repr__(self):
        content=''
        for i in self.dl:
            content+=str(i)+','
        return "DictList("+content[:-1]+')'
    
    def __contains__(self,value):
        for i in self.dl:
            for key in i.keys():
                if key==value:
                    return True
        return False
                
    def __getitem__(self,value):
        result=None
        for i in self.dl:
            for k,v in i.items():
                if k==value:
                    if result==None:
                        result=v
                    elif v>=result:
                        result=v
        if result==None:
            raise KeyError('Not in dictionary')
        return result
    
    def __setitem__(self,key,value):
        index=0
        content=None
        for i in range(len(self.dl)):
            for k,v in self.dl[i].items():
                if k==key:
                    if content==None:
                        content=v
                        index=i
                    elif v>content:
                        content=v
                        index=i
        if content!=None:
            self.dl[index][key]=value
        else:
            self.dl.append({key:value})
                    
        
    def __call__(self,name):
        result=[]
        for i in range(len(self.dl)):
            for k,v in self.dl[i].items():
                if k==name:
                    result.append((i,v))
        return result
    
    def __iter__(self):
        def delesmall(key,alist):
            deadlist=[]
            for i in range(len(alist)):
                for k,v in alist[i].items():
                    if key==k:
                        deadlist.append((v,i))
            deadlist=sorted(deadlist)
            deadlist.pop(-1)
            for i in deadlist:
                alist[i[1]].pop(key)
    
        tem=self.dl.copy()
        all_key=[]
        for i in tem:
            for k in i.keys():
                all_key.append(k)
        for i in set(all_key):
            delesmall(i,tem)
        final=[]
        count=-1
        while abs(count)<=len(tem):
            for k,v in sorted(list(tem[count].items())):
                final.append((k,v))
            count-=1
        for i in final:
            yield i
                
    def __eq__(self,other):
        if type(other) is not dict and type(other) is not DictList:
            raise TypeError('Type not supported')
        my=[]
        your=[]
        for i in self.dl:
            for key in i.keys():
                my.append(key)
        if type(other) is DictList:
            for i in other.dl:
                for key in i.keys():
                    your.append(key)
        elif type(other) is dict:
            for i in other.keys():
                your.append(i)
        if set(my)!=set(your):
            return False
        for i in my:
            if self[i]!=other[i]:
                return False
        return True
                
    def __add__(self,other):
        if type(other) is not dict and type(other) is not DictList:
            raise TypeError('Type not supported')  
        if type(other) is dict:
            codde='DictList('
            for i in self.dl:
                codde+=str(i)+','
            return eval(codde+str(other)+',)')
        
    def __radd__(self,other):
        if type(other) is not dict and type(other) is not DictList:
            raise TypeError('Type not supported')  
        if type(other) is dict:
            codde='DictList('+str(other)+','
            for i in self.dl:
                codde+=str(i)+','
            return eval(codde[:-1]+')')        
             
        

            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    d2 = DictList(dict(a='one',b='two'), dict(b='twelve',c='thirteen'))
    adict = dict(a='one',b='two')
    c=d1+adict
    print(c)
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
    driver.default_show_exception=True
    driver.default_show_exception_message=True
    driver.default_show_traceback=True
    driver.driver()
    