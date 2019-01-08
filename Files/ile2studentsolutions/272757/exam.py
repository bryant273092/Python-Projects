# submitter: bhuynh4(Huynh,Benjamin)
from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*param):
        self.dl = []
        for x in param:
            if type(x) is dict and x !=None:
                self.dl.append(x)
            else:
                raise AssertionError
    
    def __len__(self):
        result = 0
        unique = []
        for x in self.dl:
            for k in x.keys():
                if k not in unique:
                    unique.append(k)
                    result+=1
        return result
    
    def __repr__(self):
        result = str(tuple(self.dl))
        return 'DictList{}'.format(result)

    def __contains__(self,item):
        for x in self.dl:
            if item in x:
                return True
        return False
            
    def __getitem__(self,item):
        result = {}
        for x in self.dl:
            if item in x:
                if item not in result:
                    result[item] = x[item]
                else:
                    if x[item] > result[item]:
                        result[item] = x[item]
        if result == None:
            raise KeyError
        return result[item]
    
    def __setitem__(self,item,value):
        result = []
        for i in range(len(self.dl)-1,-1,-1):
            if item in self.dl[i]:
                self.dl[i][item] = value 
                result.append(item)
                break
        if item not in result:
            new_dict ={}
            new_dict[item] = value
            self.dl.append(new_dict)
            result = []

    def __call__(self,item):
        result = []
        for x in range(len(self.dl)):
            if item in self.dl[x]:
                result.append((x, self.dl[x][item]))
        return result
            
    def __iter__(self):
        temp_dict ={}
        for i in range(len(self.dl)-1,-1,-1):
            for k,v in self.dl[i].items():
                if k not in temp_dict:
                    temp_dict[k]=v
                    yield ((k,v))
    
    def __eq__(self,right):
        list1,list2= [],[]
        result_dict = {}
        for x in self.dl:
            for k in x.keys():
                if k not in list1:
                    list1.append(k)
        for x in right.dl:
            for k in x.keys():
                if k not in list2:
                    list2.append(k)
        if sorted(list1) == sorted(list2):
            for x in self.dl:
                for i in x.keys():
                    for y in right.dl:
                        for i2 in y.keys():
                            if x[i] == y[i2]:
                                result_dict[i] = x[i]
        else: return False
        if sorted(result_dict.keys()) == sorted(list1):
            return True
        else: return False
        
        """s_dict,r_dict = {},{}
        if type(right) is dict or right is DictList:
            for x in self.dl:
                for k,v in x.items():
                    for y in right:
                        for k2,v2 in y.items():"""
                            
                    
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    #d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    #d2 = DictList(dict(a=1,b=12), dict(c=13))
    #print (d1 == d2)
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
