from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        assert len(args)>0, 'the length must be greater than 0' 
        for i in args:
            assert isinstance(i,dict), '{i} is not a dictionary'.format(i=str(i))
            
        self.dl=list(args) 
        
    def __len__(self):
        key_set=set()
        for i in self.dl:
            key_set.update({k for k in i.keys()})
            
        return len(key_set) 
    
    def __repr__(self):
        eval_str=str(self.dl).lstrip('[').rstrip(']')
        return('''DictList({0})'''.format(eval_str)) 
    
    def __contains__(self,key):
        for i in self.dl:
            if key in i.keys():
                return True
            
        else: return False 
        
    def __getitem__(self,index):
        have=False
        for i in self.dl:
            if index in i.keys():
                result=i[index] 
                have=True
        if not have:
            raise KeyError('{0} appears in no dictionaries'.format(index))
        else:
            return result
         
        
    def __setitem__(self,index,value):
        set_dict=None
        for i in self.dl:
            if index in i.keys():
                set_dict=i 
                
        if set_dict==None:
            new_dict={index:value} 
            self.dl.append(new_dict)
        else:
            set_dict[index]=value  
            
    def __call__(self,index):
        result=[] 
        for i in range(len(self.dl)):
            if index in self.dl[i].keys():
                result.append(tuple([i, self.dl[i][index]])) 
        return result
                
    def __iter__(self):
        key_list=[]
        for i in range (len(self.dl)):
            for k in self.dl[-i-1]:
                if not (k in key_list):
                    yield (tuple([k,self.dl[-i-1][k]])) 
                    key_list.append(k) 
                    
    def __eq__(self,other):
        if not type(other) in (dict,DictList):
            
            raise TypeError('''false comparasion between {type_self} and 
{type_other}'''.format(type_self=type_as_str(self), type_other=type_as_str(other)))
            
        elif len(self)!=len(other):
            return False
        else:
            for i in self.dl:
                for k in i.keys():
                    if self[k]!=other[k]:
                        return False
            else:
                return True 
            
    def __add__(self,other):
        if type(other) is dict:
            result=[]
            for i in self.dl:
                result.append(dict(i))
            result.append(dict(other))
            return DictList(*result)  
        elif type(other) is DictList:
            d1,d2=dict(),dict()
            
            def merge(d, dict_list):
                for i in dict_list:
                    d.update(dict(i)) 
                return d 
                
            d1,d2=merge(d1, self.dl),merge(d2,other.dl) 
            
            
            return DictList(d1,d2)
             
        else:
            
            raise TypeError('''false operation between {type_self} and 
{type_other}'''.format(type_self=type_as_str(self), type_other=type_as_str(other)))
            
                    
    def __radd__(self,other):
        if type(other) is dict:
            result=[dict(other)]
            for i in self.dl:
                result.append(dict(i)) 
            return DictList(*result) 
        else:
            
            raise TypeError('''false operation between {type_self} and 
{type_other}'''.format(type_self=type_as_str(self), type_other=type_as_str(other)))            
    
            




            
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
