from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *kargs):
        self.dl = []
        if kargs ==():
            raise AssertionError(f'DictList.__init__: {kargs} is not a dictionary')
        for instance in kargs:
            if type(instance) == dict:
                self.dl.append(instance)
            elif type(instance) != dict:
                raise AssertionError(f'DictList.__init__: {instance} is not a dictionary')
        
    def __len__(self):
        unique = [] 
        for d in self.dl:
            for key in d.keys():
                if key not in unique:
                    unique.append(key)
        return len(unique)
    
    def __repr__(self):
        str_d='DictList('
        return str_d
    
    def __contains__(self, item):
        for d in self.dl:
            for key in d.keys():
                if key == item:
                    return True
        return False
    
    def __setitem__(self, item, val):
        self.dl.append(dict(item=val))

    
    def __call__(self, item):
        ref = []
        index = 0
        for d in self.dl:
            for key,value in d.items():
                if key == item:
                    ref.append((index, value))
            index += 1
        return ref
    
    def __iter__(self):
        tup_list = []
        for d in self.dl[-1:]:
            temp_list = [] 
            for key, value in d.items():
                temp_list.append((key,value))
            tup_list.extend(sorted(temp_list, key=lambda x: x[0]))
        return iter(tup_list)
                
    



            
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
