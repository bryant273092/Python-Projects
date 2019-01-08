from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl = []
        if len(args) == 0:
            raise AssertionError(f'{args} is empty')
        for i in args:
            if isinstance(i,dict) == False:
                raise AssertionError(f'{i} is not a dictionary')
            else:
                self.dl.append(i)
#         print(self.dl)       
    def __len__(self):
        return len(set([j for i in self.dl for j in i]))
    
    def __repr__(self):
        return 'DictList({})'.format(','.join([f'{i}' for i in self.dl]))
    
    def __contains__(self, item):
        for i in self.dl:
            for j in i:
                if j == item:
                    return True
        return False
    
    def __getitem__(self,item):
        temp = []
        for d in self.dl:
            if item in d.keys():
                temp.append(d[item])
        if len(temp) == 0:
            raise KeyError(f'{item} appears in no dictionary')
        else:
            return temp[-1]
    
    def __setitem__(self,name,value):
        temp = []
        for i, d in enumerate(self.dl):
            if name in d.keys():
                temp.append((i,d))
        
        
        if len(temp) == 0:
            self.dl.append({name:value})
        else:
            index = temp[-1][0]
#         print(index,name)
            self.dl[index][name] = value
                
    def __call__(self,name):
        temp = []
        for i, d in enumerate(self.dl):
            if name in d.keys():
                temp.append((i,d[name]))
        return temp
    
    def __iter__(self):
        temp = []
        final = []
        dup = False
#         for d in self.dl:
#             for k in d:
#                 temp.append((k,self[k]))
#             l = sorted(temp,key = lambda x: x[0][0])
#             final.extend(l)
#             l = []
        for d in reversed(self.dl):
            for k in d: 
                if len(temp) == 0:
                    temp.append((k,d[k]))
                for tuples in temp:
                    if tuples[0] != k:
                        dup = False
                    else: dup = True
                if dup == False:
                    temp.append((k,d[k]))
            dup = False
            temp = sorted(temp, key = lambda x: x[0][0])
#             print(temp)
            for i in temp:
                if len(final) != 0:
                    for k in final:
                        if k[0] == i[0]:
                            dup = True
                    if dup != True:
                        final.append(i)
                    dup = False
                else:
                    final.append(i)
                    
                            
            temp = [] 
        for i in final:
            yield i
                 
            
            
    def __eq__(self,right):
        if type(right) not in [DictList,dict]:
            raise TypeError(f'{right} is neither a DictList or a dict')
        if type(right) == DictList:
            for d in self.dl:
                for k in d:
                    if k in right:
                    
                        if self[k] != right[k]:
                            return False
                    else:
                        return False
            return True
        
        if type(right) == dict:
            for d in self.dl:
                for k in d:
                    if k in right.keys():
                        if self[k] != right[k]:
                            return False
                    else:
                        return False
                return True
            
            
            
            
    ###### EXTRA CREDIT

        
        
            
                
                
                
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d0 = dict(a=1,b=2,c=3)
    d1 = dict(c=13,d=14,e=15)
    d2 = dict(e=25,f=26,g=27)
    d = DictList(d0,d1,d2)
    
#     print(d['a'])
#     d['b'] = 'new1'
#     for i in d:
#         print(i)
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
