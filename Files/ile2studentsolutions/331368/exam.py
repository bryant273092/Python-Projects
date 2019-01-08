from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl=[]
        if args==():
            raise AssertionError("DictList.__init__:is not a dictionary")
        for x in args:
            if type(x)!=dict:
                raise AssertionError("DictList.__init__:"+"'"+str(x)+"'"+"is not a dictionary")
            else:
                self.dl.append(x)
    
    def __len__(self):
        result=[]
        for x in self.dl:
            for y in x.keys():
                if y not in result:
                    result.append(y)
        return len(result)
    

    def __repr__(self):
        result="DictList("
        for x in self.dl:
            result+=str(x)+","
        result+=")"
        return result
    
    
    def __contains__(self,item):
        result=[]
        for x in self.dl:
            for y in x.keys():
                result.append(y)
        if item in result:
            return True
        else:
            return False 
            
            
    def __getitem__(self,item):
        result=[]
        for x in self.dl:
            if item in x.keys():
                result.append(x[item])
        if result==[]:
            raise KeyError
        return result[-1]
    
    def __setitem__(self,item,value):
        result=[]
        for x in range(len(self.dl)):
            if item in self.dl[x].keys():
                result.append(x)
        if result==[]:
            self.dl.append({item:value})
        else:
            self.dl[result[-1]][item]=value
                
    
    def __call__(self,item):
        result=[]
        for x in range(len(self.dl)):
            if item in self.dl[x].keys():
                result.append((x,self.dl[x][item]))
        return result
                
    
    def __iter__(self):
        result1=[]
        temp=[]
        temp2=[]
        for x in self.dl:
            temp.append([])
            for y in x.keys():
                temp[-1].append((y,x[y]))
        temp.reverse()
        for z in temp:
            for c in z:
                result1.append(c)

        return iter(result1)
        
        
            
                    
    def __eq__(self,right):
        temp1=[]
        temp2=[]
        temp3=[]
        temp4=[]
        if type(right) is DictList:
            if len(self)==len(right):
                for x in self.dl:
                    for y in x.keys():
                        if y not in temp1:
                            temp1.append(y)
                for x in right.dl:
                    for y in x.keys():
                        if y not in temp2:
                            temp2.append(y)
                if temp1==temp2:
                    for z in temp1:
                        temp3.append(self[z])
                        temp4.append(right[z])
                    if temp3==temp4:
                        return True
                    return False
                        
                return False
                        
            else:
                return False
                    
            
            
        elif type(right)==dict:
            result={}
            for x in self.dl:
                for y in x.keys():
                    result[y]=x[y]
            if result==right:
                return True
            return False

            
        else:
            raise TypeError("It's illegall")
            




            
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
