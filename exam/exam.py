import prompt                          # for driver, which prompts user
from collections import defaultdict    # use if you want (see problem descriptions)

# You might use the following abbreviations (or their full names)
#   for the various parts of the Warehouse database

# i    : inventory (how many products are available)
# p    : product
# w    : warehouse


def read_db (openfile : open) -> {str:{str:int}}:
    inv_dict = defaultdict(dict)
    for i in openfile.readlines():
        split_items = i.strip('\n').split(":")
        new_item = split_items.pop(0)
        while split_items: 
            inv_dict[split_items.pop(0)][new_item] = eval(split_items.pop(1))
    return dict(inv_dict)


        
def inventory (db : {str:{str:int}}) -> [(str,int)]:
    new_list= []
    for dict1 in db:
        for item, quantity in db[dict1].items():
            if new_list:
                count = 0
                for item1 in new_list:
                    if item == item1[0]:
                        quantity += item1[1]
                        new_list[count] = tuple([item, quantity])
                        break
                    count +=1   
                else:
                    new_list.append(tuple([item, quantity]))  
            else: 
                new_list.append(tuple([item, quantity])) 
    return sorted(new_list, key = (lambda value : value[1]), reverse = True)
def resupply (db : {str:{str:int}}, must_have : int) -> {str: {(str,int)}}:
    re_up = defaultdict(set)
    for city in db:
        for item, quantity in db[city].items():
                if must_have-quantity > 0:
                    re_up[item].add(tuple([city, must_have-quantity]))
    return(re_up)


            
def update_purchases (db : {str:{str:int}}, purchases : [(str,str)] ) -> {(str,str)}:
    failed_list = set()
    for sale in purchases:
        city, item = sale[0], sale[1]
        if city in db and sale[1] in db[city]:
            if db[city][sale[1]]> 0:
                db[city][sale[1]] -= 1 
            else:
                failed_list.add(tuple([city,item]))
        else:
            failed_list.add(tuple([city,item]))
    return failed_list
def product_locations(db : {str:{str:int}}) -> [(str,[(str,int)])]:
    re_up = defaultdict(list)
    for city in db:
        for item, quantity in db[city].items():
            re_up[item].append(tuple([city,quantity]))
    new_list = []
    for item, cities in sorted(re_up.items()):
        new_list.append(tuple([item, cities]))
    return new_list
def unique_supplier (db : {str:{str:int}}) -> {str:{str}}:
    new_dict = defaultdict(set)
    for city in db:
        for item, quantity in db[city].items():
            for cities in db:
                if item in db[cities] and cities != city:
                    break
            else:
                new_dict[city].add(item)
                
                
                    
             
    return new_dict


 
def talk(alist : [int]) -> [int]:
    pass

 
 
