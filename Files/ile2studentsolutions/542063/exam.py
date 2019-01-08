from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        if len(args) == 0:
            raise AssertionError("Argument is not a dictionary")
        for item in args:
            assert type(item) == dict,"Argument is not a dictionary"
            self.dl.append(item)
        
    def __len__(self):
        count = 0
        key_set = set()
        for item in self.dl:
            for key in item.keys():
                key_set.add(key)
        for k in key_set:
            count+=1
        return count
    
    def __repr__(self):
        return 'DictList('+','.join(str(x) for x in self.dl)+')'
    
    def __contains__(self,check):
        for item in self.dl:
            if check in item.keys():
                return True
        return False
    
    def __getitem__(self,item):
        key_check = set()
        for each_d in self.dl:
            for each_k in each_d:
                key_check.add(each_k)
                
        if item not in key_check:
            raise KeyError("Key not in list")
        else:
            for d in self.dl:
                if item in d.keys():
                    value = d[item]
        return value
            
    def __setitem__(self,k,v):
        key_check = []
        key_set = set()
        for each_d in self.dl:
            for each_k in each_d:
                key_check.append(each_k)
                
        if k not in key_check:
            new_d = dict()
            new_d[k] = v
            self.dl.append(new_d)
        else:
            for each_d in self.dl[::-1]:
                for each_k in each_d:
                    if k == each_k and k not in key_set:
                        key_set.add(k)
                        each_d[k] = v
    
    def __call__(self,k):
        v_list = []
        v_tuple = ()
        
        for d in self.dl:
            for keys in d:
                if k == keys:
                    v_tuple = (self.dl.index(d), d[k])
                    v_list.append(v_tuple)
        return sorted(v_list)
    
    def __iter__(self):
        k_set = set()
        
        for d in self.dl[::-1]:
            for k,v in d.items():
                if k not in k_set:
                    k_set.add(k)
                    yield(k,v)
    
    def __eq__(self,d2):
        if type(d2) not in (DictList, dict):
            raise TypeError("Operand not of type DictList or dict")  
        
        if type(d2) == DictList:
            list1 = []
            list2 = []
            for d in self.dl:
                for k,v in d.items():
                    list1.append((k,v))

            for d in d2.dl:
                for k,v in d.items():
                    list2.append((k,v))

            if sorted(list1) != sorted(list2):
                return False
            
            count_matching = 0
            for d in self.dl:
                for d1 in d2.dl:
                    for k in d:
                        for k1 in d1:
                            if d[k] == d1[k1]:
                                count_matching +=1 
            count = 0
            for d in self.dl:
                for k in d:
                    count+=1
            if count != count_matching:
                return False
        
        elif type(d2) == dict:
            if d2 not in self.dl:
                return False
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
