from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self,*args):

        self.dl=[]
        if args!=None and type(arg for arg in args)!=dict:
            for arg in args:
                if type(arg)==dict:
                    for k in arg.keys():
                        self.dl.append((k,arg[k]))
                else:
                    raise AssertionError('DictList.__init: {} not a dictionary')
        elif args==None:
            raise AssertionError('DictList.__init: {} not a dictionary')
        else:
            raise AssertionError('DictList.__init: {} not a dictionary')
        
    '''
    def def __init__(self,*args):
        self.dl=[]
        if args!=None and type(arg for arg in args)!=dict:
            for arg in args:
                if type(arg)==dict:
                    for k in arg.keys():
                        self.dl.append(dict(k=arg[k]))
                else:
                    raise AssertionError('DictList.__init: {} not a dictionary')
        elif self.args==None:
            raise AssertionError('DictList.__init: {} not a dictionary')
        else:
            raise AssertionError('DictList.__init: {} not a dictionary')
        
    
    def __len__(self):
        result=set()
        count=0
        for d in self.dl:
            for key in d.keys():
                result.add(key)
        for i in result:
            count+=1
        return count
                
    
    def __repr__(self):
        x=type_as_str(d for d in self.dl)
        return 'DictList('+','.join(x)+')'
    
    def __contains__(self,arg):
        result=[]
        for d in self.dl:
            result.append(d.keys())
        return arg in result
    
    def __getitem__(self,key):
        v=None
    '''
        
 
    def __len__(self):
        lst=set()
        for d in self.dl:
            if d[0] not in lst:
                lst.add(d[0])
        count=0
        for i in lst:
            count+=1
        return count
    
    def __repr__(self):
        result=dict()
        for d in self.dl:
            result.update({d[0]:d[1]})
        return 'DictList('+str(result)+')'
    
    def __contains__(self,arg):
        return arg in [d[0] for d in self.dl]
    
    def __getitem__(self,key):
        v=None
        if key in [d[0] for d in self.dl]:
            for x,y in self.dl:
                if key==x:
                    v=y
            return v
        else:
            raise KeyError('no key')
        
    def __setitem__(self,k,v):
        check=[]
        count=0
        if k in [d[0] for d in self.dl]:
            pass
            '''
            for d in self.dl:
                if d[0] not in check:
                    check.append(d[0])
                    count+=0
                else:
                    count+=1
            for d in self.dl:
                if d[0]==k and count>=1:
                    d[1]=v 
                elif d[0]==k and count==0:
                    d[1]=v 
                else:
                    self.dl.append((k,'new'))
            '''
        else:
            self.dl.append((k,'new'))
            

            
    def __call__(self,k):
        result=[]
        count=0
        if k in [d[0] for d in self.dl]:
            for d in self.dl:
                count+=1
                if d[0]==key:
                    result.append((count//3,d[1]))
                elif 'new' in d[1]:
                    return []
            return result
        else:
            return []
        
    def __iter__(self):
        for d in self.dl:
            yield (d[0],d(1))
    
        

        
        




            
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
