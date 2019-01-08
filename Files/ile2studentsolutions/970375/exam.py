from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        
        assert len(args) != 0, 'DictList.__init__: empty parameter is not a dictionary'
        for arg in args:
            assert type(arg) == dict,'DictList.__init__:'+str(arg)+'is not a dictionary'
            
        self.dl = [a for a in args]
        
    def __len__(self):
        
        reached = set() 
        for d in self.dl:
            for k in d.keys():
                reached.add(k) 
        return len(reached)
        
    def __repr__(self):
        return 'DictList('+ ','.join(str(d) for d in self.dl) + ')'
    
    def __contains__(self,key):
        for d in self.dl:
            for k in d.keys():
                if key == k:
                    return True 
        return False
    
    def __getitem__(self,i):
        
        output = None 
        for d in self.dl:
            for k in d.keys():
                if k == i :
                    output = d[i]
        if output == None:
            raise KeyError ('invalid key')
        return output
    
    def __setitem__(self,key,value):
        index = None
        for n in range(len(self.dl)):
            for k in self.dl[n].keys():
                if k == key:
                    index = n 
                    
        if index == None:
            try:
                newd = {}
                newd[key] = value
                self.dl.append(newd)
            except:
                print('error block 1') 
        else:
            try:
                self.dl[index][key] = value
            except:
                print('error block 2')
                
    def __call__(self,item):
        output = []
        for n in range(len(self.dl)):
            for k in self.dl[n].keys():
                if k == item:
                    output.append((n,self.dl[n][k]))
                #print(output,n,self.dl)
        return output
    
    def __iter__(self):
        def reverse(l):
            output = []
            marker = len(l)-1 
            while not marker < 0:
                output.append(l[marker])
                marker -= 1 
            return output 
        reached = set() 
        for d in reverse(self.dl):
            for k in d.keys():
                if not k in reached:
                    reached.add(k)
                    yield (k, d[k])
                    
    def __eq__(self,r):
        def dlkeys(dl):
            output = set() 
            for d in dl:
                for k in d.keys():
                    output.add(k)
            return output
        
        if type(r) == type(self):
            for d in r.dl:
                for k in d.keys():
                    if not k in self:
                        return False 
                    if not r[k] == self[k]:
                        return False 
            return True 
        elif type(r) == dict:
            if not set(r.keys()) == dlkeys(self.dl):
                return False
            for k in r.keys():
                if not k in self:
                    return False
                if not r[k] == self[k]:
                    return False
            return True 
        else:
            raise TypeError('DictList.__eq__, your parameter is neither a dict not DictList')
        
    def __add__(self,r):
        def dlkeys(dl):
            output = set()
            for d in dl:
                for k in d.keys():
                    output.add(k)
            return output
        if type(r) == type(self):
            di0 = {}
            di1 = {} 
            for k in dlkeys(self.dl):
                di0[k] = self[k]
            for k in dlkeys(r.dl):
                di1[k] = r[k]
            new = DictList(di0,di1)
            return new 
        elif type(r) == dict:
            rdict = str(r)
            new = 'DictList('+ ','.join(str(d) for d in self.dl) +','+rdict+ ')'
            return eval(new) 
        else:
            raise TypeError ('operand failed, parameter type neither dict nor DictList in DictList.__add__')
        
            
    def __radd__(self,l):
        
        if type(l) == type(self):
            return l.__add__(self)
        
        elif type(l) == dict:
            new = 'DictList('+ str(l) +','+ ','.join(str(d) for d in self.dl) +')'
            return eval(new) 
        else:
            raise TypeError('operand failed, parameter type neither dict nor DictList in DictList.__radd__')
                             
            
        
        
                
            
            
                
        
                
        
        



            
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