if __name__ == '__main__':
#     import driver
#     driver.driver()

    # You can add any of your own specific testing code here
    # You can comment-out tests after your code passes them (but don't change your code!)
     
    # checks whether answer is correct, printing appropriate information
    # Note that dict/defaultdict will compare == if they have the same keys and
    #   associated values, regardless of the fact that they print differently
    def check (answer, correct):
        if (answer == correct):
            print ('    CORRECT')
        else:
            print ('    INCORRECT')
            print ('      was       =',answer)
            print ('      should be =',correct)
        print()
 
  
    # These tests are similar to those that the driver will execute for batch self-checks
    # To run a test, enter True (or just press enter); to skip a test, enter False 
         
    if prompt.for_bool('Test read_db?', True): 
        db = 'db1.txt'
        answer = read_db(open(db))
        print('  db =',db,'\n  read_db =',answer)
        check(answer, {'Irvine':  {'brush': 3,    'comb': 2,    'wallet': 2},
                       'Newport': {'comb': 1,     'stapler': 0},
                       'Tustin' : {'keychain': 3, 'pencil': 4,  'wallet': 3}})


        db = 'db2.txt'
        answer = read_db(open(db))
        print('  db =',db,'\n  read_db =',answer)
        check(answer, {'Irvine':  {'brush': 4, 'comb': 2, 'keychain': 6, 'lipgloss': 3, 'wallet': 3},
                       'Newport': {'brush': 1, 'comb': 5, 'keychain': 3, 'lipgloss': 6, 'wallet': 1},
                       'Tustin':  {'brush': 1, 'comb': 3, 'keychain': 2, 'lipgloss': 4, 'wallet': 2}})

    ##################################################
              

    if prompt.for_bool('Test inventory?', True): 
        db = {'Irvine':  {'brush': 3,    'comb': 2,    'wallet': 2},
              'Newport': {'comb': 1,     'stapler': 0},
              'Tustin' : {'keychain': 3, 'pencil': 4,  'wallet': 3}}

        answer = inventory(db)
        print('  db =',db,'\n  inventory =',answer)
        check(answer, [('wallet', 5), ('pencil', 4), ('brush', 3), ('comb', 3), ('keychain', 3), ('stapler', 0)])

 
        db = {'Irvine':  {'brush': 4, 'comb': 2, 'keychain': 6, 'lipgloss': 3, 'wallet': 3},
              'Newport': {'brush': 1, 'comb': 5, 'keychain': 3, 'lipgloss': 6, 'wallet': 1},
              'Tustin':  {'brush': 1, 'comb': 3, 'keychain': 2, 'lipgloss': 4, 'wallet': 2}}

        answer = inventory(db)
        print('  db =',db,'\n  inventory =',answer)
        check(answer, [('lipgloss', 13), ('keychain', 11), ('comb', 10), ('brush', 6), ('wallet', 6)])

 
    ##################################################
              

    if prompt.for_bool('Test resupply?', True): 
        db = {'Irvine':  {'brush': 3,    'comb': 2,    'wallet': 2},
              'Newport': {'comb': 1,     'stapler': 0},
              'Tustin' : {'keychain': 3, 'pencil': 4,  'wallet': 3}}

        answer = resupply(db,3)
        print('  db =',db,'\n  resupply =',answer)
        check(answer, {'comb': {('Newport', 2), ('Irvine', 1)}, 'wallet': {('Irvine', 1)}, 'stapler': {('Newport', 3)}})

 
        db = {'Irvine':  {'brush': 4, 'comb': 2, 'keychain': 6, 'lipgloss': 3, 'wallet': 3},
              'Newport': {'brush': 1, 'comb': 5, 'keychain': 3, 'lipgloss': 6, 'wallet': 1},
              'Tustin':  {'brush': 1, 'comb': 3, 'keychain': 2, 'lipgloss': 4, 'wallet': 2}}

        answer = resupply(db,4)
        print('  db =',db,'\n  resupply =',answer)
        check(answer, {'comb': {('Tustin', 1), ('Irvine', 2)}, 'lipgloss': {('Irvine', 1)}, 'wallet': {('Tustin', 2), ('Newport', 3), ('Irvine', 1)}, 'brush': {('Tustin', 3), ('Newport', 3)}, 'keychain': {('Tustin', 2), ('Newport', 1)}})

 
    ##################################################
    
         
    if prompt.for_bool('Test update_purchases?', True): 
        db = {'Irvine':  {'brush': 3,    'comb': 2,    'wallet': 2},
              'Newport': {'comb': 1,     'stapler': 0},
              'Tustin' : {'keychain': 3, 'pencil': 4,  'wallet': 3}}
        purchases = [('Irvine', 'brush'), ('Newport','comb'), ('Tustin', 'car'), ('Newport', 'comb')]

        answer = update_purchases(db,purchases)
        print('  db =',db,'\n  update_purchases =',answer)
        check(answer, {('Tustin', 'car'), ('Newport', 'comb')})
        print('  db mutated =',db)
        check(db, {'Irvine':  {'brush': 2,    'comb': 2,    'wallet': 2},
                   'Newport': {'comb': 0,     'stapler': 0},
                   'Tustin' : {'keychain': 3, 'pencil': 4,  'wallet': 3}})

        
        db = {'Irvine':  {'brush': 4, 'comb': 2, 'keychain': 6, 'lipgloss': 3, 'wallet': 3},
              'Newport': {'brush': 1, 'comb': 5, 'keychain': 3, 'lipgloss': 6, 'wallet': 1},
              'Tustin':  {'brush': 1, 'comb': 3, 'keychain': 2, 'lipgloss': 4, 'wallet': 2}}
        purchases = [('Santa-Ana','brush'), ('Tustin', 'brush'), ('Newport','keychain'), ('Newport', 'food'), ('Tustin', 'brush')]

        answer = update_purchases(db,purchases)
        print('  db =',db,'\n  update_purchases =',answer)
        check(answer, {('Newport', 'food'), ('Santa-Ana','brush'),('Tustin', 'brush')})
        print('  db mutated =',db)
        check(db, {'Irvine':  {'brush': 4, 'comb': 2, 'keychain': 6, 'lipgloss': 3, 'wallet': 3},
                   'Newport': {'brush': 1, 'comb': 5, 'keychain': 2, 'lipgloss': 6, 'wallet': 1},
                   'Tustin':  {'brush': 0, 'comb': 3, 'keychain': 2, 'lipgloss': 4, 'wallet': 2}})

        
    ##################################################
   
         
    if prompt.for_bool('Test product_locations?', True): 
        db = {'Irvine':  {'brush': 3,    'comb': 2,    'wallet': 2},
              'Newport': {'comb': 1,     'stapler': 0},
              'Tustin' : {'keychain': 3, 'pencil': 4,  'wallet': 3}}


        answer = product_locations(db)
        print('  db =',db,'\n  product_locations =',answer)
        check(answer, [('brush', [('Irvine', 3)]),
                       ('comb', [('Irvine', 2), ('Newport', 1)]),
                       ('keychain', [('Tustin', 3)]),
                       ('pencil', [('Tustin', 4)]),
                       ('stapler', [('Newport', 0)]),
                       ('wallet', [('Irvine', 2), ('Tustin', 3)])])
 
 
        db = {'Irvine':  {'brush': 4, 'comb': 2, 'keychain': 6, 'lipgloss': 3, 'wallet': 3},
              'Newport': {'brush': 1, 'comb': 5, 'keychain': 3, 'lipgloss': 6, 'wallet': 1},
              'Tustin':  {'brush': 1, 'comb': 3, 'keychain': 2, 'lipgloss': 4, 'wallet': 2}}


        answer = product_locations(db)
        print('  db =',db,'\n  product_locations =',answer)
        check(answer,  [('brush', [('Irvine', 4), ('Newport', 1), ('Tustin', 1)]),
                        ('comb', [('Irvine', 2), ('Newport', 5), ('Tustin', 3)]),
                        ('keychain', [('Irvine', 6), ('Newport', 3), ('Tustin', 2)]),
                        ('lipgloss', [('Irvine', 3), ('Newport', 6), ('Tustin', 4)]),
                        ('wallet', [('Irvine', 3), ('Newport', 1), ('Tustin', 2)])])
 
 
    ##################################################
              

    if prompt.for_bool('Test unique_supplier?', True): 
        db = {'Irvine':  {'brush': 3,    'comb': 2,    'wallet': 2},
              'Newport': {'comb': 1,     'stapler': 0},
              'Tustin' : {'keychain': 3, 'pencil': 4,  'wallet': 3}}
        answer = unique_supplier(db)
        print('  db =',db,'\n  unique_supplier =',answer)
        check(answer, {'Irvine': {'brush'}, 'Newport': {'stapler'}, 'Tustin': {'pencil', 'keychain'}})

        
        db = {'Irvine':  {'brush': 4, 'comb': 2, 'keychain': 6,                'wallet': 3},
              'Newport': {            'comb': 5, 'keychain': 3, 'lipgloss': 6, 'wallet': 1},
              'Tustin':  {            'comb': 3, 'keychain': 2,                'wallet': 2}}


        answer = unique_supplier(db)
        print('  db =',db,'\n  unique_supplier =',answer)
        check(answer, {'Irvine':{'brush'}, 'Newport': {'lipgloss'}})
 
 
 
    ##################################################
              

    if prompt.for_bool('Test talk?', True): 
        arg = [1,2,1,1]
        answer = talk(arg)
        print('  arg =',arg,'\n  talk =',answer)
        check(answer, [1,1,1,2,2,1])


        arg = [1,1,1,2,2,1]
        answer = talk(arg)
        print('  arg =',arg,'\n  talk =',answer)
        check(answer, [3,1,2,2,1,1])
 
 
