from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *many_dicts):
        self.dl = []
        if len(many_dicts) == 0:
            raise AssertionError
        for d in many_dicts:
            if not type(d) is dict:
                raise AssertionError
            else:
                self.dl.append(d)

    def __len__(self):
        temp_s = set()
        for d in self.dl:
            for j in d:
                temp_s.add(j)
        return len(temp_s)

    def __repr__(self):
        string = 'DictList('
        for d in self.dl:
            string += str(d) + ', '
        string = string[:-2]
        string += ')'
        return string
    
    def __contains__(self, key):
        for d in self.dl:
            if key in d.keys():
                return True
        return False
    
    def __getitem__(self, key):
        temp = None
        for d in self.dl:
            if key in d.keys():
                temp = d[key]
        if temp != None:
            return temp
        else:
            raise KeyError
        
    def __setitem__(self, key, value): 
        changed = False
        for i in range(len(self.dl)-1, -1, -1):
            if key in self.dl[i] and changed == False:
                self.dl[i][key] = value
                changed = True
        
        if changed == False:
            self.dl.append({key:value})  

    def __call__(self, key):
        listt = []
        for i in range(0, len(self.dl)):
            if key in self.dl[i]:
                listt.append((i, self.dl[i][key]))
        return listt
    
    def __iter__(self):
        temp_s = set()
        for i in range(len(self.dl)-1, -1, -1):
            for j in sorted(self.dl[i]):   
                if not j in temp_s:
                    yield (j, self.__getitem__(j))
                temp_s.add(j)
                
    def __eq__(self, d2):
        if type(d2) is DictList:
            key_set1 = set()
            for d in self.dl:
                for key in d:
                    key_set1.add(key)
            key_set2 = set()
            for d in d2.dl:
                for key in d:
                    key_set2.add(key)
            if key_set1 != key_set2:
                return False
        
            for key in key_set1:
                if self[key] != d2[key]:
                    return False
                
            return True
        elif type(d2) is dict:
            key_set1 = set()
            for d in self.dl:
                for key in d:
                    key_set1.add(key)
            
            key_set2 = set()
            for key in d2:
                key_set2.add(key)
                
            if key_set1 != key_set2:
                return False
        
            for key in key_set1:
                if self[key] != d2[key]:
                    return False
            
            return True
            
        else:
            raise TypeError
    
    def __add__(self, d2):
        if type(d2) is DictList:
            
            first_d = {}
            for d in self.dl:
                for key in d:
                    first_d[key] = d[key]
            
            second_d = {}
            for d in d2.dl:
                for key in d:
                    second_d[key] = d[key]
        
            return DictList(first_d, second_d)
         
        elif type(d2) is dict:
            d_list = []
            for d in self.dl:
                
                new_d = {}
                for key in d:
                    new_d[key] = d[key]
                d_list.append(new_d)
                
            
            copy_d = {}
            for key in d2:
                copy_d[key] = d2[key]
            
            d_list.append(copy_d)
            return DictList(*d_list)
        
        else:
            raise TypeError
        
    def __radd__(self, d2):
        
        if type(d2) is dict:
            d_list = []
            
            copy_d = {}
            for key in d2:
                copy_d[key] = d2[key]
            
            d_list.append(copy_d)
            
            for d in self.dl:
                
                new_d = {}
                for key in d:
                    new_d[key] = d[key]
                d_list.append(new_d)
                
            return DictList(*d_list)
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
