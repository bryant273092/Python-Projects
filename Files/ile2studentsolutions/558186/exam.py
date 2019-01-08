from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        assert len(args) > 0
        for arg in args:
            assert type(arg) == dict
            self.dl.append(arg)
            
    def __len__(self) -> int:
        result = 0
        unique = set()
        for d in self.dl:
            for key in d:
                if key not in unique:
                    unique.add(key)
                    result += 1
        return result

    def __repr__(self) -> str:
        return f"DictList({', '.join([str(d) for d in self.dl])})"
    
    def __contains__(self, item) -> bool:
        for d in self.dl:
            if item in d:
                return True
        return False
    
    def __getitem__(self, key):
        for i in range(len(self.dl) - 1, -1, -1):
            if key in self.dl[i]:
                return self.dl[i][key]
        raise KeyError(f"{key} appears in no dictionaries")
    
    def __setitem__(self, key, value):
        for i in range(len(self.dl) - 1, -1, -1):
            if key in self.dl[i]:
                self.dl[i][key] = value
                return
        self.dl.append({key:value})
        
    def __call__(self, key) -> [tuple]:
        result = []
        for i in range(len(self.dl)):
            if key in self.dl[i]:
                result.append((i, self.dl[i][key]))
        return result
    
    def __iter__(self):
        def dl_list(dl) -> list:
            result = []
            unique = set()
            for i in range(len(dl) - 1, -1, -1):
                for k, v in sorted(dl[i].items()):
                    if k not in unique:
                        unique.add(k)
                        result.append((k, v))
            return result
        
        def dl_gen(dl):
            for d in dl:
                yield d
                
        return dl_gen(dl_list(self.dl))
    
    def __eq__(self, right) -> bool:
        if type(right) == DictList:
            for d in self.dl:
                for key in d:
                    if not right.__contains__(key):
                        return False
                    if self.__getitem__(key) != right.__getitem__(key):
                        return False
            for d in right.dl:
                for key in d:
                    if not self.__contains__(key):
                        return False
                    if right.__getitem__(key) != self.__getitem__(key):
                        return False
            return True
        elif type(right) == dict:
            for d in self.dl:
                for key in d:
                    if key not in right:
                        return False
                    if self.__getitem__(key) != right[key]:
                        return False
            for key in right:
                if not self.__contains__(key):
                    return False
                if right[key] != self.__getitem__(key):
                    return False
            return True
        else:
            raise TypeError(f"right={right} must be type DictList or dict not type {type_as_str(right)}")
        
    def __add__(self, right):
        if type(right) == DictList:
            arg1, arg2 = {}, {}
            for d in self.dl:
                for key in d:
                    arg1[key] = self.__getitem__(key)
            for d in right.dl:
                for key in d:
                    arg2[key] = right.__getitem__(key)
            return DictList(arg1, arg2)   
        elif type(right) == dict:
            arg1 = {}
            for d in self.dl:
                for key in d:
                    arg1[key] = self.__getitem__(key)
            return DictList(arg1, dict(right))
        else:
            raise TypeError(f"right={right} must be type DictList or dict not type {type_as_str(right)}")
        
    def __radd__(self, left):
        if type(left) == dict:
            arg2 = {}
            for d in self.dl:
                for key in d:
                    arg2[key] = self.__getitem__(key)
            return DictList(dict(left), arg2)
        else:
            raise TypeError(f"left={left} must be type DictList not type {type_as_str(left)}")

            
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
