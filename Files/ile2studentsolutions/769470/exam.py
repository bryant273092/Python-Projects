
# Written by Jules Labador - 11.29.2018
# ICS 33

class DictList:
    
    def __init__(self, *dicts):
        
        self.dl = []
                
        for d in dicts:
                                    
            if isinstance(d, dict) or type(d) == dict:
                self.dl.append(d)
            
            else:
                raise AssertionError(f"{d} is not a dictionary. It is a {type(d)}")
        
        if not dicts:
            raise AssertionError("Please specify (a) dictionary/dictionaries to initialize.")
        
        
        
    def __len__(self):
        
        distinct = set()
        
        for d in self.dl:
            for key in d.keys():
                distinct.add(key)
                
        counter = 0
        for _ in distinct:
            counter += 1
        
        return counter
    
    
    
    def __repr__(self):
        
        dictionaries = ""
        
        for e, d in enumerate(self.dl):
            if e != len(self.dl) - 1:
                dictionaries += str(d) + ", "
            
            else:
                dictionaries += str(d)

        return f"DictList({dictionaries})"
    
    
    
    def __contains__(self, item):
        
        for d in self.dl:
            for key in d.keys():
                if item == key:
                    return True
                
        return False
    
    
    
    def __getitem__(self, item):
        
        newest = None
                        
        for d in self.dl:
            for key, value in d.items():
                if item == key:
                    newest = value
                
        if newest != None:
            return newest
        
        raise KeyError(f"{item} appears in no dictionaries")
    
    
    
    def __setitem__(self, item, new_value):
        
        value_changed = False
                        
        for d in sorted(self.dl, key = lambda x : -self.dl.index(x)):
            for key in d.keys():
                if item == key:
                    if value_changed == False:
                        d[item] = new_value
                        value_changed = True
                    
        if value_changed == False:
            self.dl.append({item: new_value})
            
            
            
    def __call__(self, item):
        
        calls = []
        
        for i, d in enumerate(self.dl):
            for (k, v) in d.items():
                if item == k:
                    calls.append((i, v))
        
        return calls
    
    
    
    def __iter__(self):
        
        seen = set()
        
        for d in sorted(self.dl, key = lambda x : -self.dl.index(x)):
            for k, v in sorted(d.items(), key = lambda x : x[1]):
                if not k in seen:
                    yield (k, v)
                    seen.add(k)
                    
                    
                
    def __eq__(self, right):
        
        if isinstance(right, DictList):
            self_dictionary = {}
            right_dictionary ={}
            
            for d in self.dl:
                for k, v in d.items():
                    self_dictionary[k]= v
                    
            for d in right.dl:
                for k, v in d.items():
                    right_dictionary[k]= v
            
            if self_dictionary == right_dictionary:
                return True
            
            return False
            
        elif isinstance(right, dict):
            self_dictionary = {}
            
            for d in self.dl:
                for k, v in d.items():
                    self_dictionary[k]= v
                    
            if self_dictionary == right:
                return True
            
            return False
            
        else:
            raise TypeError(f"{self} is not equal to {right}")
        
        
        
    def __add__(self, right):
        
        result = DictList({})
        
        if isinstance(right, DictList):
             
            for d in self.dl:
                for k, v in d.items():
                    result.__setitem__(k, v)
                     
            for d in right.dl:
                for k, v in d.items():
                    result.__setitem__(k, v)
             
            return result
         
        elif isinstance(right, dict):
            
            for d in self.dl:
                for k, v in d.items():
                    result.__setitem__(k, v)
                    
            for k, v in right.items():
                result.__setitem__(k, v)
                
            return result
            
        else:
            raise TypeError()
        
        
        
    def __radd__(self, left):
        
        result = DictList({})
        
        if isinstance(left, DictList):
            
            for d in left.dl:
                for k, v in d.items():
                    result.__setitem__(k, v)
             
            for d in self.dl:
                for k, v in d.items():
                    result.__setitem__(k, v)            
             
            return result
         
        elif isinstance(left, dict):
            
            for k, v in left.items():
                result.__setitem__(k, v)
            
            for d in self.dl:
                for k, v in d.items():
                    result.__setitem__(k, v)
                    
            return result
            
        else:
            raise TypeError()
            
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
