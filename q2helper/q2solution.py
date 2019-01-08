#Submitter: bryanth1(Hernandez, Bryant)
import re
from goody import irange
from collections import defaultdict

# Before running the driver on the bsc.txt file, ensure you have put a regular
#   expression pattern in the files repattern1a.txt, repattern1b.txt, and
#   repattern2a.txt. The patterns must be all on the first line

def pages (page_spec : str, unique :  bool) -> [int]: #result in ascending order
    answer = []
    p2a = open('repattern2a.txt').read().rstrip()
    for line in page_spec.split(','):
        m1, m2, m3, n = re.match(p2a, line).groups()
        if not m2:
            answer.append(int(m1))
        else:
            m1, m3, n = int(m1), int(m3), int(n) if not None else None
            if m2 == '-':
                assert int(m1) <= int(m3)
                answer += [i for i in range(int(m1),int(m3),n)]
            else:
                answer += [i for i in range(int(m1), m1+m3,m)]
    return sorted(set(answer) if unique else answer)
    
    
    
    
    
#     matches =[]
#     p2a = open('repattern2a.txt').read().rstrip()
#     for i in page_spec.split(','):
#         match = list(re.match(p2a, i).groups())
#         if '-' in match:
#             if match[3] != None:
#                 for i in irange(eval(match[0]),eval(match[2]),eval(match[3])):
#                     matches.append(i)
#             else: 
#                 assert  eval(match[0])<=eval(match[2])
#                 for i in irange(eval(match[0]),eval(match[2])):
#                     matches.append(i)      
#         elif ':' in match:
#             if match[3] != None:
#                 for i in range(eval(match[0]),eval(match[0])+eval(match[2]),eval(match[3])):
#                     matches.append(i)
#                 break
#             else:   
#                 for i in range(eval(match[0]),eval(match[0])+eval(match[2])):
#                     matches.append(i)
#         else: 
#             for i in match:
#                 if i != None:
#                     matches.append(eval(i))
#     if unique:
#         return list(set(matches))
#     return sorted(matches)
def expand_re(pat_dict:{str:str}):
    for key in pat_dict.keys():
        for key2, value in pat_dict.items():
            if str(key) in value.split('#'):
                new = value.split('#')
                pat_dict[key2]=((re.sub(str(key), '(?:'+ str(pat_dict[key])+')', ''.join(new))))
                
    





if __name__ == '__main__':
    
    p1a = open('repattern1a.txt').read().rstrip() # Read pattern on first line
    print('Testing the pattern p1a: ',p1a)
    for text in open('bm1.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p1a,text)
        print(' ','Matched' if m != None else "Not matched")
        
    p1b = open('repattern1b.txt').read().rstrip() # Read pattern on first line
    print('\nTesting the pattern p1b: ',p1b)
    for text in open('bm1.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p1b,text)
        print('  ','Matched with groups ='+ str(m.groups()) if m != None else 'Not matched' )
        
        
    p2 = open('repattern2a.txt').read().rstrip() # Read pattern on first line
    print('\nTesting the pattern p2: ',p2)
    for text in open('bm2a.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p2,text)
        print('  ','Matched with groups ='+ str(m.groups()) if m != None else 'Not matched' )
        
    print('\nTesting pages function')
    for text in open('bm2b.txt'):
        text = text.rstrip().split(';')
        text,unique = text[0], text[1]=='True'
        try:
            p = pages(text,unique)
            print('  ','pages('+text+','+str(unique)+') = ',p)
        except:
            print('  ','pages('+text+','+str(unique)+') = raised exception')
        
    
    print('\nTesting expand_re')
    pd = dict(digit = r'[0-9]', integer = r'[+-]?#digit##digit#*')
    print('  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary
    # {'digit': '[0-9]', 'integer': '[+-]?(?:[0-9])(?:[0-9])*'}
    
    pd = dict(integer       = r'[+-]?[0-9]+',
              integer_range = r'#integer#(..#integer#)?',
              integer_list  = r'#integer_range#(?,#integer_range#)*',
              integer_set   = r'{#integer_list#?}')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'integer': '[+-]?[0-9]+',
    #  'integer_range': '(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?',
    #  'integer_list': '(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?)(?,(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?))*',
    #  'integer_set': '{(?:(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?)(?,(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?))*)?}'
    # }
    
    pd = dict(a='correct',b='#a#',c='#b#',d='#c#',e='#d#',f='#e#',g='#f#')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'a': 'correct',
    #  'b': '(?:correct)',
    #  'c': '(?:(?:correct))',
    #  'd': '(?:(?:(?:correct)))',
    #  'e': '(?:(?:(?:(?:correct))))',
    #  'f': '(?:(?:(?:(?:(?:correct)))))',
    #  'g': '(?:(?:(?:(?:(?:(?:correct))))))'
    # }
    
    print()
    print()
    import driver
    driver.default_file_name = "bscq2F18.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()