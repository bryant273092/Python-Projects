from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl = []
        if len(args) == 0:
            raise AssertionError('There are no dictionaries')
        else:
            for i in args:
                if type(i) != dict:
                    raise AssertionError(f'{i} is not a dictionary')
                else:
                    self.dl.append(i)
                    
    def __len__(self):
        count = 0
        used_keys = []
        for i in self.dl:
            for key in i.keys():
                if key not in used_keys:
                    count += 1
                    used_keys.append(key)
        return count
    
    def __repr__(self):
        dict_str = ''
        for i in self.dl:
            dict_str += str(i) + ', '
        dict_str = dict_str[:-2]
        return f"DictList({dict_str})"
    
    def __contains__(self,value):
        for i in self.dl:
            if value in i.keys():
                return True
            
    def __getitem__(self,value):
        stored_value = 0
        all_keys = set()
        for i in self.dl:
            for key in i.keys():
                all_keys.add(key)
        if value not in all_keys:
            raise KeyError
        else:
            for i in self.dl:
                if value in i.keys():
                    stored_value = i[value]
            return stored_value
            
    def __setitem__(self,key,value):
        appears_in = []
        for i in self.dl:
            if key in i.keys():
                appears_in.append(self.dl.index(i))
        if len(appears_in) == 0:
            new_dict = {key:value}
            self.dl.append(new_dict)
        else:
            appears_in_last = max(appears_in)
            self.dl[appears_in_last][key] = value
                
    def __call__(self,key):
        list_of_tuples = []
        for i in self.dl:
            if key in i.keys():
                list_of_tuples.append((self.dl.index(i),i[key]))
        return list_of_tuples
    
    def __iter__(self):
        used_value = []
        for i in reversed(self.dl):
            for k,v in i.items():
                if k not in used_value:
                    yield (k,v)
                    used_value.append(k)

    def __eq__(self,other):
        if type(other) == DictList:
            own_keys = set()
            other_keys = set()
            for i in self.dl:
                for j in i.keys():
                    own_keys.add(j)
            for m in other.dl:
                for l in m.keys():
                    other_keys.add(l)
            if own_keys == other_keys:
                for x in own_keys:
                    if self[x] != other[x]:
                        return False
                return True
            else:
                return False
        elif type(other) == dict:
            own_keys = set()
            for i in self.dl:
                for m in i.keys():
                    own_keys.add(m)
            if own_keys == other.keys():
                for j in own_keys:
                    if self[j] != other[j]:
                        return False
                return True
            else:
                return False
        else:
            raise TypeError(f'{other} is not a DictList or dictionary')
         
    def __add__(self,other):
        if type(other) == DictList:
            pass
        elif type(other) == dict:
            pass
        else:
            raise TypeError(f'{other} is not a DictList or dictionary')
    
                
                
                
                
                
        
        
            




            
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
