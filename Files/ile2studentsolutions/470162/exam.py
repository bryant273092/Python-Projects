from goody import type_as_str  # Useful in some exceptions
import copy
class DictList:
    def __init__(self, *args):
        self.dl = []
        if(len(args) == 0):
            print(f"DictList.__init__: arg contains no dictionaries")
            raise AssertionError;
        for arg in args:
            if(type(arg) is not dict):
                print(f"DictList.__init__:{arg} is not a dictionary.")
                raise AssertionError;
            else:
                self.dl.append(arg);

    def __len__(self):
        unique_key_set = set()
        for some_dict in self.dl:
            for key in some_dict.keys():
                unique_key_set.add(key)
                
        return len(unique_key_set)
    
    def __repr__(self):
        return ("DictList(" + ", ".join(str(some_dict) for some_dict in self.dl) + ")")
    
    def __contains__(self, key):
        for elem in self.dl:
            try:
                elem[key];
                return True;
            except KeyError:
                pass;
        return False;
    
    def __getitem__(self, key):
        cur_val = None;
        for elem in self.dl:
            try:
                cur_val = elem[key];
            except KeyError:
                pass;
            
        if(cur_val != None):
            return cur_val;
        else:
            print(f"DictList.__getitem__: {key} is not in DictList")
            raise KeyError;
        
    def __setitem__(self, key, value):
        last_dict = None
        for sub_dict in self.dl:
            try:
                sub_dict[key]
                last_dict = sub_dict
            except KeyError:
                pass;
        if(last_dict != None):
            last_dict[key] = value;
        else:
            self.dl.append({key: value})
            
    def __call__(self, key):
        ret_list = []
        dl_len = len(self.dl)
        for i in range(0, dl_len):
            try:
                ret_list.append((i, self.dl[i][key]));
            except KeyError:
                pass;
        return ret_list;
    
    def __iter__(self):
        used_keys = set();
        for sub_dict in reversed(self.dl):
            for key in sorted(sub_dict.keys()):
                try:
                    if (key not in used_keys):
                        yield (key, sub_dict[key]);
                        used_keys.add(key)
                except KeyError:
                    pass;
                
    def __eq__(self, right):
        if(type(right) is not DictList and type(right) is not dict):
            print(f"DictList.__eq__: {right} is of type {type(right)} it should be of type dict or DictList")
            raise TypeError
        my_dict_iter = iter(self)
        for two_tuple in my_dict_iter:
            try:
                if(self[two_tuple[0]] != right[two_tuple[0]]):
                    return False;
            except KeyError:
                return False;
        return True;
        #loop through keys of self
        
    def __radd__(self, left):
        if(type(left) is not dict):
            print(f"DictList.__radd__: {left} is of type {type(left)} it should be of type dict or DictList")
            raise TypeError
        
        return DictList(copy.copy(left), *(copy.copy(sub_dict) for sub_dict in self.dl))
    
    def __add__(self, right):
    
        if(type(right) is not DictList and type(right) is not dict):
            print(f"DictList.__add__: {right} is of type {type(right)} it should be of type dict or DictList")
            raise TypeError   
        if(type(right) is dict):
            return DictList(*(copy.copy(sub_dict) for sub_dict in self.dl), copy.copy(right))
        else:
            left_iter = iter(self)
            right_iter = iter(right)
            left_dict = dict()
            right_dict = dict()
            for two_tuple in left_iter:
                left_dict.setdefault(two_tuple[0], two_tuple[1])
            for two_tuple in right_iter:
                right_dict.setdefault(two_tuple[0], two_tuple[1]) 
            return DictList(copy.copy(left_dict), copy.copy(right_dict))
        
        
         
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
 
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
