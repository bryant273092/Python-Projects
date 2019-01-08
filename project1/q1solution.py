from collections import defaultdict
from math import sqrt,atan2


def integrate(f_int : callable, n : int) -> callable:
    if not n > 0:
        raise AssertionError('integer not greater than 0')
    def f(a, b):
        if not a <= b:
            raise AssertionError('a is not less than or equal to b')
        width = (b-a)/n
        total_area = 0
        for rect in range(a,b+1):
            total_area =+ f_int(rect)*width
       
        #print('sum is: ', sum)
        #height = f(a)
        #print('height is: ', height)
        return total_area
    return f


def sorted1 (ps : {int:(int,int)}) -> [(int,(int,int))]:
    return sorted(ps.items(), key = (lambda ps: ps[1]))



def sorted2 (ps : {int:(int,int)}) -> [(int,int)]:
    return sorted( sorted(ps.values(), key = (lambda ps:ps[0])), key = (lambda ps: atan2(ps[1], ps[0])), reverse=True)
    #return sorted(ps.values(), key = (lambda ps: atan2(ps[1], ps[0])), reverse=True)
  


def sorted3 (ps : {int:(int,int)}) -> [int]:
    return [k for k,v in sorted(ps.items(), key = (lambda ps: sqrt(ps[1][0]*ps[1][0]+ps[1][1]*ps[1][1])))]



def points (ps : {int:(int,int)}) -> [(int,int)]:
    return [v for k, v in sorted(ps.items(), key = (lambda k: k))]



def first_quad (ps : {int:(int,int)}) -> {(int,int):float}:
    return {v : sqrt(v[0]*v[0]+v[1]*v[1]) for v in ps.values() if v[0]>=0 and v[1]>=0}



def movie_rank(db : {str:{(str,int)}}) -> [(str,float)]:
    
    for movie in db:
        ratings_movies = []
        total_score = 0
        viewer_count = 0
        for viewer, rating in(db[movie]):
            new_tuple =()
            total_score =+ rating
            viewer_count=+1
        avg_score = total_score/viewer_count
        new_tuple =movie, avg_score
        ratings_movies.append(new_tuple)
    return ratings_movies
            



def reviewer_dict(db : {str:{(str,int)}}) -> {str:{(str,int)}}:
    pass





if __name__ == '__main__':
    # This code is useful for debugging your functions, especially
    #   when they raise exceptions: better than using driver.driver().
    # Feel free to add more tests (including tests showing in the bscF18.txt file)
    # Use the driver.driver() code only after you have removed anybugs
    #   uncovered by these test cases.
    
    print('Testing integrate')
    f = integrate( (lambda x : x), 100)
    print(f(0,1),f(0,2),f(-1,1))
    f = integrate( (lambda x : 3*x**2 - 2*x + 1), 1000)
    print(f(0,1),f(0,2),f(-1,1))
 
 
    print('\nTesting sorted1')
    ps1 = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    ps2 = {1:(0,5), 2:(2,3), 3:(-3,2), 4:(-5,1), 5:(-3,-2), 6:(4,-2), 7:(5,0), 8:(0,-5)}  
    print(sorted1(ps1))
    print(sorted1(ps2))
 
    print('\nTesting sorted2')
    ps1 = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    ps2 = {1:(0,5), 2:(2,3), 3:(-3,2), 4:(-5,1), 5:(-3,-2), 6:(4,-2), 7:(5,0), 8:(0,-5)}  
    print(sorted2(ps1))
    print(sorted2(ps2))
 
    print('\nTesting sorted3')
    ps1 = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    ps2 = {1:(0,5), 2:(2,3), 3:(-3,2), 4:(-5,1), 5:(-3,-2), 6:(4,-2), 7:(5,0), 8:(0,-5)}  
    print(sorted3(ps1))
    print(sorted3(ps2))
    
    print('\nTesting points')
    ps1 = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    ps2 = {1:(0,5), 2:(2,3), 3:(-3,2), 4:(-5,1), 5:(-3,-2), 6:(4,-2), 7:(5,0), 8:(0,-5)}  
    print(points(ps1))
    print(points(ps2))
 
    print('\nTesting first_quad')
    ps1 = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    ps2 = {1:(0,5), 2:(2,3), 3:(-3,2), 4:(-5,1), 5:(-3,-2), 6:(4,-2), 7:(5,0), 8:(0,-5)}  
    print(first_quad(ps1))
    print(first_quad(ps2))
 
    print('\nTesting movie_rank')
    db1 = {'Psycho':  {('Bob',5),  ('Carrie',5), ('Alan', 1), ('Diane', 1), }, 'Amadeus': {('Bob',3),  ('Carrie',3), ('Diane',3)}, 'Up': {('Alan',2), ('Diane',5)} }
    db2 = {'Psycho':  {('Bob',5),  ('Carrie',5), ('Alan', 1), ('Diane', 1), ('Evan',4), ('Fawn',2)},
           'Amadeus': {('Bob',3),  ('Carrie',3), ('Diane',3)},
           'Up': {('Alan',2), ('Diane',5)},
           'Casablaca': {('Alan',2), ('Diane',5), ('Evan',2)},
           'Rashamon': {('Alan',2), ('Diane',5), ('Fawn',3), ('Gary',4)},
           'Alien': {('Alan',2), ('Diane',5), ('Evan',5), ('Fawn',5)}}
    print(movie_rank(db1))
    print(movie_rank(db2))
 
    print('\nTesting reviewer_dict')
    db1 = {'Psycho':  {('Bob',5),  ('Carrie',5), ('Alan', 1), ('Diane', 1)}, 'Amadeus': {('Bob',3),  ('Carrie',3), ('Diane',3)}, 'Up': {('Alan',2), ('Diane',5)} }
    db2 = {'Psycho':  {('Bob',5),  ('Carrie',5), ('Alan', 1), ('Diane', 1), ('Evan',4), ('Fawn',2)},
           'Amadeus': {('Bob',3),  ('Carrie',3), ('Diane',3)},
           'Up': {('Alan',2), ('Diane',5)},
           'Casablaca': {('Alan',2), ('Diane',5), ('Evan',2)},
           'Rashamon': {('Alan',2), ('Diane',5), ('Fawn',3), ('Gary',4)},
           'Alien': {('Alan',2), ('Diane',5), ('Evan',5), ('Fawn',5)}}
    print(reviewer_dict(db1))
    print(reviewer_dict(db2))
 
 
    print('\ndriver testing with batch_self_check:')
    import driver
    driver.default_file_name = "bscq1F18.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()           

