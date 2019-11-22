#Submitter: bryanth1(Hernandez, Bryant)
from goody import type_as_str
import inspect

class Check_All_OK:
    """
    Check_All_OK class implements __check_annotation__ by checking whether each
      annotation passed to its constructor is OK; the first one that
      fails (by raising AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self,check,param,value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (by raising AssertionError) this classes raises AssertionError and prints
      its failure, along with a list of all annotations tried followed by the
      check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self,check,param,value,check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 



class Check_Annotation:
    # Below, setting the class attribute to True allows checking to occur
    #   (but only if self._checking_on is also True)
    checking_on  = True
  
    # set self._checking_on to True too, for checking the decorated function 
    def __init__(self, f):
        self._f = f
        self._checking_on = True
        
    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):
        print('check this: ',self, param, annot,value)
        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        def check_None():
            pass
        def check_type():
            if not isinstance(value, annot):
                raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))
        def check_list():
            #check if it is an instance
            if not isinstance(value, type(annot)):
                raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))
            
            print(type(annot[0]), type(lambda annot:annot))
            #check if list is nested
            if type(value[0]) in [list, tuple]:
                #if nested, check all value types are in annotation types
                
                
                nested_values = [type(i) for list in value for i in list]
                nested_annot = [x for x in annot[0]]
                for value_type in nested_values:
                    if value_type not in nested_annot:
                        raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))
                        
                    
                #then check if all annotation types correspond with value types
                for annot_type in nested_annot:
                    if annot_type not in nested_values:
                        raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))    
            #if nested lambda fucntion
            
            elif type(annot[0]) == type(lambda annot:annot):
                check_lambda()
               
            #if not nested
            else:
                for i in value:
                    if type(i) not in annot and type(i) != tuple:
                        raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))
                value_types = list([type(i) for i in value])
                for i in annot:
                    if i not in value_types:
                        raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))        
        def check_tuple():
            #check if it is an instance
            if not isinstance(value, type(annot)):
                raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))
            
            
            #check if tuple is nested
            if type(value[0]) in [tuple, list]:
                #if nested, check all value types are in annotation types
                
                
                nested_values = [type(i) for tuple in value for i in tuple]
                nested_annot = [x for x in annot[0]]
                for value_type in nested_values:
                    if value_type not in nested_annot:
                        raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))
                        
                    
                #then check if all annotation types correspond with value types
                for annot_type in nested_annot:
                    if annot_type not in nested_values:
                        raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))    
               
            #if not nested
            else:
                for i in value:
                    if type(i) not in annot:
                        raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))
                value_types = list([type(i) for i in value])
                for i in annot:
                    if i not in value_types:
                        raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))
#                 if not isinstance(value, type(annot)):
#                     raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))
#                 
#                 for i in value:
#                     if type(i) not in annot:
#                         raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))
#                 value_types = list([type(i) for i in value])
#                 for i in annot:
#                     if i not in value_types:
#                         raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))       
        def check_dict():
            if not isinstance(value, type(annot)):
                raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))
            #check keys, elements are corresponding
            for key, element in value.items():
                if type(key) not in annot.keys() or type(element) not in annot.values():
                    raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))
            
            
            
            
            
            for i in value:
                if type(i) not in annot:
                    raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))
            value_types = list([type(i) for i in value]) 
            for i in annot:
                if i not in value_types:
                    raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))       
        def check_set():
            if not isinstance(value, type(annot)):
                raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))
            for i in value:
                if type(i) not in annot:
                    raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))
            value_types = list([type(i) for i in value])
            for i in annot:
                if i not in value_types:
                    raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))          
        def check_frozenset():
            if not isinstance(value, type(annot)):
                raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))
            for i in value:
                if type(i) not in annot:
                    raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))
            value_types = list([type(i) for i in value])
            for i in annot:
                if i not in value_types:
                    raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))       
        def check_lambda():
            if not param or len(param)> 1:
                raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))       

            try:
                if type(value) == list:
                    for i in value:
                        if not annot[0](i):
                            raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))      
                elif not annot(value):
                    raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))      

            except:
                raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))      
        def check_str():
            try:
                if not eval(value):
                    raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))      
            except:
                raise AssertionError("'{param}' failed annotation check(wrong type): value = {value} was type {type} ... should be type {annot}".format(param = param, value = value, type = type(value), annot =  annot))      
                
        if annot is None:
            check_None()
        elif annot in [list,tuple, dict, set, frozenset, type(lambda annot:annot),str]:
            check_type()
        elif type(annot) == list:
            check_list()
        elif type(annot) == tuple:
            check_tuple()
        elif type(annot) == dict:
            check_dict()
        elif type(annot) == set:
            check_set()
        elif type(annot) == frozenset:
            check_frozenset()
        elif type(annot) == type(lambda annot:annot): 
            check_lambda()
        elif type(annot) == str:
            check_str()
        else:
            check_type()
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)

        # Below, decode check function's annotation; check it against arguments
        
    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
    def __call__(self, *args, **kargs):
        
        # Return a dictionary of the parameter/argument bindings (actually an
        #    ordereddict, storing the function header's parameters in order)
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if not (param.name in bound_f_signature.arguments):
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments

        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        # Otherwise do all the annotation checking
        if not self._checking_on or not self.checking_on:
            return self._f(*args, *kargs)
        func_annot = self._f.__annotations__  
        bindings= param_arg_bindings()
        print('funcannot:', func_annot)
        print('bindings', bindings)
        
        try:
            # Check the annotation for all parameters (if there are any)
            for param in func_annot.keys():
                if param != 'return':
                    self.check(param, func_annot[param], bindings[param])
            dec_func = self._f(*args, *kargs)
            if 'return' in func_annot.keys():
                bindings['_return'] = dec_func
                self.check('return', func_annot['return'], bindings['_return'])
                   
            # Compute/remember the value of the decorated function
            
            # If 'return' is in the annotation, check it
            
            # Return the decorated answer
            
        #remove after adding real code in try/except
            
        # On first AssertionError, print the source lines of the function and reraise 
        except AssertionError:
#             print(80*'-')
#             for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
#                 print(l.rstrip())
#             print(80*'-')
            raise 



  
if __name__ == '__main__':     
    # an example of testing a simple annotation  
#     def f(x:int)-> int: return x
#     f = Check_Annotation(f)
#     f(3)
#     f('a')
#     def f(x:int): pass
#     f = Check_Annotation(f)
#     f(3)
#     f('a')
#     def f(x : [int,str]): 
#         pass
#     f = Check_Annotation(f)
#     f([1,'b'])
#     f([1])
   
#     def f(x : [[str]]): 
#         pass
#     f = Check_Annotation(f)
#     f([['a','b'],['c','d']])        
#     def f(x : [int]): 
#         pass
#     f = Check_Annotation(f)
#     f([1,2])
#     def f(x : [(str,)]): 
#         pass
#     f = Check_Annotation(f)
#     f([('a','b'),('c','d')])
#     def f(x : ([str],)): 
#         pass
#     f = Check_Annotation(f)
#     f((['a','b'],['c','d']))
#     def f(x : ([str],)): 
#         pass
#     f = Check_Annotation(f)
#     f((['a','b'],['c','d']))
#     def f(x : {str : int}): 
#         pass
#     f = Check_Annotation(f)
#     f({'a':1,'b':2})
#     def f(x : lambda x : x >= 0): 
#         pass
#     f = Check_Annotation(f)
#     f(3)
#     def f(x : [lambda x : x >= 0]): 
#         pass
#     f = Check_Annotation(f)
#     f([0,1,0])
#     def f(x : None)->int: 
#         return x
#     f = Check_Annotation(f)
#     f(3)
    #driver tests
    import driver
    driver.default_file_name = 'bscp4F18.txt'
#     driver.default_show_exception= True
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()
