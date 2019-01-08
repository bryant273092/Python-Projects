

class DictList:
    
    def __init__(self, *args):
        assert len(args) != 0, 'DictList must be initialized with dictionaries'
        self.dl = []
        for this_dict in args:
            assert type(this_dict) is dict, 'DictList.__init__: ' + str(this_dict) + 'is not a dictionary'
            self.dl.append(this_dict)
    
    def __len__(self):
        helper_set = set()
        for this_dict in self.dl:
            for this_key in this_dict:
                helper_set.add(this_key)
        return len(helper_set)
    
    def __repr__(self):
        ret_str = 'DictList('
        count = 1
        for this_dict in self.dl:
            if count != len(self.dl):
                ret_str += "{" + '{}'.format(','.join(["'"+str(k)+"':"+str(v) for k,v in this_dict.items()])) + '},'
            else:
                ret_str += "{" + '{}'.format(','.join(["'"+str(k)+"':"+str(v) for k,v in this_dict.items()])) + '}'
            count += 1
        ret_str += ')'
        return ret_str
    
    def __contains__(self, item):
        for this_dict in self.dl:
            for this_key in this_dict:
                if this_key == item:
                    return True
        return False
    
    def __getitem__(self, item):
        ret_val = None
        for this_dict in self.dl:
            for this_key, val in this_dict.items():
                if this_key == item: #will reset if it ever finds another key later on
                    ret_val = val
        if(ret_val):
            return ret_val
        else:
            raise KeyError(str(item) + 'appears in no dictionaries')
            
    def __setitem__(self, item, value):
        if item in self:
            count = 0
            for this_dict in self.dl:
                if item in this_dict:
                    last_index = count
                count += 1
            self.dl[last_index][item] = value
        else:
            added_dict = {}
            added_dict[item] = value
            self.dl.append(added_dict)
    
    def __call__(self, item):
        ret_list = []
        if item in self:
            this_index = 0
            for this_dict in self.dl:
                if item in this_dict:
                    ret_list.append((this_index, self.dl[this_index][item]))
                this_index += 1
        return ret_list
    
    #my own functions
    def all_keys(self):
        helper_set = set()
        for this_dict in self.dl:
            for this_key in this_dict:
                helper_set.add(this_key)
        return helper_set
        
            
    def __iter__(self):
        def dictlist_gen(dl):
            yield_list = []
            for k in dl.all_keys():
                yield_list.append((k, self[k]))
            for this_tup in sorted(yield_list, key = lambda x: (-self(x[0])[-1][0], x[0])):
                yield this_tup
        return dictlist_gen(self)
    
    def __eq__(self, right):
        if type(right) is DictList:
            same_keys = sorted(list(self.all_keys())) == sorted(list(self.all_keys()))
            if(same_keys):
                return all([self[k] == right[k] for k in self.all_keys()])
            else:
                return False
        elif type(right) is dict:
            same_keys = sorted(list(self.all_keys())) == sorted(right.keys())
            if(same_keys):
                return all([self[k] == right[k] for k in right.keys()])
            else:
                return False
        else:
            raise TypeError('can only comper DictList and DictList or Dictlist and dict')
            
            
                
                             




            
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
