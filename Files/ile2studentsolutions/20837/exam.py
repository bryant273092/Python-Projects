from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*dictionaries):
        self.dl =[]
        if len(dictionaries) == 0:
            raise AssertionError('one or more dictionaries was not supplied')
        for thing in dictionaries:
            if type(thing) is not dict:
                raise AssertionError('DictList.__init: argument is not a dictionary')
            else:
                self.dl.append(thing)
    def __len__(self):
        result = set()
        for dictionary in self.dl:
            for k in dictionary.keys():
                result.add(k)
        return len(result)
    def __repr__(self):
        dict_string = str(self.dl)
        dict_string_sliced = dict_string[1:-1]
        result = 'DictList({})'.format(dict_string_sliced)
        return result
    def __contains__(self,argument):
        for dictionary in self.dl:
            if argument in dictionary.keys():
                return True
    def __getitem__(self,argument):
        try:
            for dictionary in self.dl:
                if argument in dictionary.keys():
                    result = dictionary[argument]
            return result
        except UnboundLocalError:
            raise KeyError
    def __setitem__(self,item,value):
        
        all_keys = []
        for dictionary in self.dl:
            for key in dictionary.keys():
                all_keys.append(key)  
        
        if item not in all_keys:
            dict_to_append = {item:value}
            self.dl.append(dict_to_append)
            
        else: #if the item is currently in one of the dictionaries
            for dictionary in self.dl[::-1]:
                if item in dictionary.keys():
                    dictionary[item] = value
                    break
    def __call__(self,item):
        result = []
        for index in range(len(self.dl)):
            if item in self.dl[index].keys():
                result.append((index,self.dl[index][item]))
        return result
    def __iter__(self):
        keys_to_produce = set()
        for dictionary in self.dl:
            for key in dictionary.keys():
                keys_to_produce.add(key) 
    
        for dictionary in self.dl[::-1]:
            for letter in dictionary.keys():
                if letter in keys_to_produce:
                    yield (letter,dictionary[letter])
                    keys_to_produce.remove(letter)
    def __eq__(self,right):
        if type(right) is DictList:
            left_keys = set()
            right_keys = set()
            for dictionary in self.dl:
                for key in dictionary.keys():
                    left_keys.add(key)
            for dictionary in right.dl:
                for key in dictionary.keys():
                    right_keys.add(key)
            if left_keys != right_keys:
                return False
            equal_values = True
            try:
                for key in left_keys:
                    if self[key] != right[key]:
                        equal_values = False
                if (equal_values and left_keys == right_keys):
                    return True
                return False
            except KeyError:
                return False
        elif type(right) is dict:
            left_keys = set()
            for dictionary in self.dl:
                for key in dictionary.keys():
                    left_keys.add(key)
            same_keys = (len(left_keys) == len(right.keys()))
            try:
                for key in left_keys:
                    if self[key] != right[key]:
                        return False
                if same_keys:
                    return True
            except KeyError:
                return False
        else:
            raise TypeError
    
    def __add__(self,right):
        dict_copy = right.copy()
        dict_list_copy = self.dl.copy()
        result = DictList()
        result_dl = dict_list_copy.append(dict_copy)
        result.dl = result_dl
        return result
            
            
             
        
            
        
        
        
        
            

    


            
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
