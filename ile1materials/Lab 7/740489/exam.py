from collections import defaultdict   # If you choose to use defaultdict  

# You might use these abbreviations in your code
# c  : caller
# r  : receiver
# t  : time
# ts : list of times


def all_parties(db : {str:{str:[int]}}) -> {str}:
    callers = set()
    for person in db:
        callers.add(person)
        for called in db[person]:
            callers.add(called)
    return callers



def read_db(file : open) -> {str:{str:[int]}}:
    readfile = file.read()
    lines = readfile.splitlines()
    thedict = {}
    for line in lines:
        splitline = line.split(":")
        name = splitline[0]
        called = splitline[1]
        timelist = splitline[2:]
        timelistint = []
        for t in timelist:
            timelistint.append(int(t))    
        if name not in thedict:
            thedict[name] = {called:timelistint}
        else:
            if called in thedict[name].keys():
                thedict[name][called] += timelistint
            else:
                thedict[name].update({called:timelistint})
    return thedict 



def talker_frequency (db : {str:{str:[int]}}) -> [(str,int)]:
    callslist = []
    calldict = {}
    for caller in db:
        if caller not in calldict:
            calldict[caller] = 0
        for called in db[caller]:
            if called not in calldict:
                calldict[called] = 0
                calldict[caller] += len(db[caller][called])
                calldict[called] += len(db[caller][called])
            else:
                calldict[caller] += len(db[caller][called])
                calldict[called] += len(db[caller][called])
    for caller in calldict:
        callslist.append((caller,calldict[caller]))
    return sorted(callslist, key = lambda x : (-x[1],x[0]))



def mutual_callers (db : {str:{str:[int]}}) -> {(str,str)}:
    callerset = set()
    callerdict = {}
    for caller in db:
        callerdict[caller] = []
        for called in db[caller]:
            callerdict[caller].append(called)
    for caller in callerdict:
        for called in callerdict[caller]:
            if caller in callerdict[called]:
                callerlist = sorted([caller,called])
                callerset.add(tuple(callerlist))
    return callerset
        
    
                



def initiators (db : {str:{str:[int]}}) -> [str]:
    callerlist = []
    callerdict = {}
    for caller in db:
        if caller not in callerdict:
            callerdict[caller] = [0,0]
        for called in db[caller]:
            if called in callerdict:
                callerdict[called][1] += len(db[caller][called])
                callerdict[caller][0] += len(db[caller][called])
            else:
                callerdict[called] = [0,0]
                callerdict[called][1] += len(db[caller][called])
                callerdict[caller][0] += len(db[caller][called])
    for caller in callerdict:
        calls = ()
        for times in callerdict[caller]:
            calls+=(times,)
        callerlist.append(calls+(caller,))
    values = sorted(callerlist, key = lambda x : (-x[0],x[1],x[2]))
    finalnames = []
    for caller in values:
        finalnames.append(caller[2])
    return finalnames
        



def matrix (db : {str:{str:[int]}}) -> [[int]]:
    pass





