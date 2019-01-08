from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        if type(args) == tuple and len(args) == 0:
            raise AssertionError
        for arg in args:
            if type(arg) == dict:
                self.dl.append(arg)
            else:
                raise AssertionError
    
    def __len__(self):
        set_keys = set()
        for ele in self.dl:
            for key in ele.keys():
                set_keys.add(key)
        return len(set_keys)
    
    def __repr__(self):
        builder = "DictList("
        for d in self.dl:
            builder += str(d) + ','
            
        return builder[:-1] + ')'
        

    def __contains__(self,key:str):
        for d in self.dl:
            if key in d.keys():
                return True
        return False
    
    def __getitem__(self, key):
        in_graph = False
        for d in self.dl:
            if key in d.keys():
                value = d[key]
                in_graph = True
        if not in_graph:
            raise KeyError
        else:
            return value
            
    def __setitem__(self, key, value):
        in_graph = False
        for index in range(len(self.dl)):
            if key in self.dl[index].keys():
                dict_to_change = index
                in_graph = True
        if in_graph:
            self.dl[dict_to_change][key] = value
        else:
            self.dl.append({key:value})
    def __call__(self, key):
        index_list = []
        for index in range(len(self.dl)):
            if key in self.dl[index].keys():
                index_list.append((index, self.dl[index][key]))
        return index_list
    
    def __iter__(self):
        tuple_list = []  #(key, value)
        key_set = set()
        for index in range(len(self.dl)-1,-1,-1):
            for key in self.dl[index].keys():
                if key not in key_set:
                    key_set.add(key)
                    tuple_list.append((key, self.__getitem__(key)))
                    
                
        #weird sort stuff
        for tup in tuple_list:
            yield(tup)
                
    def __eq__(self, other):     
        if type(other) == DictList:
            self_keys = set()
            other_keys = set()
            for ele in self.dl:
                for key in ele.keys():
                    self_keys.add(key)
            for ele in other.dl:
                for key in ele.keys():
                    other_keys.add(key)
            if self_keys == other_keys:
                for key in self_keys:
                    if not self.__getitem__(key) == other.__getitem__(key):
                        return False
            return True
             
        elif type(other) == dict:
            self_keys = set()

            for ele in self.dl:
                for key in ele.keys():
                    self_keys.add(key)
            if sorted(list(self_keys)) == sorted(list(other.keys())):
                for key in self_keys:
                    if not self.__getitem__(key) == other[key]:
                        return False
            else:
                return False
            return True            
        else:
            raise TypeError
            

            
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
