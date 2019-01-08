from goody import type_as_str  # Useful in some exceptions
import copy

class DictList:
    
    def __init__(self,*args):
        assert len(args) != 0, 'You must submit either 1 or more dictionary'
        #print(args)
        for i in args:
            assert type(i) == dict, f'DictList.__init__:{i} is not a dictionary.'
        self.dl = list(args)
        #print('self.dl',self.dl)
        
    def __len__(self):
        a_set_of_keys = set()
        for i in self.dl:
            for j in i:
                a_set_of_keys.add(j)
        #print(a_set_of_keys)
        return len(a_set_of_keys)
                
    def __repr__(self):
        return 'DictList(' + ','.join(str(i) for i in self.dl) + ')'

    
    def __contains__(self,value):
        for i in self.dl:
            for j in i:
                if j == value: return True
        return False
    
    def __getitem__(self,item):
        
        copy = list(self.dl)
        copy.reverse()
        for i in copy:
            for j in i:
                if j == item:
                    return i[j]
        raise KeyError(f'{item}  appears in no dictionaries')
        
        
    def __setitem__(self,key,value):
        #print('key, value',key,value)
        flag = 0
        copy = list(self.dl)
        copy.reverse()
        
        for i in copy:
            if key in i:
                i[key] = value
                flag = 1
                break
        
        if flag ==0:
            self.dl.append({key:value})
        else:
            copy.reverse()
            #print(copy)
            self.dl = copy
         
    def __call__(self,key):
        main_list = []
        for i in self.dl:
            for j in i:
                if j == key:
                    main_list.append(( self.dl.index(i)  , i[key] ))
                    
        return main_list
        
    def __iter__(self):
        
        def _gen(dl):
            a_set = set()
            dl.reverse()
            for i in dl:
                for j in sorted(i):
                    if j not in a_set: yield((j,i[j]))
                    a_set.add(j)
        return _gen(list(self.dl))
                    
                
            
    
    def __eq__(self,right):
        
        
        
        if type(right) == dict:
            if len(right) != len(self): return False
            
            for i in right:
                try:
                    if right[i] != self[i]:return False
                except KeyError:
                    return False
            return True
        
        elif type(right) == DictList:
            temp_set = set()
                
            if len(right) != len(self): return False
            
            for i in right.dl:
                for j in i:
                    temp_set.add(j)
            for k in temp_set:
                if self[k] != right[k]: return False
            return True
            
        else:
            raise TypeError('Operands must be either dict or DictList')
        
    
    
    def __add__(self,right):
        if type(right) == DictList:
            sett_of_left  = set()
            sett_of_right = set()
            
            for i in self.dl:
                for j in i:
                    sett_of_left.add(j)
            for i in right.dl:
                for j in i:
                    sett_of_right.add(j)
            
            #print('leftset',sett_of_left)
            #print('rightset',sett_of_right)
            
            
            left_dict = dict()
            right_dict = dict()
            
            for i in sett_of_left:
                left_dict[ i ] = copy.copy(self[i])
                
            for i in sett_of_right:
                right_dict[i] = copy.copy(right[i])
            
            return copy.deepcopy(DictList(left_dict, right_dict))
        
        
        
        elif type(right) == dict:
            main_list = []
            for i in self.dl:
                main_list.append(i)
            main_list.append(right)
            
            return copy.deepcopy(DictList(*main_list))
            
            
            
            
    def __radd__(self,right):
        #print('self is radd',self)
        #print('right in radd',right)
        if type(right) != dict: raise TypeError('right operand must be a dictionary or a DictList')
        main_list = []
        main_list.append(right)
        for i in self.dl:
            main_list.append(i)
        
        return copy.deepcopy(DictList(*main_list))
        
        
        #return self + right
        
        
        
        
        
        
    
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d = DictList(dict(a=1,b=2,c=3),dict(c=13,d=14,e=15), dict(e=25,f=26,g=27))
    #print(len(d))
    #print(repr(d))
    #print(d['c'])
    #d['c'] = 'new'
    #d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    #d2 = DictList(dict(a='one',b='two'), dict(b='twelve',c='thirteen'))
    #adict = dict(a='one',b='two')
    
    #d1+d2
    
    #d1+adict
    
    #print('adict+d1',adict+d1)
    
    #print('comoparing dictlist with dict',d1 == dict(a=1,b =12, z = 13))
    #print(d1 == d2)
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
