from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = [];
        if len(args) == 0:
            raise AssertionError("Dictlist.__init__: at least one argument required");
        for arg in args:
            if type(arg) is not dict:
                raise AssertionError(f"Dictlist.__init__: {arg} is not a dictionary");
            else:
                self.dl.append(arg);
                
    def __len__(self):
        result_set = set();
        for dct in self.dl:
            for key in dct:
                result_set.add(key)
        return len(result_set);
    
    def __repr__(self):
        return f"DictList({str(tuple((dct for dct in self.dl)))[1:-1]})";
    
    def __contains__(self, key):
        for dct in self.dl:
            for k in dct.keys():
                if k == key:
                    return True;
        return False;
    
    def __getitem__(self, key):
        item = None;
        for dct in self.dl:
            for k,v in dct.items():
                if k == key:
                    item = v;
        if item == None:
            raise KeyError(f"DictList.__getitem__: '{key}' appears in no dictionaries");
        else:
            return item;
    
    def __setitem__(self, key, value):
        existed_dct = None;
        for dct in self.dl:
            for k,v in dct.items():
                if k == key:
                    existed_dct = dct;
        if existed_dct == None:
            self.dl.append({key:value});
        else:
            existed_dct[key] = value;
    
    def __call__(self, key):
        returned_lst = [];
        for i in range(len(self.dl)):
            for k,v in self.dl[i].items():
                if k == key:
                    returned_lst.append((i,v));
        return returned_lst;
    
    def __iter__(self):
        appeared_key = set();
        for i in range(len(self.dl)-1, -1, -1):
            for k,v in sorted(self.dl[i].items()):
                if k not in appeared_key:
                    appeared_key.add(k);
                    yield (k,v);
    
    def __eq__(self, right):
        self_k_v_set = set(i for i in self);
        if type(right) is DictList:
            right_k_v_set = set(i for i in right);
            return self_k_v_set == right_k_v_set;
        elif type(right) is dict: 
            right_k_v_set = set((k,v) for k,v in right.items());
            return self_k_v_set == right_k_v_set;
        else:
            raise TypeError(f"DictList.__eq__: {right} is neither a DictList or a Dict");
        
    def __add__(self, right):
        if type(right) is DictList:
            dict_self = dict(i for i in self);
            dict_right = dict(i for i in right);
            return DictList(dict_self, dict_right);
        elif type(right) is dict:
            dict_lst = [dict(dct) for dct in self.dl]
            dict_lst.append(dict(right));
            return DictList(*tuple(dict_lst));
        else:
            raise TypeError(f"DictList.__add__: {right} is neither a DictList nor a Dict");
        
    def __radd__(self, left):
        if type(left) is dict:
            dict_lst = [dict(left)];
            for dct in self.dl:
                dict_lst.append(dict(dct));
            return DictList(*tuple(dict_lst));
        else:
            raise TypeError(f"DictList.__radd__: {left} is not a valid dictionary");
        
        
            
        




            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test


    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#    driver.default_show_exception=True
#    driver.default_show_exception_message=True
#    driver.default_show_traceback=True
    driver.driver()
