from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        for i in args:
            if type(i)!=dict:
                raise AssertionError
        self.dl=[i for i in args]
        if self.dl==[]:
            raise AssertionError
    def __len__(self):
        coll=set()
        for i in self.dl:
            for j in i.keys():
                coll.add(j)
        return len(coll)
    def __repr__(self):
        long_str='DictList('
        for i in self.dl:
            long_str+=str(i)+','
        return long_str[:-1]+')'
    def __contains__(self,item):
        result=[]
        for i in self.dl:
            for j in i.keys():
                result.append(j)
        if item in result:
            return True
        else:
            return False
    def __getitem__(self,item):
        new_dic=dict()
        for i in self.dl:
            for j in i.keys():
                if j not in new_dic.keys():
                    new_dic.update({j:list()})
                    new_dic[j].append(i[j])
                else:
                    new_dic[j].append(i[j])
        if len(new_dic[item])>1:
            try:
                return max(new_dic[item])
            except:
                return new_dic[item][0]
        else:
            return new_dic[item][0]
    def __setitem__(self,item,value):
        dl_keys=set()
        for i in self.dl:
            for j in i.keys():
                dl_keys.add(j)
        if item not in dl_keys:
            self.dl.append(dict([(item,value)]))
        elif item in dl_keys:
            for i in self.dl:
                for j,k in i.items():
                    if k==self.__getitem__(item):
                        i[j]=value
    def __call__(self,item):
        result=[]
        for j,k in enumerate(self.dl):
            if item in k.keys():
                result.append((j,k[item]))
        return result
    def __iter__(self):
        reverse=[]
        new_dic=dict()    
        for i in range(len(self.dl)-1,-1,-1):
            reverse.append(self.dl[i])
        for i in reverse:
            result=[]
            for j in i.keys():
                if j not in new_dic.keys():
                    new_dic.update({j:list()})
                    new_dic[j].append(i[j])
                    result.append((j,new_dic[j][0]))
                else:
                    pass
            for x in result:
                yield x
    def __eq__(self,right):
        if type(right) not in (DictList,dict):
            raise TypeError
        set_a=set()
        set_b=set()
        for i in self.dl:
            for j in i.keys():
                set_a.add(j)
        if type(right)==DictList:
            for i in right.dl:
                for j in i.keys():
                    set_b.add(j)
        elif type(right)==dict:
            for i in right.keys():
                set_b.add(i)
        key_list=list((set_a | set_b))
        try:
            return all(self.__getitem__(i)==right.__getitem__(i) for i in key_list)
        except KeyError:
            return False 

            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d0 = dict(a=1,b=2,c=3)
    d1 = dict(c=13,d=14,e=15)
    d2 = dict(e=25,f=26,g=27)
    d = DictList(d0,d1,d2)
    d_b=DictList(dict(a=1,b=2,c=13,d=14,e=25,f=26,g=27))
    print(d('c'))
    for i in d:
        print(i)
    assert d_b==d
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
