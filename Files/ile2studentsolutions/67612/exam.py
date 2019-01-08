from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*d):
        self.dl = []
        if len(d) == 0:
            raise AssertionError
        for di in d:
            if not(type(di) is dict):
                raise AssertionError
            self.dl.append(di)
    
    def __len__(self):
        distinct_keys = set()
        for d in self.dl:
            for key in d:
                distinct_keys.add(key)
        return len(distinct_keys)
    
    def __repr__(self):
        return f"DictList({', '.join([str(d) for d in self.dl])})"
    
    def __contains__(self, item):
        for d in self.dl:
            if item in d:
                return True
        return False
    
    def __getitem__(self, item):
        dl_keys = set()
        for d in self.dl:
            for k in d.keys():
                dl_keys.add(k)
        if item not in dl_keys:
            raise KeyError
        else:
            index = 0
            for d in self.dl:
                if item in d:
                    index = self.dl.index(d)
        return self.dl[index][item]
    
    def __setitem__(self, key, value):
        dl_keys = set()
        for d in self.dl:
            for k in d.keys():
                dl_keys.add(k)
        if key not in dl_keys:
            self.dl.append({key: value})
        else:
            index = 0
            for d in self.dl:
                if key in d:
                    index = self.dl.index(d)
            self.dl[index][key] = value
        
    def __call__(self, item):
        dl_keys = set()
        for d in self.dl:
            for k in d.keys():
                dl_keys.add(k)
        if item not in dl_keys:
            return []
        else:
            return_list = []
            for d in self.dl:
                if item in d:
                    return_list.append((self.dl.index(d), d[item]))
            return return_list
    
    def __eq__(self, right):
        if type_as_str(right) not in ['dict', 'exam.DictList']:
            raise TypeError
        elif type_as_str(right) == 'exam.DictList':
            return self.dl == right.dl
        else:
            dl_keys = set()
            for d in self.dl:
                for k in d.keys():
                    dl_keys.add(k)
            if dl_keys != set(right.keys()):
                return False
            else:
                return_bool = []
                for key in right:
                    return_bool.append(self.__getitem__(key) == right[key])
                return all(return_bool)
   
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
