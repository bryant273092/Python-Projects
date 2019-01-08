from goody import type_as_str  # Useful in some exceptions
from _operator import indexOf

class DictList:
    def __init__(self, *args):
        init_list = list()
        if len(args) == 0:
            raise AssertionError
        for arg in args:
            if type(arg) != dict:
                raise AssertionError
            if type(arg) == dict:
                init_list.append(arg)
        self.dl = list(init_list)
    
    def __len__(self):
        len_set = set()
        for item in self.dl:
            for key in item:
                if key not in len_set:
                    len_set.add(key)
        return len(len_set)
    
    def __repr__(self):
        repr_str = "DictList("
        for item in self.dl:
            repr_str += '{'
            for k, v in item.items():
                repr_str += "'"+k+"'"+':'+str(v)+', '
            repr_str = repr_str.rstrip(', ')
            repr_str += '}'
            repr_str += ', '
        repr_str = repr_str.rstrip(', ')
        repr_str += ")"
        return repr_str

    
    def __contains__(self, key):
        for item in self.dl:
            if key in item:
                return True
        return False
    
    def __getitem__(self, key):
        value = 0
        len_set = set()
        for item in self.dl:
            for k in item:
                if k not in len_set:
                    len_set.add(k)
        if key not in len_set:
            raise KeyError
        for item in self.dl:
            for k_item in item.keys():
                if key == k_item:
                    value = item[k_item]
        return value
    
    def __setitem__(self, key, value):
        len_set = set()
        for item in self.dl:
            for k in item:
                if k not in len_set:
                    len_set.add(k)
        if key not in len_set:
            new_dict = dict()
            new_dict[key] = value
            self.dl.append(new_dict)
         
        highest_index = 0
        for i in range(len(self.dl)):
            highest_index = i
        for d in self.dl[highest_index]:
            if key in d:
                d[key] = value
        
#         highest_index = 0 
#         count = 0     
#         for d in self.dl[1]:
#             if key in d:
#                 count = 0
#         for d in self.dl[1:]:
#             count += 1
#             if key in d:
#                 highest_index = count
#         for d in self.dl[highest_index]:
#             if key in d:
#                 d[key] = value
        
                
                
        
    def __call__(self, key):
        call_dict = []
        index = 0
        if key in self.dl[0]:
            call_dict.append((index, self.dl[0][key]))
        for item in self.dl[1:]:
            index += 1
            if key in item:
                call_dict.append((index, item[key]))
        return call_dict
    
    def __iter__(self):
        pass
    
    def __eq__(self, right):
        if type(right) == DictList:
            self_list = list()
            for item in self.dl:
                for key in item:
                    self_list.append(key)
            right_list = list()
            for item in right.dl:
                for key in item:
                    right_list.append(key)
            self_set = set(self_list)
            right_set = set(right_list)
            if self_set == right_set:
                for item in self.dl:
                    for r_item in right.dl:
                        if item != r_item:
                            return False
                

            return False
        
    def __add__(self, right):
        pass




            
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