if __name__ == '__main__':
    import prompt
    # checks whether answer is correct, printing appropriate information
    # Note that dict/defaultdict will compare == if they have the same keys and
    #   associated values, regardless of the fact that they print differently
    def check (answer, correct):
        if (answer   == correct):
            print ('    CORRECT')
        else:
            print ('    INCORRECT')
            print ('      was       =',answer)
            print ('      should be =',correct)
        print()
 
 
    def lol(alol):
        return '\n        '+'\n        '.join(','.join(f'{col:3}' for col in line) for line in alol)
    
    if prompt.for_bool('Test all_parties?', True):  
        db1 = {'Alan': {'Barb': [10, 20], 'Carl': [10, 10]},
               'Barb': {'Alan': [10, 10], 'Deja': [5, 5, 5]},
               'Carl': {'Alan': [10, 5],  'Deja': [15],       'Elan': [5, 5]},
               'Deja': {'Elan': [5]},
               'Elan': {'Carl': [10]}
               }
        print('  argument =', db1)
        answer = all_parties(db1)
        print('  answer   =', answer)
        check(answer, {'Barb', 'Deja', 'Carl', 'Elan', 'Alan'})

        db1a = {'Alan': {'Barb': [10, 20], 'Carl': [10, 10]},
                'Barb': {'Alan': [10, 10], 'Deja': [5, 5, 5]},
                'Carl': {'Alan': [10, 5],  'Deja': [15],       'Elan': [5, 5]}
                }
        print('  argument =', db1a)
        answer = all_parties(db1a)
        print('  answer   =', answer)
        check(answer, {'Barb', 'Deja', 'Carl', 'Elan', 'Alan'})

        db2 = {
                'Gary': {'Barb': [1], 'Carl': [19, 12, 2], 'Hope': [8], 'Alan': [25, 26]},
                'Carl': {'Hope': [10], 'Gary': [11, 8], 'Deja': [12], 'Alan': [15, 11, 4], 'Barb': [34]},
                'Elan': {'Fern': [16], 'Deja': [6, 27], 'Carl': [3], 'Hope': [29]},
                'Barb': {'Gary': [14], 'Alan': [14], 'Fern': [4]},
                'Deja': {'Gary': [30, 26], 'Barb': [25, 3], 'Fern': [10, 3, 27], 'Hope': [4], 'Elan': [5]},
                'Alan': {'Barb': [3, 15], 'Hope': [2, 46], 'Gary': [36]},
                'Fern': {'Alan': [7], 'Carl': [37, 46, 43], 'Elan': [5], 'Gary': [7]},
                'Hope': {'Elan': [15],'Fern': [9, 2, 36], 'Alan': [6, 16], 'Barb': [29]}
                }
        print('  argument =', db2)
        answer = all_parties(db2)
        print('  answer   =', answer)
        check(answer, {'Hope', 'Barb', 'Elan', 'Carl', 'Alan', 'Gary', 'Deja', 'Fern'})



    if prompt.for_bool('Test read_db?', True):  
        db1 = {'Alan': {'Barb': [10, 20], 'Carl': [10, 10]},
               'Barb': {'Alan': [10, 10], 'Deja': [5, 5, 5]},
               'Carl': {'Alan': [10, 5],  'Deja': [15],       'Elan': [5, 5]},
               'Deja': {'Elan': [5]},
               'Elan': {'Carl': [10]}
               }
        print('  argument = db1.txt')
        answer = read_db(open('db1.txt'))
        print('  answer   =', answer)
        check(answer, db1)

        db2 = {
                'Gary': {'Barb': [1], 'Carl': [19, 12, 2], 'Hope': [8], 'Alan': [25, 26]},
                'Carl': {'Hope': [10], 'Gary': [11, 8], 'Deja': [12], 'Alan': [15, 11, 4], 'Barb': [34]},
                'Elan': {'Fern': [16], 'Deja': [6, 27], 'Carl': [3], 'Hope': [29]},
                'Barb': {'Gary': [14], 'Alan': [14], 'Fern': [4]},
                'Deja': {'Gary': [30, 26], 'Barb': [25, 3], 'Fern': [10, 3, 27], 'Hope': [4], 'Elan': [5]},
                'Alan': {'Barb': [3, 15], 'Hope': [2, 46], 'Gary': [36]},
                'Fern': {'Alan': [7], 'Carl': [37, 46, 43], 'Elan': [5], 'Gary': [7]},
                'Hope': {'Elan': [15],'Fern': [9, 2, 36], 'Alan': [6, 16], 'Barb': [29]}
                }
        print('  argument = db2.txt')
        answer = read_db(open('db2.txt'))
        print('  answer   =', answer)
        check(answer, db2)


    
    if prompt.for_bool('Test talker_frequency?', True):  
        db1 = {'Alan': {'Barb': [10, 20], 'Carl': [10, 10]},
               'Barb': {'Alan': [10, 10], 'Deja': [5, 5, 5]},
               'Carl': {'Alan': [10, 5],  'Deja': [15],       'Elan': [5, 5]},
               'Deja': {'Elan': [5]},
               'Elan': {'Carl': [10]}
               }
        print('  argument =', db1)
        answer = talker_frequency(db1)
        print('  answer   =', answer)
        check(answer, [('Alan', 8), ('Carl', 8), ('Barb', 7), ('Deja', 5), ('Elan', 4)])

        db2 = {
                'Gary': {'Barb': [1], 'Carl': [19, 12, 2], 'Hope': [8], 'Alan': [25, 26]},
                'Carl': {'Hope': [10], 'Gary': [11, 8], 'Deja': [12], 'Alan': [15, 11, 4], 'Barb': [34]},
                'Elan': {'Fern': [16], 'Deja': [6, 27], 'Carl': [3], 'Hope': [29]},
                'Barb': {'Gary': [14], 'Alan': [14], 'Fern': [4]},
                'Deja': {'Gary': [30, 26], 'Barb': [25, 3], 'Fern': [10, 3, 27], 'Hope': [4], 'Elan': [5]},
                'Alan': {'Barb': [3, 15], 'Hope': [2, 46], 'Gary': [36]},
                'Fern': {'Alan': [7], 'Carl': [37, 46, 43], 'Elan': [5], 'Gary': [7]},
                'Hope': {'Elan': [15],'Fern': [9, 2, 36], 'Alan': [6, 16], 'Barb': [29]}
                }
        print('  argument =', db2)
        answer = talker_frequency(db2)
        print('  answer   =', answer)
        check(answer, [('Carl', 15), ('Alan', 14), ('Fern', 14), ('Gary', 14), ('Hope', 13), ('Deja', 12), ('Barb', 10), ('Elan', 8)])


 
    if prompt.for_bool('Test mutual_callers?', True):  
        db1 = {'Alan': {'Barb': [10, 20], 'Carl': [10, 10]},
               'Barb': {'Alan': [10, 10], 'Deja': [5, 5, 5]},
               'Carl': {'Alan': [10, 5],  'Deja': [15],       'Elan': [5, 5]},
               'Deja': {'Elan': [5]},
               'Elan': {'Carl': [10]}
               }
        print('  argument =', db1)
        answer = mutual_callers(db1)
        print('  answer   =', answer)
        check(answer, {('Alan', 'Carl'), ('Carl', 'Elan'), ('Alan', 'Barb')})

        db2 = {
                'Gary': {'Barb': [1], 'Carl': [19, 12, 2], 'Hope': [8], 'Alan': [25, 26]},
                'Carl': {'Hope': [10], 'Gary': [11, 8], 'Deja': [12], 'Alan': [15, 11, 4], 'Barb': [34]},
                'Elan': {'Fern': [16], 'Deja': [6, 27], 'Carl': [3], 'Hope': [29]},
                'Barb': {'Gary': [14], 'Alan': [14], 'Fern': [4]},
                'Deja': {'Gary': [30, 26], 'Barb': [25, 3], 'Fern': [10, 3, 27], 'Hope': [4], 'Elan': [5]},
                'Alan': {'Barb': [3, 15], 'Hope': [2, 46], 'Gary': [36]},
                'Fern': {'Alan': [7], 'Carl': [37, 46, 43], 'Elan': [5], 'Gary': [7]},
                'Hope': {'Elan': [15],'Fern': [9, 2, 36], 'Alan': [6, 16], 'Barb': [29]}
                }
        print('  argument =', db2)
        answer = mutual_callers(db2)
        print('  answer   =', answer)
        check(answer, {('Elan', 'Fern'), ('Carl', 'Gary'), ('Alan', 'Hope'), ('Deja', 'Elan'), ('Alan', 'Barb'), ('Barb', 'Gary'), ('Elan', 'Hope'), ('Alan', 'Gary')})



    if prompt.for_bool('Test initiators?', True):  
        db1 = {'Alan': {'Barb': [10, 20], 'Carl': [10, 10]},
               'Barb': {'Alan': [10, 10], 'Deja': [5, 5, 5]},
               'Carl': {'Alan': [10, 5],  'Deja': [15],       'Elan': [5, 5]},
               'Deja': {'Elan': [5]},
               'Elan': {'Carl': [10]}
               }
        print('  argument =', db1)
        answer = initiators(db1)
        print('  answer   =', answer)
        check(answer, ['Barb', 'Carl', 'Alan', 'Elan', 'Deja'])

        db2 = {
                'Gary': {'Barb': [1], 'Carl': [19, 12, 2], 'Hope': [8], 'Alan': [25, 26]},
                'Carl': {'Hope': [10], 'Gary': [11, 8], 'Deja': [12], 'Alan': [15, 11, 4], 'Barb': [34]},
                'Elan': {'Fern': [16], 'Deja': [6, 27], 'Carl': [3], 'Hope': [29]},
                'Barb': {'Gary': [14], 'Alan': [14], 'Fern': [4]},
                'Deja': {'Gary': [30, 26], 'Barb': [25, 3], 'Fern': [10, 3, 27], 'Hope': [4], 'Elan': [5]},
                'Alan': {'Barb': [3, 15], 'Hope': [2, 46], 'Gary': [36]},
                'Fern': {'Alan': [7], 'Carl': [37, 46, 43], 'Elan': [5], 'Gary': [7]},
                'Hope': {'Elan': [15],'Fern': [9, 2, 36], 'Alan': [6, 16], 'Barb': [29]}
                }
        print('  argument =', db2)
        answer = initiators(db2)
        print('  answer   =', answer)
        check(answer, ['Deja', 'Carl', 'Hope', 'Gary', 'Fern', 'Elan', 'Alan', 'Barb'])

    
  
    if prompt.for_bool('Test matrix?', True):  
        db1 = {'Alan': {'Barb': [10, 20], 'Carl': [10, 10]},
               'Barb': {'Alan': [10, 10], 'Deja': [5, 5, 5]},
               'Carl': {'Alan': [10, 5],  'Deja': [15],       'Elan': [5, 5]},
               'Deja': {'Elan': [5]},
               'Elan': {'Carl': [10]}
               }
        print('  argument =', db1)
        answer = matrix(db1)
        print('  answer   =', answer)
        check(lol(answer), lol([[0, 50, 35, 0, 0], [50, 0, 0, 15, 0], [35, 0, 0, 15, 20], [0, 15, 15, 0, 5], [0, 0, 20, 5, 0]]))

        db2 = {
                'Gary': {'Barb': [1], 'Carl': [19, 12, 2], 'Hope': [8], 'Alan': [25, 26]},
                'Carl': {'Hope': [10], 'Gary': [11, 8], 'Deja': [12], 'Alan': [15, 11, 4], 'Barb': [34]},
                'Elan': {'Fern': [16], 'Deja': [6, 27], 'Carl': [3], 'Hope': [29]},
                'Barb': {'Gary': [14], 'Alan': [14], 'Fern': [4]},
                'Deja': {'Gary': [30, 26], 'Barb': [25, 3], 'Fern': [10, 3, 27], 'Hope': [4], 'Elan': [5]},
                'Alan': {'Barb': [3, 15], 'Hope': [2, 46], 'Gary': [36]},
                'Fern': {'Alan': [7], 'Carl': [37, 46, 43], 'Elan': [5], 'Gary': [7]},
                'Hope': {'Elan': [15],'Fern': [9, 2, 36], 'Alan': [6, 16], 'Barb': [29]}
                }
        print('  argument =', db2)
        answer = matrix(db2)
        print('  answer   =', answer)
        check(lol(answer),lol([[0, 32, 30, 0, 0, 7, 87, 70], [32, 0, 34, 28, 0, 4, 15, 29], [30, 34, 0, 12, 3, 126, 52, 10], [0, 28, 12, 0, 38, 40, 56, 4], [0, 0, 3, 38, 0, 21, 0, 44], [7, 4, 126, 40, 21, 0, 7, 47], [87, 15, 52, 56, 0, 7, 0, 8], [70, 29, 10, 4, 44, 47, 8, 0]]))

