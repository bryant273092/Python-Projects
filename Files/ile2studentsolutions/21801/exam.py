

class DictList:

    def __init__(self, *dictl):
        self.dl = []
        if len(dictl) == 1:
            if type(dictl) != {}:
                raise AssertionError('not a dict')
            else:
                self.dl = [dictl]
        if len(dictl) > 1:
            for x in dictl:
                if type(x) != {}:
                    raise AssertionError('not a dict')
            self.dl = [dictl]

    
    def __len__(self):
        suml = 0
        for x in self.dl:
            for i in x.keys():
                
                if i == x:
                    suml += 1
        return sum
    
    
    def __repr__(self):
        if len(self.dl) == 1:
            return 'DictList{}'.format(self.dl)
        if len(self.dl) > 1:
            for x in self.dl:
                return 'DictList{}'.format(x)
    
    def __contains__(self,key):
        if len(self.dl) == 1:
            for x in self.dl.keys():
                if x == key:
                    return True
        else:
            
            for x in self.dl:
                for i in x.keys():
                    if i == key:
                        return True
        return False
    
    def __getitem__(self, key):
        temp_list = []
        if len(self.dl) == 1:
            for x in self.dl.keys():
                if x == key:
                    return x 
                else:
                    return KeyError('key not in dict')
        if len(self.dl) >1:
            for x in self.dl:
                for i in x.keys():
                    if i == key:
                        temp_list.append(i)
            if temp_list == []:
                raise KeyError('key not in dict')
            else:
                return temp_list[-1]
        raise KeyError('key not in dict')
    
    
    
                    
                        
    
    
    def __eq__(self, right):
        if type(right) != DictList or type(right) != dict:
            raise TypeError('right not a dictlist or a dict')
                




            
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
