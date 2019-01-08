from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        assert len(args) != 0, "empty"
        self.dl = []
        for arg in args:
            assert type(arg) == dict, "DictList.__init__:'{}' is not a dictionary.".format(arg)
            self.dl.append(arg)
    
    def __len__(self):
        counter = 0
        iterated = []
        for dickt in self.dl:
            for key in dickt:
                if key not in iterated:
                    iterated.append(key)
                    counter += 1
        return counter
    
    def __repr__(self):
        as_str = 'DictList('
        for dickt in self.dl:
            as_str += str(dickt) + ', '
        as_str = as_str[:-2] + ')'
        return as_str 
                
    def __contains__(self, matcher):
        for dickt in self.dl:
            for key in dickt:
                if key == matcher:
                    return True
        return False

    def __getitem__(self, getted):
        inthere = False
        for dickt in self.dl:
            for key in dickt:
                if key == getted:
                    final_val = dickt[key]
                    inthere = True
        if not inthere:
            raise KeyError('DictList.__getitem__: key not in there')
        return final_val
    
    def __setitem__(self, keye, val):
        index = -1
        inthere = False
        for dickt in self.dl:
            index += 1
            for key in dickt:
                if key == keye:
                    final_index = index
                    inthere = True
        if inthere:
            self.dl[final_index][keye] = val
        else:
            self.dl.append({keye: val})
    
    def __call__(self, keye):
        dexval_list = []
        index = -1
        for dickt in self.dl:
            index += 1
            for key in dickt:
                if key == keye:
                    dexval_list.append((index, dickt[key]))
        return dexval_list
    
    def __iter__(self):
        reversed = self.dl.copy()
        reversed.reverse()
        iterated = []
        
        for dickt in reversed:
            for key in sorted(dickt):
                if key not in iterated:
                    iterated.append(key)
                    yield (key, dickt[key])
                    
    def __eq__(self, compared): 
        keys_self = set()
        for dickt in self.dl:
            for key in dickt:
                keys_self.add(key)
                
        if type(compared) == type(self):
            keys_compared = set()
            for dickie in compared.dl:
                for keye in dickie:
                    keys_compared.add(keye)
            
            if keys_self == keys_compared:
                for kei in keys_self:
                    if self[kei] == compared[kei]:
                        pass
                    else:
                        return False
                return True
            else:
                return False
        elif type(compared) == dict:
            keys_compared = set()
            for key in compared:
                keys_compared.add(key)
            
            if keys_self == keys_compared:
                for kei in keys_self:
                    if self[kei] == compared[kei]:
                        pass
                    else:
                        return False
                return True
            else:
                return False
             
        else:
            raise TypeError('DictList.__eq__: That is not a DictList or dict type!')
        
    def __add__(self, adder):
        self_final_dict = {}
        
        for dickt in self.dl:
            for key in dickt:
                self_final_dict[key] = self[key]
        
        if type(adder) == type(self):
            adder_final_dict = {}
            for dickt in adder.dl:
                for key in dickt:
                    adder_final_dict[key] = adder[key]
                    
            return DictList(self_final_dict, adder_final_dict)
            
            
            
        elif type(adder) == dict:
            return DictList(self_final_dict, adder.copy())
        else:
            raise TypeError('DictList.__add__: That is not a DictList or dict type!')
    
    def __radd__(self, adder):
        self_final_dict = {}
        
        for dickt in self.dl:
            for key in dickt:
                self_final_dict[key] = self[key]
                
        if type(adder) == dict:
            return DictList(adder.copy(), self_final_dict)
        else:
            raise TypeError('DictList.__add__: That is not a DictList or dict type!')
            
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
