from goody import type_as_str  # Useful in some exceptions
from _collections_abc import ItemsView
from pip._vendor.html5lib.treebuilders.base import ActiveFormattingElements

class DictList:
    def __init__(self,*dicts):
        self.dl = []
        for items in dicts:
            if type(items) == dict:
                self.dl.append(items)
            else:
                if type(items) != dict:
                    raise AssertionError
    def __len__(self):
        answer = []
        for items in self.dl:
            for elements in items.keys():
                if elements not in answer:
                    answer.append(elements)
        return len(answer)
    def __repr__(self):
        answer = ''
        for elements in self.dl:
            answer += str(elements)
        return 'DictList(' + answer + ')'
    
    def __contains__(self,key):
        final = []
        for items in self.dl: 
            for elements in items.keys():
                final.append(elements)
        if key in final:
            return True
        else:
            return False
    def __getitem__(self,key):
        final = []
        for elements in self.dl:
            for items in elements.items():
                if key == items[0]:
                    final.append(items[1])
        return final[-1]
    
    def __setitem__(self,k,v):
        final = {}
        for elements in self.dl:
            for items in elements.keys():
                if k == items:
                    elements[k] = v
                else:
                    final[k] = v
                    
    
    def __call__(self,key):
        pass
        '''for elements in self.dl:
            for items in elements.items():
                if key == items[0]:
                    final_2 = elements[key]'''
                    
   
                
                    
                    
                    
               
                  

        




            
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
