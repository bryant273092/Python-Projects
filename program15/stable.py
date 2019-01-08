#Submitter: bryanth1(Hernandez, Bryant)
import prompt
import goody
import copy

# Use these global variables to index the list associated with each name in the dictionary.
# e.g., if men is a dictionary, men['m1'][match] is the woman who matches man 'm1', and 
# men['m1'][prefs] is the list of preference for man 'm1'.
# It would seems that this list might be better represented as a named tuple, but the
# preference list it contains is mutated, which is not allowed in a named tuple. 

match = 0   # Index 0 of list associate with name is match (str)
prefs = 1   # Index 1 of list associate with name is preferences (list of str)


def read_match_preferences(open_file : open) -> {str:[str,[str]]}:
    person_dict = {}
    for person in open_file.readlines():
        person1 = person.strip('\n').split(';')
        person_dict[person1.pop(0)] = [None, person1]
    return(person_dict)
    


def dict_as_str(d : {str:[str,[str]]}, key : callable=None, reverse : bool=False) -> str:
    str_dict = ''
    for x in sorted(d.keys(),key = key,  reverse = reverse):
        str_dict += '  ' + x + ' -> ' + str(d[x]) + '\n'
    return(str_dict)
        


def who_prefer(order : [str], p1 : str, p2 : str) -> str:
    value_list = [p1, p2]
    for preference in order:
        if preference in value_list:
            return preference


def extract_matches(men : {str:[str,[str]]}) -> {(str,str)}:
    return({tuple((person, men[person][0])) for person in men.keys()})
    

def make_match(men : {str:[str,[str]]}, women : {str:[str,[str]]}, trace : bool = False) -> {(str,str)}:   
    temp_dict= copy.deepcopy(men)
    unmatched = set()
    for man in temp_dict.keys():
        unmatched.add(man)  
    while bool(unmatched):
        man = unmatched.pop()
        preferred = temp_dict[man][1].pop(0)
        matched_w = [person [0] for person in temp_dict.values()]
        if preferred not in matched_w:
            temp_dict[man][0] = preferred
        elif preferred in matched_w:
            for key in temp_dict.keys():
                if temp_dict[key][0] == preferred:
                    preferred_male = who_prefer(women[preferred][1],man, key)
                    temp_dict[preferred_male][0]=preferred
                    if key == preferred_male:
                        unmatched.add(man)
                        temp_dict[man][0]=None
                    elif man == preferred_male:
                        unmatched.add(key)
                        temp_dict[key][0]=None
    return(extract_matches(temp_dict))        
                    
                       
    


  
    
if __name__ == '__main__':
    men_pref = read_match_preferences(goody.safe_open('Choose the file name representing preferences of the men' ,'r', 'Illegal: file name'))
    women_pref = read_match_preferences(goody.safe_open('Choose the file name representing preferences of the women' ,'r', 'Illegal: file name'))
    print('Men Preferences \n ', dict_as_str(men_pref), 'Women Preferences \n'    , dict_as_str(women_pref))
    matches = make_match(men_pref, women_pref)          
    # For running batch self-tests
    print(match)
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
