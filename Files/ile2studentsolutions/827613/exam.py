from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *kargs):
        self.dl=[]
        if kargs==():
            assert False, 'no parameters entered dict list requires at least 1'
        for value in kargs:
            if type(value)==dict:
                self.dl.append(value)
            elif kargs==() or type(value)!=dict:
                assert False, 'each value must be of type dict'
        
    def __len__(self):
        distinct=[]
        for d in self.dl:
            for value in d:
                if value not in distinct:
                    distinct.append(value)
        return len(distinct)
    
    def __repr__(self):
        dict_str='DictList('
        for value in self.dl:
            if value!=self.dl[-1]:
                dict_str=dict_str+str(value)+', '
            else:
                dict_str=dict_str+str(value)
        return dict_str+')'
    
    def __contains__(self,item):
        for value in self.dl:
            for d_list in value:
                if type(item)==str and item in d_list:
                    return True
        return False
    
    def __getitem__(self,item):
        current_dict=0
        g_item=0
        item_state=False
        for value in range(len(self.dl)):
            if item in self.dl[value]:
                item_state=True
                if value>=current_dict:
                    current_dict=value
                    g_item=self.dl[value][item]
        if item_state==False:
            raise KeyError('item not in Dict_List')
        else:
            return g_item
    
    def __setitem__(self,item,value):
        item_state=False
        counter=len(self.dl)-1
        for d in reversed(self.dl):
            if item in d:
                item_state=True
                self.dl[counter][item]=value
                break
            counter-=1
        if item_state==False:
            self.dl.append({item:value})
        
    def __call__(self,item):
        index_list=[]
        for value in range(len(self.dl)):
            if item in self.dl[value]:
                index_list.append((value,self.dl[value][item]))
        return index_list
    
    def __iter__(self):
        order=[]
        highest_value={}
        counter=len(self.dl)-1
        for d in reversed(self.dl):
            for l in d:
                order.append((l,self.dl[counter][l]))
            counter-=1
        order_copy=order.copy()
        for x in order_copy:
            if x[0] in highest_value and x[1]>highest_value[x[0]]:
                highest_value[x[0]]=x[1]
            elif x[0] not in highest_value:
                highest_value[x[0]]=x[1]    
        order=list(highest_value.items())
        for z in order:
            yield z
    
    def __eq__(self,right):
        for value in self.dl:
            for v in value:
                try:
                    if self[v]!=right[v]:
                        return False
                except KeyError:
                    return False
        return True
    
    
                
            
        
                     
        




            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d1 = dict(c=13,d=14,e=15)
    d  = DictList(d1)
    [i for i in d]

    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
