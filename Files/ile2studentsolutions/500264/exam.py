from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl=[]
        assert len(args) is not 0,"DictList.__init__:"+"no argument!"
        for i in args:
            assert type(i) is dict,"DictList.__init__:"+repr(i)+" is not a dictionary"
            self.dl.append(i)
    def __len__(self):
        l_list=[]
        for i in self.dl:
            for k in i:
                if k not in l_list:
                    l_list.append(k)
        return len(l_list)
    def __repr__(self):
        return "DictList("+",".join(repr(i) for i in self.dl)+")"
    def __contains__(self,key):
        for i in self.dl:
            if key in i:
                return True
        return False

    def __getitem__(self,key):
        item=None
        for i in self.dl:
            if key in i:
                item=i[key]
        if item == None:
            raise KeyError
        else:
            return item
    def __setitem__(self,key,value):
        key_list=[]
        for p in self.dl:
            for g in p.keys():
                key_list.append(g)
        if key in key_list:
            for i in reversed(self.dl):
                if key in i:
                    i[key]=value
                    return
        else:
            self.dl.append({key:value})      
    def __call__(self,key):
        c_list=[]
        for i in enumerate(self.dl,0):
            if key in i[1]:
                c_list.append((i[0],i[1][key]))
        return c_list
    def __iter__(self):
        k_list=[]
        i_list=[]
        for i in reversed(self.dl):
            for k,v in sorted(i.items(),key= lambda x:x[0]):
                if k not in k_list:
                    i_list.append((k,v))
                    k_list.append(k)
        return iter(i_list)
    def __eq__(self,right):
        if type(right) not in (DictList,dict):
            raise TypeError("DictList.__eq__: right operand is not DictList or dict")
        k_set=set()
        for i in self.dl:
            for k in i.keys():
                k_set.add(k)
        
        for i in k_set:
            if i not in right:
                return False
            elif self[i] !=right[i]:
                return False
        return True
    def __add__(self,right):
        if type(right) not in (DictList,dict):
            raise TypeError("DictList.__add__: right operand is not DictList or dict")
        if type(right)==DictList:
            self_set=set()
            for i in self.dl:
                for k in i.keys():
                    self_set.add(k)
            right_set=set()
            for i in right.dl:
                for k in i.keys():
                    right_set.add(k)
            self_dict={}
            right_dict={}
            for i in self_set:
                self_dict[i]=self[i]
            for i in right_set:
                right_dict[i]=right[i]
            return DictList(self_dict,right_dict)
        elif type(right)==dict:
            copy_self=[i for i in self.dl]
            copy_right=dict(zip(right.keys(),right.values()))
            return eval("DictList("+",".join(repr(i) for i in copy_self)+","+repr(copy_right)+")")
    def __radd__(self,right):
        if type(right) not in (DictList,dict):
            raise TypeError("DictList.__add__: right operand is not DictList or dict")
        if type(right) is DictList:
            self.__add__(right)
        else:
            copy_self=[i for i in self.dl]
            copy_right=dict(zip(right.keys(),right.values()))
            return eval("DictList("+repr(copy_right)+","+",".join(repr(i) for i in copy_self)+")")
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test


    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
    driver.default_show_traceback=True
    driver.driver()
