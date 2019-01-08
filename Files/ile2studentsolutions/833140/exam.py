from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        assert len(args) !=0, "No dicts were passed"
        for i in args:
            assert type(i) is dict
        self.dl = list(args)
        
    def __len__(self):
        unique_keys = set()
        dl_len = 0
        for k in self.dl:
            for kk in k:
                if kk not in unique_keys:
                    dl_len += 1
                    unique_keys.add(kk)
        return dl_len
    
    def __repr__(self):
        return "DictList({})".format(', '.join([str(x) for x in self.dl]))
    
    def __contains__(self, value):
        for d in self.dl:
            for k in d.keys():
                if k == value:
                    return True
        return False
    
    def __getitem__(self, value):
        if not self.__contains__(value):
            raise KeyError('{} appears in no dictionaries')
        
        for d in self.dl:
            for k,v in d.items():
                if k == value:
                    dl_v = v
        return dl_v
    
    def __setitem__(self, key, value):
        changed_existing_dict = False
        set_index = 0
        for i, d in enumerate(self.dl):
            for k,_ in d.items():
                if k == key:
                    set_index = i
                    changed_existing_dict = True
        
        if not changed_existing_dict:
            self.dl.append({key:value})
        
        else:
            self.dl[set_index][key] = value
            
    def __call__(self, key):
        call_list = []
        for i, d in enumerate(self.dl):
            for k,v in d.items():
                if k == key:
                    call_list.append(tuple((i,v)))
        return call_list
    
    def __iter__(self):
        i = int(len(self.dl)-1)
        unique_keys = set()

        while i >= 0:
            for k,v in self.dl[i].items():
                if k not in unique_keys:
                    yield(tuple((k,v)))
                    unique_keys.add(k)
            i -= 1
    def __eq__(self, right):
        if type(right) not in [DictList, dict]:
            raise TypeError('Must be type DictList or dict, was type {type}'.format(type=type(right)))
        
        if type(right) == DictList:
            for d in self.dl:
                for k,v in d.items():
                    if self.__getitem__(k) != right.__getitem__(k):
                        return False
            return True
        
        else:
            for k,v in self:
                if k not in right or right[k] != v:
                    return False
            return True
    
    def __add__(self, right):
        if type(right) not in [DictList, dict]:
            raise TypeError('Must be type DictList or dict, was type {type}'.format(type=type(right)))
        
        if type(right) == DictList:
            sum_dl = DictList(dict([i for i in self]), dict([j for j in right]))
            
            return sum_dl
        
        else:
            copy_dl = self.dl.copy()
            copy_d = right.copy()
            sum_dl = eval( "DictList({})".format( ', '.join( [str(x) for x in copy_dl] ) + ', '+ str(copy_d) ) )\
            
            return sum_dl
        
    def __radd__(self,left):
        if type(left) != dict:
            raise TypeError('Must be type DictList or dict, was type {type}'.format(type=type(left)))
        
        copy_dl = self.dl.copy()
        copy_d = left.copy()
        sum_dl = eval( "DictList({})".format( str(copy_d) + ', ' + ', '.join( [str(x) for x in copy_dl] ) ) )\
        
        return sum_dl
        
        
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
