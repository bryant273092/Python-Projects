from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self,*args):
        self.dl = []
        assert len(args) >= 1, 'Arguments must include 1 or more dictionaries.'
        for i in args:
            if type(i) == dict:
                self.dl.append(i)
            else:
                raise AssertionError('{i} is not a dictionary.'.format(i=i))
            
    def __len__(self):
        counter = 0
        keys = []
        for d in self.dl:
            for key in d:
                if key not in keys:
                    keys.append(key)
                    counter += 1
        return counter
    
    def __repr__(self):
        middle_str = ""
        for d in self.dl:
            middle_str += (str(d) + ", ")
        middle_str = middle_str.strip(", ")
        return "DictList("+ middle_str + ")"
    
    def __contains__(self, item):
        for d in self.dl:
            if item in d.keys():
                return True
            
    def __getitem__(self, item):
        result = None
        is_in = False
        for d in self.dl:
            if item in d.keys():
                is_in = True
                result = d[item]
        if is_in == False:
            raise KeyError('{item} appears in no dictionaries.'.format(item=item))
        else:
            return result
    
    def __setitem__(self,k,v):
        is_in = False
        highest = 0
        for index in range(len(self.dl)):
            if k in self.dl[index].keys():
                is_in = True
                highest = index
        if is_in == True:
            self.dl[highest].update({k:v})
        else:
            self.dl.append({k:v})
    
    def __call__(self,k):
        result = []
        for index in range(len(self.dl)):
            if k in self.dl[index].keys():
                result.append((index,self.dl[index][k]))
        return result
    
    def __iter__(self):
        keys = []
        indexes = []
        result = []
        for index in range(len(self.dl)):
            indexes.append(index)
        indexes = sorted(indexes, reverse = True)
        for i in indexes:
            for k in self.dl[i].keys():
                if k not in keys:
                    keys.append(k)
                    result.append((k, self.dl[i][k]))
        for tup in result:
            yield tup
            
    def __eq__(self, right):
        keys_self = set()
        counter = 0
        for d in self.dl:
            for key in d.keys():
                if key not in keys_self:
                    keys_self.add(key)
        if type(right) in [DictList, dict]:
            if type(right) == DictList:
                keys_right = set()
                for d in right.dl:
                    for key in d.keys():
                        if key not in keys_right:
                            keys_right.add(key)
            if type(right) == dict:
                keys_right = set()
                for key in right.keys():
                    if key not in keys_right:
                        keys_right.add(key)
        
            if keys_self == keys_right:
                for key in keys_self:
                    if self[key] == right[key]:
                        counter += 1
            if counter == len(keys_self):
                return True
            else:
                return False     
        else:
            raise TypeError('Right argument must be a DictList or dictionary.')
        
    def __add__(self,right):
        keys = []
        left_d = dict()
        right_d = dict()
        for d in self.dl:
            for k in d.keys():
                if k not in keys:
                    keys.append(k)
        for k in keys:
            left_d.update({k:self[k]})
        keys = []
        for d in right.dl:
            for k in d.keys():
                if k not in keys:
                    keys.append(k)
        for k in keys:
            right_d.update({k:self[k]})
        return DictList(left_d,right_d)
        
        

        
        


            
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
