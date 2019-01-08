from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        if args==():
            raise AssertionError('DictList cannot be empty')
        self.dl=[]
        for x in args:
            if type(x)!=dict:
                raise AssertionError(str(x)+'is not a dictionary')
            else:
                self.dl.append(x)

    def __len__(self):
        count=[]
        for x in self.dl:
            for y in x:
                if y not in count:
                    count.append(y)
        return len(count)
   
    def __repr__(self):
        st=''
        for x in self.dl:
            st+=str(x)+', '
        return 'DictList('+st[:-2]+')' 
    
    def __contains__(self,arg):
        for x in self.dl:
            for y in x:
                if str(arg) in y:
                    return True
        return False
    
    def __getitem__(self,a):
        count=len(self.dl)-1
        while count>-1:
            if a in self.dl[count]:
                return self.dl[count][a]
            count-=1
        raise KeyError('item not in DictList')
    
    def __setitem__(self,a,v):
        count=len(self.dl)-1
        inside=False
        while count>-1:
            if a in self.dl[count]:
                self.dl[count][a]=v
                inside=True
                break
            count-=1
        if not inside:
            self.dl.append({a:v})
        
    def __call__(self,v):
        result=[]
        count=0
        while count<len(self.dl):
            if v in self.dl[count]:
                result.append((count,self.dl[count][v]))
            count+=1
        return result
    
    def __iter__(self):
        count=len(self.dl)-1
        result=[]
        while count>-1:
            for x in sorted(self.dl[count].items()):
                add=True
                for n in result:
                    if n[0]==x[0]:
                        add=False
                if add:    
                    result.append(x)
            count-=1
        return iter(result)
    
        
    def __eq__(self,right):
        if type(right)==DictList:
            if len(self)==len(right):    
                for x in self.dl:
                    for y in x:
                        try:
                            if self.__getitem__(y)!=right.__getitem__(y):
                                return False
                        except:
                            return False
                return True
            return False
        elif type(right)==dict:
            if len(self)==len(right):    
                for x in self.dl:
                    for y in x:
                        if y not in right or self.__getitem__(y)!=right[y]:
                                return False
                return True
            return False
        raise TypeError('values are not comparable')
                     
    def __add__(self,right):
        if type(right)==DictList:
            temp1={}
            temp2={}
            for x in self.dl:
                for y in x:
                    if y not in temp1:
                        temp1[y]=self.__getitem__(y)
            for m in right:
                for n in m:
                    if n not in temp2:
                        try:
                            temp2[n]=right.__getitem__(n)
                        except:
                            pass
            return DictList(temp1,temp2)       
        elif type(right)==dict:
            temp3={}
            for x in self.dl:
                for y in x:
                    if y not in temp3:
                        temp3[y]=self.__getitem__(y)
            return DictList(temp3,right.copy())
        raise TypeError('values cannot be added')
    
    def __radd__(self,left):
        if type(left)==dict:
            temp3={}
            for x in self.dl:
                for y in x:
                    temp3[y]=self.__getitem__(y)
            return DictList(left.copy(),temp3)
        raise TypeError('values cannot be added')
        
        
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
