""" Main driver """

from maxflow.dinic import DinicImageSequence
from maxflow.graph import input_graph, display_graph
from maxflow.block_flow import BlockingFlowImageSequence
from gui.image_display import start_gui

graph, v, e = input_graph()
display_graph(graph)
print graph


def blocking_flow_test():
    b = DinicImageSequence(graph, v, e, 0, v - 1)
    start_gui(b)
    # block_graph = b.blocking_flow()
    # print "blocking flow", block_graph
    # display_graph(block_graph, "Block_flow")
blocking_flow_test()
