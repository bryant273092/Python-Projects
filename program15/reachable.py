#Submitter: bryanth1(Hernandez, Bryant)
import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    temp_graph = {number : node.strip('\n').split(';') for number, node in enumerate(file.readlines(), 1)}
    graph = defaultdict(set)
    for node in temp_graph.values():
        graph[node[0]].add(node[1])
    return(dict(sorted(graph.items())))
    
def graph_as_str(graph : {str:{str}}) -> str:
    str_graph = ''
    for x in sorted(graph.keys()):
        str_graph += '  ' + x + ' -> '+ str(sorted(list(graph[x]))) + '\n'
    return(str_graph)

        
def reachable(graph : {str:{str}}, start : str, trace : bool = False) -> {str}:
    reached_nodes = set()
    list_explore = [start]
    while list_explore:
        if trace:
            print('reached set    =', reached_nodes)
            print('exploring list =', list_explore)
        first_node = list_explore.pop(0)
        if trace:
            print('removing node from exploring list and adding it to reached list: node =', first_node)
        reached_nodes.add(first_node)
        if graph.get(first_node) != None:
            for node in graph.get(first_node):
                if node not in reached_nodes:
                    list_explore.append(node)  
        if trace:
            print('after adding all nodes reachable directly from', node, 'but not already in reached, exploring = ', list_explore, '\n')      
    return(reached_nodes)





if __name__ == '__main__':
    file = goody.safe_open('Choose the file name representing the graph' ,'r', 'Illegal: file name')
    graph = read_graph(file)
    print('\n',"Graph: any node -> [all that node's destination nodes]")
    print(graph_as_str(graph))
    while True: 
        start = prompt.for_string('Choose the start node (or choose quit)', is_legal = (lambda start : start in graph.keys() or start == 'quit'), error_message ='Illegal: not a source node') 
        if start == 'quit':
            break 
        trace = prompt.for_bool('Choose whether to trace this algorithm', default = True, error_message = "Input must be bool")
        print('From',start, 'the reachable nodes are', sorted(reachable(graph, start, trace), reverse = True))
        import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
