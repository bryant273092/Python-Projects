from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self, *args):
        self.dl = []
        if len(args) != 0:
            for item in args:
                if type(item) == dict:
                    self.dl.append(item)
                else:
                    raise AssertionError (f"'{item}' is not of type dict")
        else:
            raise AssertionError(f"No dictionaries were found")
        
        
    def __len__(self):
        answer_set = set()
        for item in self.dl:
            for key in item.keys():
                answer_set.add(key)
        return len(answer_set)
    
    
    def __repr__(self):
        answer = f"DictList("
        for item in self.dl:
            answer += f"{str(item)}, "
        answer = answer[:-1]
        answer += ')'
        return answer
    
    
    def __contains__(self, arg):
        for item in self.dl:
            for key in item.keys():
                if key == arg:
                    return True
        return False


    def __getitem__(self, arg):
        all_keys = set()
        for item in self.dl:
            for k in item.keys():
                all_keys.add(k)
        if arg not in all_keys:
            raise KeyError(f"'{arg}' appears in no dictionaries")    
        backward_list = []
        for i in range(len(self.dl)):
            backward_list.append(self.dl[-(i+1)])
        for b_item in backward_list:
            if arg in b_item.keys():
                return b_item[arg]
            
            
    def __setitem__(self, k, v):
        all_keys = set()
        for item in self.dl:
            for key in item.keys():
                all_keys.add(key)
                
        backward_list = []
        for i in range(len(self.dl)):
            backward_list.append(self.dl[-(i+1)])  
            
        if k in all_keys:
            for item in backward_list:
                for key in item.keys():
                    if k == key:
                        item[k] = v
                        return 
        else:
            self.dl.append({k:v})
        

    def __call__(self, k):
        answer = []
        for num,item in enumerate(self.dl):
            for key in item.keys():
                if k == key:
                    answer.append((num, item[k]))
        return answer
    
    
    def __iter__(self):
        backward_list = []
        for i in range(len(self.dl)):
            backward_list.append(self.dl[-(i+1)])
        
        check_set = set()
        for item in backward_list:
            for key in item:
                if key not in check_set:
                    yield (key, item[key])
                    check_set.add(key)
                
    
    def __eq__(self, other):
        self_set = set()
        for item in self.dl:
            for k in item.keys():
                self_set.add(k)

        value_list = []
        for something in self_set:
            value_list.append((something,self.__getitem__(something)))
            
        if type(other) == type(self):
            other_set = set()
            for item in other.dl:
                for k in item.keys():
                    other_set.add(k)

            for key in other_set:
                if key not in self_set:
                    return False
            for s in self_set:
                if s not in other_set:
                    return False
            
            ovalues = []
            for ov in other_set:
                ovalues.append((ov, other.__getitem__(ov))) 
                
            for o in ovalues:
                if o not in value_list:
                    return False
            for vv in value_list:
                if vv not in ovalues:
                    return False
                return True

        
        elif type(other) == dict:
            for key in other.keys():
                if key not in self_set:
                    return False
            for s in self_set:
                if s not in other.keys():
                    return False
                
            for tup in other.items():
                if tup not in value_list:
                    return False
            return True
        
        else:
            raise TypeError(f"'{other}' is not of type dict or DictList")
        
                  
            
            
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
