from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        assert len(args) > 0
        for arg in args:
            assert type(arg) == dict
        self.dl = [a for a in args]
        
    def __len__(self):
        result = set()
        for d in self.dl:
            for key in d:
                result.add(key)
        return len(result)
    
    def __repr__(self):
        list_of_dicts_as_str = [str(d) for d in self.dl]
        dict_str = ','.join(list_of_dicts_as_str)
        return "DictList({})".format(dict_str)
    
    def __contains__(self, target):
        for dictionary in self.dl:
            for key in dictionary:
                if key == target:
                    return True
        return False
    
    def __getitem__(self, target):
        result = None
        for dictionary in self.dl:
            for pair in dictionary.items():
                if pair[0] == target:
                    result = pair[1]
        if result != None:
            return result
        else:
            raise KeyError("{} key not found in DictList object.".format(str(target)))
        
    def __setitem__(self,n_key,n_val):
        found = False
        
        target_index = None
        for dict_index in range(len(self.dl)):
            for key in self.dl[dict_index]:#look through keys in dict obj
                if key == n_key:
                    target_index = dict_index
                    #self.dl[dict_index][key] = n_val
                    found = True
                    
        if found == False:
            to_add = {}
            to_add[n_key] = n_val
            self.dl.append(to_add)
        else:
            self.dl[target_index][n_key] = n_val
            
    def __call__(self,target):
        result = []
        for dict_index in range(len(self.dl)):
            for pair in self.dl[dict_index].items():
                if pair[0] == target:
                    to_add = (dict_index,pair[1])
                    result.append(to_add)
        return result
    
    def __iter__(self):
        result = []
        
        for dict_index in range(len(self.dl)):
            dict_family = []
            for pair in self.dl[dict_index].items():
                dict_family.append(pair)
            result.append(dict_family)
            
        result = result[::-1]
        temp_result = []
        for sub_list in result:
            temp_result.append(sorted(sub_list))
        #temp_result is a list of lists where
        #each sublist is the dictionary in increasing index order
        #now we need to remove duplicates
        
        for sub_list in temp_result:
            for pair in sub_list:
                searching = pair
                for sub_list2 in temp_result:
                    for pair2 in sub_list2:
                        if (searching[0] == pair2[0]) and (searching[1]!=pair2[1]):
                            sub_list2.remove(pair2)
        final_res = []
        for sl in temp_result:
            for pair in sl:
                final_res.append(pair)
        for i in final_res:
            yield i

                
    def __eq__(self,r_val):
        if type(r_val) not in (dict,DictList):
            raise TypeError("{} must be of type dict or DictList".format(str(r_val)))
        
        len_bool = len(r_val) == len(self)
        
        if type(r_val) == dict:
            all_matched = True
            for key in r_val:
                if r_val[key] != self[key]:
                    all_matched = False
            return all_matched and len_bool
        
        elif type(r_val) == DictList:
            all_matched = True
            for pair in r_val:
                if pair[0] not in self:
                    all_matched = False
                elif self[pair[0]] != pair[1]:
                    all_matched = False
            return all_matched
        
    def __radd__(self,r_val):
        if type(r_val) not in (dict,DictList):
            raise TypeError("{} must be of type dict or DictList".format(str(r_val)))
        
        if type(r_val) == DictList:
            try:
                self_dict = {}
                for pair in self:
                    self_dict[pair[0]] = pair[1]
                
                r_dict = {}
                for pair in r_val:
                    r_dict[pair[0]] = pair[1]
                return DictList(self_dict,r_dict)
            except:
                return None

        elif type(r_val) == dict:
            return DictList(r_val, *self.dl)
            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    #x = [{'a':1},{'b':2},{'c':3}]
    #y = [str(d) for d in x]
    #print(y)
    #z = ','.join(y)
    #print(z)

    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
