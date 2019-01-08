from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl=[]
        assert len(args)!=0, "DictList requires at least one dict argument, none was inputted"
        for dict_arg in args:
            assert type(dict_arg)==dict, f"Invalid argument: must be type dict, but {dict_arg} was {type_as_str(dict_arg)}"
            self.dl.append(dict_arg)
    def __len__(self):
        all_keys = set()
        for dict_arg in self.dl:
            for key in dict_arg:
                all_keys.add(key)
        return len(all_keys)
    def __repr__(self):
        list_str = str(self.dl).replace('[', "")
        return f"DictList({list_str.replace(']', '')})"
    def __contains__(self, item):
        return any([item in dict_arg for dict_arg in self.dl])
    def __getitem__(self, item):
        answer_index = None
        for dict_arg in self.dl:
            if item in dict_arg:
                if answer_index == None:
                    answer_index = self.dl.index(dict_arg)
                else:
                    if self.dl.index(dict_arg)>answer_index:
                        answer_index = self.dl.index(dict_arg)
        if answer_index == None:
            raise KeyError(f"Invalid Key: {item}, not in DictList") 
        return self.dl[answer_index][item]
    def __setitem__(self, key, item):
        maxed = -1
        while maxed >= -(len(self.dl)):
            if key in self.dl[maxed]:
                self.dl[maxed][key]=item
                maxed = None
                break
            else:
                maxed -=1
        if maxed != None:
            self.dl.append({key:item})
    def __call__(self, item):
        answer_ls = []
        for dict_arg in self.dl:
            if item in dict_arg:
                answer_ls.append((self.dl.index(dict_arg), dict_arg[item]))  
        return answer_ls
    def __iter__(self):
        maxed = -1
        found_set = set()
        while maxed >= -(len(self.dl)):
            for key in self.dl[maxed]:
                if key not in found_set:
                    yield (key, self.dl[maxed][key])
                    found_set.add(key)
            maxed -= 1
    def __eq__(self, right):
        if type_as_str(right) not in ("exam.DictList", "dict"):
            raise TypeError(f"Invalid comparison: {right}, must be DictList or dict but was {type_as_str(right)}")
        dl_set=self.dl_as_set(self)
        if type_as_str(right)=="exam.DictList":
            right_set = self.dl_as_set(right)
            if dl_set == right_set:
                return all([right[key]==self[key] for key in right_set])
            else:
                return False
        if type(right)==dict:
            if set(right.keys())==dl_set:
                return all([right[key]==self[key] for key in right])
            else:
                return False                      
                
    def __add__(self, right):
        if type_as_str(right)=="exam.DictList":
            dl_set = self.dl_as_set(self)
            new_dl = {}
            right_set=self.dl_as_set(right)
            new_right = {}
            for key in dl_set:
                new_dl[key]=self[key]
            for key in right_set:
                new_right[key]=right[key]
            return DictList(new_dl, new_right)
                
            
        
        
    def dl_as_set(self, dl):
        dl_set = set()
        for dict_arg in dl:
            dl_set.add(dict_arg[0])
        return dl_set


            
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
