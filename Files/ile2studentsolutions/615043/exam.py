from goody import type_as_str  # Useful in some exceptions

# d0 = dict(a=1,b=2,c=3)
# d1 = dict(c=13,d=14,e=15)

class DictList:
    def __init__(self, *args):
        self.dl = []
        for item in args:
            if type(item) == dict:
                self.dl.append(item)
            else:
                raise AssertionError(".__init__ incorrect data type")
        if len(args) == 0:
            raise AssertionError('No length in the __init__')
    
    def __len__(self):
        key_set= set()
        for dicts in self.dl:
            for keys in dicts:
                key_set.add(keys)                
        return len(key_set)
    
    def __repr__(self):
        repstring= ''
        for items in self.dl:
            repstring+=str(items)
        return 'DictList('+repstring+')'
    
    def __contains__(self,item):
        
        for sources in self.dl:
            return item in sources.keys()
#         print(all(self.dl))
#         for sources in range(len(self.dl)):
#             
#             print(self.dl[sources])
# 
#             return item in self.dl[sources].keys()
        
        
        
    def __getitem__(self, item):
        for sources in self.dl:
            if item in sources:
                return sources[item]
            else:
                
                raise KeyError("Not a valid key")
    
    def __setitem(self,item,value):
        for i in self.dl:
            if item in i.keys():
                i[item] = value
            else:
                i[item] = value
                
                
                
    
    def __call__(self, item):
        a1 = []
        for i,v in enumerate(self.dl[0:]):
            if item in v.keys():
                a1.append((i, v[item]))
            else:
                return []
        return a1
            
         
    def __iter__(self):
        result = []
        for i in self.dl:
            result.append((i, sorted(i.items())))
            
        result.sort()
        for ult,val in result:
            yield val
            
            
#     def __eq__(self, right):
#         if type(right) is DictList:
#             return


            
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
