from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*dic):
        self.dl = []
        if len(dic) == 0:
            raise AssertionError
        for ele in dic:
            if type(ele) != dict:
                raise AssertionError("DictList.__init__: 'abc' is not a dictionary")
            else:
                self.dl.append(ele)
        
    
    def __len__(self):
        key = set()
        for i in self.dl:
            key.update(i.keys())
        return len(key)
    
    def __repr__(self):
        for i in range(len(self.dl)):
            return 'DictList('+(str(self.dl[i])+', ')+')'
        
    def __contains__(self,item):
        for ele in self.dl:
            if item in ele.keys():
                return True
            
    def __getitem__(self,item):
        all_value = []
        key = set()
        for ele in self.dl:
            key.update(ele.keys())
        if item not in key:
            raise KeyError("attribute in no dictionaries")
        for ele in self.dl:
            if item in ele:
                all_value.append(ele[item])
        return all_value[-1]
            
    def __setitem__(self,k,v):
        find_index = -1
        key = set()
        for ele in self.dl:
            key.update(ele.keys())
        if k not in key:
            self.dl.update({k:v})
        for ele in self.dl:
            if k in ele:
                find_index += 1
        self.dl[find_index][k] = v
    
    def __call__(self,item):
        result = []
        key =set()
        for ele in self.dl:
            key.update(ele.keys())
        if item not in key:
            return []
        for i in range(len(self.dl)):
            if item in self.dl[i]:
                result.append((i,self.dl[i][item]))
        return result
                
    def __iter__(self):
        for ele in range(-len(self.dl)):
            for i in range(-len(self.dl)):
                if self.dl[ele].keys() not in self.dl[i+1].keys():
                    yield (self.dl[ele])
    
    def __eq__(self,right):
        left = set()
        right = set()
        if type(right) is DictList:
            print(1)
            for ele in self.dl:
                    for item in right:
                        left.update(ele.keys())
                        right.update(ele.keys())
        print(left)
        if type(right) == DictList:
            print(1)
            if left == right:
                for ele in self.dl:
                    for item in right:
                        for key1,key2 in left, right:
                            if ele[key1] == ele[key2]:
                                return True
            else:
                return False
                
            
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
