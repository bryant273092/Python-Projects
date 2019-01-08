from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        assert len(args)>0,"can't be empty"
        self.dl=[]
        for item in args:
            assert type(item) is dict,f"'{item}' is not a dictionary"
            self.dl.append(item)
    
    def __len__(self):
        answer=set()
        for item in self.dl:
            for k in item.keys():
                answer.add(k)
        return len(answer)
    
    def __repr__(self):
        return "DictList({})".format(",".join([str(a) for a in self.dl]))
    
    def __contains__(self,value):
        key_lst=[]
        for item in self.dl:
            for k in item.keys():
                key_lst.append(k)
        if value in key_lst:
            return True
        else:
            return False
    
    def __getitem__(self,value):
        answer=[]
        if self.__contains__(value):
            for item in self.dl:
                for k,v in item.items():
                    if k is value:
                        answer.append((self.dl.index(item),v))
            if len(answer)==1:
                return answer[0][1]
            else:
                answer=sorted(answer,key=lambda x:-x[0])
                return answer[0][1]
        else:
            raise KeyError(f"{value} is not a key")
        
    
    def __setitem__(self,name,value):
        if self.__contains__(name):
            target_value=self.__getitem__(name)
            for item in self.dl:
                for k,v in item.items():
                    if k is name and v is target_value:
                        item[k]=value
        else:
            new={}
            new[name]=value
            self.dl.append(new)
    
    def __call__(self,value):
        answer=[]
        if self.__contains__(value):
            for item in self.dl:
                for k,v in item.items():
                    if k is value:
                        answer.append((self.dl.index(item),v))
            return sorted(answer,key=lambda x:x[0])
        else:
            return []
        
    def __iter__(self):
        answer=[]
        used_key=[]
        for item in self.dl:
            for k,v in item.items():
                answer.append((self.dl.index(item),k,v))
        answer=sorted(answer,key=lambda x:(-x[0],x[1]))
        for _,k,v in answer:
            if k not in used_key:
                yield(k,v)
                used_key.append(k)
    
    def __eq__(self,right):
        if type(right) is not DictList and type(right) is not dict:
            raise TypeError("must compare with either DictList object or a dictionary object")
        elif type(right) is DictList:
            key_lst=set()
            for item in self.dl:
                for k in item.keys():
                    key_lst.add(k)
            key_lst_rt=set()
            for itemr in right.dl:
                for k in itemr.keys():
                    key_lst_rt.add(k)
            
            if not key_lst.isdisjoint(key_lst_rt):
                for key in list(key_lst):
                    try:
                        if self.__getitem__(key)!=right.__getitem__(key):
                            return False
                    except:
                        return False
                else:
                    return True
            else:
                return False
            
        elif type(right) is dict:
            key_lst=set()
            for item in self.dl:
                for k in item.keys():
                    key_lst.add(k)
            key_lst_rt=set(list(right.keys()))
            
            if not key_lst.isdisjoint(key_lst_rt):
                for key in list(key_lst):
                    try:
                        if self.__getitem__(key)!=right[key]:
                            return False
                    except:
                        return False
                else:
                    return True
            else:
                return False

    def __add__(self,right):
        if type(right) is not DictList and type(right) is not dict:
            raise TypeError(f"{right} must either be a dictionary or a DictList")
        elif type(right) is DictList:
            left_key_list=set()
            left_dict={}
            for item in self.dl:
                for k in item.keys():
                    left_key_list.add(k)
            for key in left_key_list:
                left_dict[key]=self.__getitem__(key)
            
            right_key_list=set()
            right_dict={}
            for itemr in right.dl:
                for k in itemr.keys():
                    right_key_list.add(k)
            for keyr in right_key_list:
                right_dict[keyr]=right.__getitem__(keyr)
            
            return DictList(left_dict,right_dict)
        elif type(right) is dict:
            new={}
            for k,v in right.items():
                new[k]=v
            return DictList(*(a for a in self.dl),new)
    
    def __radd__(self,left):
        if type(left) is dict:
            new={}
            for k,v in left.items():
                new[k]=v
            return DictList(new,*(a for a in self.dl))
        else:
            raise TypeError(f"{left} must be a dictionary")


            
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
