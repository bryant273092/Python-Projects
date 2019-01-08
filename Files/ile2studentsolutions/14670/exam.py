from goody import type_as_str  # Useful in some exceptions
from audioop import reverse

class DictList:
    def __init__(self,*arg):
        self.dl=[]
        if arg==[]:
            raise AssertionError
        for i in arg:
                if type(i) is not dict:
                    raise AssertionError
                else:
                    self.dl.append(i)
        
    def __len__(self):
        lenth=[]
        for i in self.dl:
            for x in i.keys():
                if x not in lenth:
                    lenth.append(x)
        return len(lenth)
    
    def __repr__(self):
        return "DictList{x}".format(x=tuple(self.dl))
    
    def __contains__(self,item):
        for i in self.dl:
            if item in i.keys():
                return True
        return False
    def __getitem__(self,item):
        items=[]
        for i in self.dl:
            if item in i.keys():
                items.append(i[item])
        if items==[]:
            raise KeyError
        else:
            return items[-1]
    
    def __setitem__(self,item,value):
        items=[]
        for i in range(len(self.dl)):
            if item in self.dl[i].keys():
                items.append(i)
        if items!=[]:   
            self.dl[items[-1]][item]=value
        else:    
            self.dl.append({item:value})
        
    def __call__(self,item):
        items=[]
        for i in range(len(self.dl)):
            if item in self.dl[i].keys():
                items.append((i,self.dl[i][item]))
        return items
            
    def __iter__(self):
        items=[]
        for i in range(len(self.dl)):
            item_list=[]
            for item in self.dl[i].keys():
                value=self.__call__(item)
                if value[-1][0]==i:
                    item_list.append((item,value[-1][1]))
            items.append(sorted(item_list,key=lambda x:x[0]))
        
        for i in sorted(items,reverse=True):
            for x in i:
                yield x                  
    
    def __eq__(self,right):
        
        if type(right) is type(DictList()):
            for i in range(len(right.dl)):
                for k in right.dl[i].keys():
                    if self.__contains__(k):
                            if right.dl[i][k] not in[y[1] for y in self.__call__(k)]:
                                return False
                    else:
                        return False
            return True
       
        elif type(right) is dict:
            for k in right.keys():
                if self.__contains__(k):
                        if right[k]!= self.__call__(k)[-1][1]:
                            return False
                else:
                    return False
            return True
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
