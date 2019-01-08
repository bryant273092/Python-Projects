from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        if args==():
            raise AssertionError ("There are no arguments in the dictionary")
        for i in args:
            if type(i)!=dict:
                raise AssertionError ('DictList.__init__: '+str(i)+' is not a dictionary')
            
        self.dl=list(args)

    def __len__(self):
        count=set()
        for i in self.dl:
            for j in i:
                count.add(j)
        return len(count) 
    
    def __repr__(self):
        dic_str='DictList('
        for i in self.dl:
            dic_str+=str(i)+', '
        return dic_str+')'
    
    def __contains__(self,right):
        keys={j for i in self.dl for j in i}
        return right in keys
                   
    def __getitem__(self, right):   
        keys={j for i in self.dl for j in i}
        if right in keys:
            for i in self.dl[::-1]:
                if right in i:
                    return i[right]
        else:
            raise KeyError (str(right)+' appears in no dictionaries')
            
    def __setitem__(self, index, value):
        keys={j for i in self.dl for j in i}
        if index in keys:
            for i in self.dl[::-1]:
                if index in i:
                    i[index]=value
                    return
        self.dl.append({index:value})    
                           
    def __call__(self,value):
        values=[]
        keys={j for i in self.dl for j in i}
        if value not in keys:
            return []
        else:
            for i in range(len(self.dl)):
                if value in self.dl[i]:
                    values.append((i,self.dl[i][value])) 
            return values
                
    def __iter__(self):
        values=set()
        for i in self.dl[::-1]:
            for j in sorted(i):
                if j not in values:
                    yield(j,i[j])
                    values.add(j)
                    
    def __eq__(self,right):
        self_keys={j for i in self.dl for j in i}  
        if type(right)== DictList:
            if self_keys== {j for i in right.dl for j in i}:
                for i in self_keys:
                    if self[i]!=right[i]:
                        return False
                return True
            else:
                return False
        elif type(right)== dict:
            if self_keys== set(right.keys()):
                for i in self_keys:
                    if self[i]!=right[i]:
                        return False
                return True
            else:
                return False
        else:
            raise TypeError (str(right)+' is not a DictList or a dict')
      
    def __add__(self, right):
        if type(right)!=dict or type(right)!=DictList:
            raise TypeError (str(right)+' has to be either a dict or DictList')      
        elif type(right)==DictList:
            left={}
            rights={}
            for i in self.dl:
                for j in i:
                    left[j]+=i[j]
            for i in right.dl:
                for j in i:
                    rights[j]=i[j]
            return DictList(left+rights)
        elif type(right)==dict:
            left={}
            for i in self.dl:
                for j in i:
                    left[j]+=i[j]
            return DictList(left+right)
                
            

            
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
