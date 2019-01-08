#Submitter: bryanth1(Hernandez, Bryant)

# Generators must be able to iterate through any kind of iterable.
# hide is present and called to ensure that your generator code works on
#   general iterable parameters (not just a string, list, etc.)
# For example, although we can call len(string) we cannot call
#   len(hide(string)), so the generator functions you write should not
#   call len on their parameters
# Leave hide in this file and add code for the other generators.

def hide(iterable):
    for v in iterable:
        yield v


# The combination of return and yield None make each of the following
#   a generator (yield None) that immediately raises the StopIteration
#   exception (return)

def sequence(*iterables):
    for i in iterables:
        for j in i:
            yield j 
            
def group_when(iterable,p):
    list_match = []
    list_count = 0
    for i in iterable:
        list_match.append(i)
        if p(i):
            old_list = list_match
            list_match = []
            yield old_list
    if list_match:
        yield list_match
def drop_last(iterable, n):
    #need to know why I cant create copies of iterables, withoutaffecting the other iterables, while being able to know its position
    z = iter(iterable)
    last_five = []
    while True:
        try: 
            for i in range(n+1 - len(last_five)):
                last_five.append(next(z))
            yield last_five.pop(0)
        except StopIteration:
            return None
def yield_and_skip(iterable,skip):
    z = iter(iterable)
    is_true = True
    while True:
        for i in z:
            try: 
                for j in range(skip(i)):
                    next(z)
            except StopIteration:
                is_true = False
                
            yield i
        return None           
        
def alternate_all(*args):
    is_true = True
    arg_list = [iter(i) for i in args]
    to_remove = []
    while is_true:
        if not arg_list:
            is_true = False
            return None  
        for i in range(len(arg_list)):
            try: 
                next1 = next(arg_list[i])
                yield next1
            except StopIteration:
                to_remove.append(arg_list[i])
        if to_remove:
            for i in to_remove:
                try:
                    arg_list.remove(i)
                except:
                    pass



def min_key_order(adict):
    passed_keys = [0]
    is_true = True
    while is_true:
        try: 
            current_keys = sorted(adict)
            for key in current_keys:      
                if key not in passed_keys and key in adict:
                    if passed_keys[-1]<key:
                        passed_keys.append(key)
                        looking = False
                        yield (key, adict[key])
            else:
                if not looking:
                    break 
        except RuntimeError:
            pass
        except StopIteration:
            is_true = False
            return None
    return None
        

 
           
         
if __name__ == '__main__':
    from goody import irange
#     
    #Test sequence; you can add any of your own test cases
    print('Testing sequence')
    for i in sequence('abc', 'd', 'ef', 'ghi'):
        print(i,end='')
    print('\n')
    print(''.join([v for v in drop_last('combustible', 5)]))
    for i in drop_last('combustible', 5):
        print(i)
 
    print('Testing sequence on hidden')
    for i in sequence(hide('abc'), hide('d'), hide('ef'), hide('ghi')):
        print(i,end='')
    print('\n')
  
  
    # Test group_when; you can add any of your own test cases
    print('Testing group_when')
    for i in group_when('combustibles', lambda x : x in 'aeiou'):
        print(i,end='')
    print('\n')
  
    print('Testing group_when on hidden')
    for i in group_when(hide('combustibles'), lambda x : x in 'aeiou'):
        print(i,end='')
    print('\n')
  
  
    # Test drop_last; you can add any of your own test cases
    print('Testing drop_last')
    for i in drop_last('combustible', 5):
        print(i,end='')
    print('\n')
  
    print('Testing drop_last on hidden')
    for i in drop_last(hide('combustible'), 5):
        print(i,end='')
    print('\n')
  
  
    # Test sequence; you can add any of your own test cases
    print('Testing yield_and_skip')
    for i in yield_and_skip('abbabxcabbcaccabb',lambda x : {'a':1,'b':2,'c':3}.get(x,0)):
        print(i,end='')
    print('\n')
          
    # Test min_key_order; add your own test cases
#     print('\nTesting Ordered')
#     d = {1:'a', 2:'x', 4:'m', 8:'d', 16:'f'}
#     i = min_key_order(d)
#     print(next(i))
#     print(next(i))
#     del d[8]
#     print(next(i))
#     d[32] = 'z'
#     print(next(i))
#     print(next(i))
#      


         
         
    import driver
    driver.default_file_name = "bscq4F18.txt"
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
    
