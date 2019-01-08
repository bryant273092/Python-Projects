from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self,*args):
        assert args, "not exist"
        self.dl=[]
        for value in args:
            if type(value)!=dict:
                raise AssertionError("not dictionary")
            self.dl.append(value)
    
    
    def __len__(self):
        newlis=[]
        for value in self.dl:
            for v in value:
                if v not in newlis:
                    newlis.append(v)
        return len(newlis)
            
    def __repr__(self):
        return "DictList("+",".join(str(i) for i in self.dl)+")"

    def __contains__(self,key):
        for value in self.dl:
            if key in value:
                return True
        return False
    

    def __getitem__(self,index):
        ret=0
        for value in self.dl:
            if index in value and value[index]>ret:
                ret=value[index]
        if any(index in value for value in self.dl)==False:
            raise KeyError()
        return ret


    def __setitem__(self,index,value):
        if any(index in v for v in self.dl):
            nv=-1
            for i,v in enumerate(self.dl):
                if index in v and i>nv:
                    nv=i
            self.dl[i][index]=value        
                
            '''
            ret=0
            for v in self.dl:
                if index in value and value[index]>ret:
                    ret=value[index]
            for v in self.dl:
                if index in v and v[index]==ret:
                    v[index]=value
            '''
            
        elif any(index in v for v in self.dl)==False:
            self.dl.append({index:value})

   
    def __call__(self,item):
        if any(item in value for value in self.dl)==False:
            return []
        else:
            lis=[]
            for i,v in enumerate(self.dl):
                if item in v:
                    lis.append((i,v[item]))
        return lis

    def __iter__(self):
        newlis=[]
        for dic in self.dl:
            for k,v in sorted(dic.items(), key=lambda x:x[0],reverse=True):
                newlis.append((k,v))
        for i,v in enumerate(newlis): 
            for i1,v1 in enumerate(newlis):
                if v[0]==v1[0] and v[1]!=v1[1]:
                    if v[1]<v1[1]:
                        del newlis[i]
                    if v[1]>v1[1]:
                        del newlis[i1]
        for i in newlis:
            yield newlis


    def __eq__(self,right):
        if type(right)==DictList:
            for i in self.dl:
                if all(value in r for r in right for value in self.dl)==False:
                    return False

                
        elif type(right)==dict:
            for i in self.dl:
                if all(value in right for value in self.dl)==False:
                    return False
                nv=-1
                for value in right:
                    for i,v in enumerate(self.dl):
                        if value in v and i>nv:
                            nv=i
                    if right[value]!=v[value]:
                        return False
        else:
            raise TypeError()
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
