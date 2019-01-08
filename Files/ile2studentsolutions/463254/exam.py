from goody import type_as_str  # Useful in some exceptions


class DictList:
    def __init__(self,*argue_dic):
        assert len(argue_dic)!=0,"da"
        if len(argue_dic)==1:
            if type(argue_dic[0])!= dict:
                raise AssertionError( "f")
        for item in argue_dic:
            if type(item)!= dict:
                raise AssertionError( "h")
        self.dl=list(argue_dic)
    
    def __len__(self):
        keys=set()
        for item in self.dl:
            for key in item.keys():
                keys.add(key)
        return len(keys)
            
            #fix this
    def __repr__(self):
        strr = "DictList("
        for x in self.dl:
            strr= strr + str(dict(x)) +','
        strr.strip(',')
        return strr+')'
    
    def __contains__(self,key):
        for item in self.dl:
            if key in item.keys():
                return True
        return False
        
    def __getitem__(self, key):
        storage=0
        check_in=False
        for item in self.dl:
            if key in item.keys():
                check_in =True
                if storage<item[key]:
                    storage = item[key]
        if check_in:
            return storage
        else:
            raise KeyError
        
    def __setitem__(self,key,value):
        storage=0
        index_num =0
        check_in=False
        for index in range(0,len(self.dl)):
            if key in self.dl[index].keys():
                check_in =True
                if storage<self.dl[index][key]:
                    storage = self.dl[index][key]
                    index_num=index
        if check_in == False:
            self.dl.append({key:value})
        else:
            self.dl[index_num][key]= value
        
    def __call__(self,key):
        list_k = []
        for index in range(0,len(self.dl)):
            if key in self.dl[index].keys():
                list_k.append((index,self.dl[index][key]))
        return list_k
#                         
    def __iter__(self):
        def iter_gen(list_dict):
            list_=[]
            for index in range(0,len(list_dict)):
                list_=[]
                count=1
                for key in list_dict[index].keys():
                    if count==len(list_dict[index].keys()) and index+1!=(len(list_dict)):
                        pass
                    else:
                        yield((key,list_dict[index][key]))
                count+=1
                          
        return iter_gen(self.dl)
#     
#     def __iter__(self):
#         def iter_gen(list_dict):
#             seen = False
#             key=''
#             sorte = sorted(list_dict, reverse=True)
#             print(sorte)
#             for item in sorte:
#                 for keys in item.keys():
#                     if key!=keys:
#                         key=key
#                         yield((key,list_dict[item][keys]))
#         return iter_gen(self.dl)
#     
    def __eq__(self,right):
        if type(right)==DictList:
            return self.dl == right
        elif type(right)==dict:
            count=1
            for index in range(0,len(self.dl)):
                for keys in self.dl[index].keys():
                    if right.keys() not in keys:
                        return False
                    for key in keys:
                        count+=1
                        if count==len(keys) and index+1==len(self.dl):
                            pass
                        else:
                            if right[key]!=self.dl[index][key]:
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
