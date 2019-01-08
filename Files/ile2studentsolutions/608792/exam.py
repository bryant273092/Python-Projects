from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *dicts):
        self.dl=[]
        if len(dicts)== 0:
            raise AssertionError()
        for elems in dicts:
            temp ={}
            if type(elems) == dict:
                for k,v in elems.items():
                    temp[k]=v
                self.dl.append(temp)
            else:
                raise AssertionError()
            
    def __len__(self):
        a_set = set({})
        for elems in self.dl:
            for keys in elems:
                a_set.add(keys)
        return len(a_set)
    
    def __repr__(self):          
        x = ''
        for items in self.dl:
            x+= str(items)+ ', '  
        return "DictList(" + x[:-2] +")"
    
    def __contains__(self,item):
        for elems in self.dl:
            if item in elems.keys():
                return True
        else:
            return False
    def __getitem__(self, item):
        for x in range(len(self.dl)):
            if item in self.dl[-x-1]:
                return self.dl[-x-1][item]
        else:
            raise KeyError()
                         
    def __setitem__(self, key, value):
        for x in range(len(self.dl)):
            if key in self.dl[-x-1]:
                self.dl[-x-1][key] = value
        else:
            self.dl.append({key:value})
            
    def __call__(self, item):
        a_list = []
        for x in range(len(self.dl)):
            if item in self.dl[x]:
                a_list.append((x, self.dl[x][item]))
        return a_list
    
    def __iter__(self):
        def gen(dicti):
            for x in range(len(dicti)):
                yield (dicti[-x-1].items([x])[0],dicti[-x-1].items([x])[1])
        return gen(self.dl)

    def __eq__(self, right):
        if type(right) == DictList:
            a_set = set({})
            b_set = set({})
            for items in self.dl:
                for k1 in items:
                    a_set.add(k1)
            for elems in right.dl:
                for k2 in elems:
                    b_set.add(k2)
            return a_set == b_set
        elif type(right) == dict:
            a_set = set({})
            b_set = set({})
            for items in self.dl:
                for k1 in items:
                    a_set.add(k1)
            for items in right.keys():
                b_set.add(items)
            return a_set == b_set
        else:
            raise TypeError()
            
                        
                    
                
                
        
       
            
            
    
            




            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d = DictList({'a': 1, 'b':2 , 'c':3}, {'c': 13, 'd':14, 'e':15})
    print(d.dl)
    print(len(d))
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
