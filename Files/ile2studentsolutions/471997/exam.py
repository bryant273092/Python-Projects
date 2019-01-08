from goody import type_as_str  # Useful in some exceptions
from _operator import index

class DictList:
    #Jeremy Sto Tomas 34834909
    def __init__(self, *args):
        dict_list = []
        if args == ():
            raise AssertionError
        for argument in args:
            if type(argument) != dict or len(args) == 0 or args == None:
                raise AssertionError
            else:
                dict_list.append(argument)
        self.dl = dict_list
        
    def __len__(self):
        return_set = set()
        for dict_l in self.dl:
            for key in dict_l.keys():
                return_set.add(key)
        return len(return_set)
    
    def __repr__(self):
        return_string = ""
        
        for i in self.dl:
            if self.dl.index(i) != len(self.dl) -1:
                return_string += str(i) + ", "
            else:
                return_string += str(i)
        return "DictList({})".format(return_string)
                
   
    
    def __contains__(self, value):
        return_set = set()
        for i in self.dl:
            for key in i.keys():
                return_set.add(key)
        return value in return_set
    
    def __getitem__(self, value):
        return_set = set()
        for dict_l in self.dl:
            for key in dict_l.keys():
                return_set.add(key)
        if value not in return_set:
            raise KeyError
        else:
            comparison_dict = []
            for dict_l in self.dl:
                if value in dict_l.keys():
                    comparison_dict.append(dict_l)
            return comparison_dict[-1][value]
        
    def __setitem__(self, value, item):
        return_set = set()
        for dict_l in self.dl:
            for key in dict_l.keys():
                return_set.add(key)
        if value not in return_set:
            self.dl.append({value:item})
        else:
            comparison_dict = []
            for dict_l in self.dl:
                if value in dict_l.keys():
                    comparison_dict.append(dict_l)
            comparison_dict[-1][value] = item
    
    def __call__(self,value):
        return_set = set()
        for dict_l in self.dl:
            for key in dict_l.keys():
                return_set.add(key)
        if value not in return_set:
            return []
        else:
            return_list = []
            for i in self.dl:
                if value in i.keys():
                    indexer = self.dl.index(i)
                    val = i[value]
                    return_list.append((indexer,val))
            return return_list
        
    def __iter__(self):
        def gen(gen_obj):
            used_set = set()
            outer_list = []
            for dict_l in self.dl[::-1]:
                inner_dict_list = []
                for i in dict_l.items():
                    if i[0] not in used_set:
                        used_set.add(i[0])
                        inner_dict_list.append(i)
                    else:
                        pass
                for i in sorted(inner_dict_list, key = lambda x: x[0]):
                    outer_list.append(i)
            for i in outer_list:
                yield i
            
        return gen(self.dl)
    
    
    
    def __eq__(self, right):
        if type(right) not in [dict, DictList]:
            raise TypeError
        elif type(right) == dict and type(self) == DictList:
            right_key = set()
            return_set = set()
            for dict_l in self.dl:
                for key in dict_l.keys():
                    return_set.add(key)
            for i in right.keys():
                right_key.add(i)
            if right_key != return_set:
                return False
            
            for right_key in right.keys():
                if right[right_key] == self.__getitem__(right_key):
                    pass
                else:
                    return False 
            return True
        elif type(right) == DictList and type(self) == DictList:
            right_set = set()
            return_set = set()
            for dict_l in self.dl:
                for key in dict_l.keys():
                    return_set.add(key)
                    
            for dict_l in right.dl:
                for key in dict_l.keys():
                    right_set.add(key)
            
            if right_set != return_set:
                return False
            else:
                for i in return_set:
                    if right[i] != self.__getitem__(i):
                        return False
                    else:
                        pass
                return True
            
                
        
            
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
