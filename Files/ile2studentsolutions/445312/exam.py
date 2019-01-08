from goody import type_as_str  # Useful in some exceptions
from _hashlib import new
#from pygame.tests.test_utils.png import reversed

class DictList:
    def __init__(self,*args):
        self.dl = []
        if len(args) == 0 or len(args) == 1 and type(args[0]) is not dict:
            raise AssertionError
        for element in args:
            #print(element)
            if type(element) is not dict:
                raise AssertionError(element + 'is not a dictionary')
            self.dl.append(element)
    
    def __len__(self):
        answer = []
        answer_len = 0
        for every_dict in self.dl:
            for every_key in every_dict:
                answer.append(every_key)
        
        answer_len = len(set(answer))
        return answer_len
                
    def __repr__(self): 
        temp = ''
        temp_list = []
        for each_dict in self.dl:
            for each_key in each_dict:
                temp += each_key + '=' + str(each_dict[each_key]) + ','
            temp_list.append(temp)
            
        new_temp = ','.join(x for x in tuple(temp_list))
        return 'DictList(' + tuple(new_temp) + ')'   
    
    def __contains__(self, looking_key):   
        for each_dict in self.dl:
            for key in each_dict.keys():
                if key == looking_key:
                    return True
        return False     
    
    def __getitem__(self, looking_key):
        key_list = []
        for each_dict in reversed(self.dl):
            for every_key in each_dict:
                key_list.append(every_key)
        if looking_key not in key_list:
            raise KeyError
        for each_dict in reversed(self.dl):
            for every_key in each_dict:
                if every_key == looking_key:
                    return each_dict[looking_key]
                
    def __setitem__(self, looking_key, set_value):
        #print(looking_key, set_value)
        changed_list = []
        for each_dict in reversed(self.dl):
            for every_key in each_dict:
                if every_key == looking_key and every_key not in changed_list:
                    each_dict[looking_key] = set_value
                    changed_list.append(every_key)
        
        key_list = []
        for each_dict in reversed(self.dl):
            for every_key in each_dict:
                key_list.append(every_key)
        
        if looking_key not in key_list:
            self.dl.append({looking_key:set_value})
        
        
    def __call__(self, looking_key):
        key_list = []
        answer_list = []
        for each_dict in reversed(self.dl):
            for every_key in each_dict:
                key_list.append(every_key)
        if looking_key not in key_list:
            return []
        
        for counter, each_dict in enumerate(self.dl):
            for every_key in each_dict:
                if every_key == looking_key:
                    answer_list.append((counter, each_dict[every_key]))
        
        return answer_list
    
    def __iter__(self):
        changed_list = []
        answer_list = []
        for each_dict in reversed(self.dl):
            for every_key in each_dict:
                if every_key not in changed_list:
                    answer_list.append((every_key, each_dict[every_key]))
                    changed_list.append(every_key)
        
        answer = iter(answer_list)
        
        for i in answer:
            yield i
                    
        
    def __eq__(self, compare_obj):   

        key_list = []
        for each_dict in reversed(self.dl):
            for every_key in each_dict:
                key_list.append(every_key)
        compare_obj_key_list = []
        if type(compare_obj) == DictList:
            for each_dict in compare_obj.dl:
                for every_key in each_dict:
                    compare_obj_key_list.append(every_key)
            if compare_obj_key_list == list(set(key_list)):
                return True
        
        if type(compare_obj == DictList):
            for each_dict in self.dl:
                for every_key in each_dict:
                    if every_key in compare_obj_key_list and self.__getitem__(every_key) != compare_obj.__getitem__(every_key):
                        return False
            return True
        elif type(compare_obj) == dict:
            for each_dict in self.dl:
                for every_key in each_dict:
                    if every_key in compare_obj.keys() and self.__getitem__(every_key) != compare_obj[every_key]:
                        return False
            return True

        
        
        
        #for each_dict in 
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    #a = DictList(dict(a=1,b=3,c=3))
    #b = DictList(dict(a=1,b=3,c=3))
 

    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
