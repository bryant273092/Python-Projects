import cProfile
from graph_goody import random_graph, spanning_tree
import pstats

# Put script below to generate data for Problem #2
# In case you fail, the data appears in sample8.pdf in the helper folder
n = 15000
new_graph = random_graph(n ,lambda n : 10*n)
graph = lambda: spanning_tree(new_graph)
cProfile.run('graph()','profile')
p = pstats.Stats('profile')
p.strip_dirs().sort_stats('calls').print_stats(10)
p.strip_dirs().sort_stats('time').print_stats(10)