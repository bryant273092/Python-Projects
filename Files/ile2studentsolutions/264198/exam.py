

class DictList:
    
    def __init__(self, *args):
        for val in args:
            if type(val) != dict:
                raise AssertionError("Argument must be a dictionary value.")
        if len(args) == 0:
            raise AssertionError("Cannot be an empty dictionary.")
        else:
            self.dl = args

    
    def __len__(self):
        dist_keys = set()
        for i in self.dl:
            for k in i:
                dist_keys.add(k)
        return len(dist_keys)
     
    def __repr__(self):
        return("DictList" + str(self.dl))
        
     
    def __contains__(self, duplicate):
        l = []
        for i in self.dl:
            for k in i:
                l.append(k)
        if duplicate in l:
            return True
        else:
            return False
     
    def __getitem__(self, wanted_key):
        new_d = {}
        l = []
        for d in self.dl:
            for k, v in d.items():
                new_d[k] = v
                l.append(k)
        for i in new_d:
            if wanted_key == i:
                return new_d[wanted_key]
            if wanted_key not in l:
                raise KeyError

     
    def __setitem__(self, k, v):
#         new_d = {}
        """
        d = {'a': 1, 'b': 2, 'c': 3}
            {'c': 13, 'd': 14, 'e': 15}
            {'e': 25, 'f': 26, 'g': 27}
        """
        for d in self.dl:
            for letter, number in d.items():
                if k in d:
                    d[k] = v
#                 else:
#                     new_d[k] = v
#                     d = d + new_d
    
#     
#     def __call__(self):
#         pass
#     
#     def __iter__(self):
#         pass
#     
#     def __eq__(self, right):
#         pass



            
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
