from yamlify import yamlify
from edge_list_generator  import edge_list_generator



if __name__ == '__main__':
    

    # parse .py 
    yamlify('../labgraph/examples/simple_viz_zmq.py')

    # generate an edge list representation of the computational graph
    edge_list = edge_list_generator('./outputs/simple_viz_zmq.yaml',labels_only=True)
    print(edge_list)



