from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl=[]
#         assert len(self.dl)>=1 and type(self.dl) is list
#         assert len(args)>=1
#         assert [type(i)is dict for i in args]

        for a in args:
            #print(a)
            #assert type(args) is dict 
            self.dl.append(a)
            #print(self.dl)
            assert type(a) is dict and len(a)>=1
            assert len(self.dl)>=1 and type(self.dl) is list
        assert len(self.dl)>=1
            
        
            
        
    
            
        
        
    def __len__(self):
        #print(self.dl)
        t=set()
        for i in self.dl:
            for k,v in i.items():
                if k not in t:
                    t.update(k)
        return len(t)
    def __repr__(self):
        return 'DictList('+",".join([str(i) for i in self.dl])+")"
    def __contains__(self,k):
        for i in self.dl:
            #print(i)
            for key in i:
                if key==k:
                    return True
                
        return False
    def __getitem__(self,k):
        for i in self.dl[::-1]:
            #print(i)
            #for key in i:
                #print(key)
            if k in i:
                try:
                    return i[k]
                except:
                    raise KeyError
                return k
        raise KeyError
    def __setitem__(self,k,v):
        d={}
        for i in self.dl:
            count=0
            if k in i:
                i[k]=v
            else:
                i[k]=v
                count+=1
  
    def __call__(self,k):
        #print(k)
        
        for i in self.dl:
            
            if k in i:
                
                for num, it in enumerate(i):
                    l=[]
                    
                    l.append((num,i[k]))
                    return l
                
                
    def __iter__(self):
        t={}
        for i in self.dl[::-1]:
            for item in sorted(i, key=lambda x:x[0]):
                #print(item)
                if item not in t:
                    t.update(item)
                    print(t)
    def __eq__(self,right):
        #print(self.keys())
        if type(self)==DictList and type(right)==DictList:
            if self.dl==right.dl:
                return True
        if type(self)==DictList:
            if self.dl==right:
                return True
    def __neq__(self,right):
        return right==self

                    
            
            
                
            
            
            




            
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
