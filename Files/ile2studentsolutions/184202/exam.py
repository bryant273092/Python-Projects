

class DictList:
    def __init__(self, *args):
        if len(args) == 0:
            raise AssertionError
        for a in args:
            assert type(a) is dict, "DictList.__init__: {} is not a dictionary".format(str(a))
        self.dl = []
        for a in args: 
            self.dl.append(a)
            
    def __len__(self):
        dl_set = set()
        for d in self.dl:
            for k in d:
                dl_set.add(k)
        return len(dl_set)
    
    def __repr__(self):
        dl_string = ""
        dl_string += ", ".join(str(dl) for dl in self.dl)
        return "DictList(" + dl_string + ")"
    
    def __contains__(self, key):
        for dl in self.dl:
            if key in dl.keys():
                return True
            
    def __getitem__(self, key):
        for dl in self.dl:
            if key in dl.keys():
                index_num = self.dl.index(dl)
            else:
                raise KeyError
            return self.dl[index_num][key] 
    
    
    def __setitem__(self, key, value):
        for dl in self.dl:
            if key not in dl:
                new_dict = {}
                new_dict[key] = value
                self.dl.append(new_dict)
            else:
                index_num = self.dl.index(dl)
                self.dl[index_num][key] = value

    
    def __call__(self, key):
        dl_list = []
        for dl in self.dl:
            if key in dl:
                dl_list.append((self.dl.index(dl), dl[key]))
        return dl_list
                 

    def __iter__(self):
        for dl in self.dl:
            for k in dl:
                yield (k, dl[k])
                
    def __eq__(self, dict2):
        if type(dict2) is DictList:
            return self.dl == dict2.dl
        elif type(dict2) is dict:
            for d in self.dl:
                return d.keys() == dict2.keys()
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
