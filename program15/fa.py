#Submitter: bryanth1(Hernandez, Bryant)
import goody


def read_fa(file : open) -> {str:{str:str}}:
    transitions = {}
    for line in file.readlines():
        diff_states = line.strip('\n').split(';')
        key = diff_states.pop(0)        
        transitions[key] = dict(zip([tran for tran in diff_states if tran.isdigit()], [tran for tran in diff_states if tran != 'x' and not tran.isdigit() ]))  
    return(dict(sorted(transitions.items(), reverse = True)))


def fa_as_str(fa : {str:{str:str}}) -> str:
    new_str = ''
    for key in sorted(fa.keys(), reverse = False):
        temp_list = []
        for in_key in sorted(fa[key]):
            temp_list.append(tuple((in_key,(fa[key][in_key]))))
        new_str +='  '+ key+' transitions: ' + str(temp_list)+'\n'
    return (new_str)

    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    trace = []
    trace.append(state)
    for tran in inputs:
        if tran == '1':
            if state == 'odd':
                state = 'even'
                trace.append(tuple((tran, state)))
            elif state == 'even':
                state = 'odd'
                trace.append(tuple((tran,state)))
        elif tran == '0':
            trace.append(tuple((tran, state)))
        elif tran == 'x':
            trace.append(tuple((tran, None)))
            
    return(trace)
    


def interpret(fa_result : [None]) -> str:
    f_str =''
    f_str +='Start state = ' + fa_result.pop(0) + '\n'
    for x, y in fa_result:
        if y == None:
            f_str += '  Input = ' + x + '; ' + 'illegal input: simulation terminated' + '\n' 
            break  
        f_str += '  Input = ' + x + '; ' + 'new state = ' + y + '\n'
    f_str +=  'Stop state = ' + str(y) + '\n'
    return(f_str)
    
    
if __name__ == '__main__':
    file = goody.safe_open('Choose the file name representing the finite automaton', 'r', 'illegal file name')
    fa = read_fa(file)
    print(fa_as_str(fa))
    new_file = goody.safe_open('Choose the file name representing the start-states and their inputs', 'r', 'illegal file name')
    for line in new_file.readlines():
        inputs = line.strip('\n').split(';')
        start = inputs.pop(0)
        print('\n'+ 'Begin tracing the next FA simulation' + '\n' + interpret(process(fa, start, inputs)))
        
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
