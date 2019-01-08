from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        if len(args) == 0:
            raise AssertionError("The dictionary can't be empty")
        for i in args:
            if type(i) is not dict:
                raise AssertionError(str(i)+'is not a dictionary')
        self.dl  = [a for a in args]
        
    def __len__(self):
        result = []
        for i in self.dl:
            for j in i.keys():
                if j not in result:
                    result.append(j)
        return len(result)
    
    def __repr__(self):
        return 'DictList(' + ','.join([str(i) for i in self.dl]) + ')'

    def __contains__(self, a):
        result = False
        for i in self.dl:
            for j in i.keys():
                if a == j:
                    result = True
        return result
    
    def __getitem__(self, k):
        if k not in self:
            raise KeyError(str(k) + 'appears in no dictionaries')
        for i in self.dl:
            for j in i.keys():
                if j == k:
                    result = i[j]
        return result

    def __setitem__(self, k, v):
        if k not in self:
            self.dl.append({k:v})
        else:
            for index in range(len(self.dl)):
                if k in self.dl[index]:
                    t = index
            self.dl[t][k] = v
            
    def __call__(self, k):
        if k not in self:
            return []
        else:
            result = []
            for i in range(len(self.dl)):
                if k in self.dl[i]:
                    result.append((i, self.dl[i][k]))
            return result
        
    def __iter__(self):
        key_list = []
        for i in self.dl:
            for j in i.keys():
                key_list.append(j)
        key_set = set(key_list)
        if len(self.dl) != 1:         
            k = self.dl
            k.reverse()
            for i in k:
                for j in i.keys():
                    if j in key_set:
                        yield (j, i[j])
                        key_set.remove(j)
        elif len(self.dl) == 1:
            for i in self.dl:
                for j in i.keys():
                    yield (j, i[j])

    def __eq__(self, right):
        if type(right) not in [dict, DictList]:
            raise TypeError(str(right) + 'has to be a DictList or dictionary')
        
        if type(right) is dict:
            if len([i for i in self]) == len([(k,v) for k,v in right.items()]):
                result = True
                for t in [i for i in self]:
                    if t not in [(k,v) for k,v in right.items()]:
                        result = False
                return result
            else:
                return False
            
        if type(right) is DictList:
            if len([i for i in self]) == len([j for j in right]):
                result = True
                
                for k in [i for i in self]:
                    if k not in [j for j in right]:
                        result = False
                return result
            else:
                return False
      
    def __req__(self, left):
        return self == left   
          
   
        
            


            
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
