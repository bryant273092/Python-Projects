from performance import Performance
from goody import irange
from graph_goody import random_graph,spanning_tree
from random import randint

# Put script below to generate data for Problem #1
# In case you fail, the data appears in sample8.pdf in the helper folder
n = 1000

for i in range(8):
    new_graph = random_graph(n ,lambda n : 10*n)
    first_data = Performance(lambda: spanning_tree(new_graph), lambda: None, 5, 'Spanning Tree of size '+str(n))
    first_data.evaluate()
    first_data.analyze()
    n = n *2
    