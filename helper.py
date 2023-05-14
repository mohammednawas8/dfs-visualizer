
import matplotlib.pyplot as plt
import networkx as nx



# This function will get each parent and its children as pairs and group them in a tuple then return them as a list
# Example: [(1,2),(1,3)] 1 is a parent node that has "2" and "3" as children.
def getEdgesFromGraph(graph):
    keys = list(graph.keys())
    edgesFrom = []
    for parent in keys:
        for child in graph[parent]:
            edgesFrom.append((parent, child))
    return edgesFrom



# graph: is the graph dict
# the function returns G object which comes from Networkx
def buildGraphUI(graph):
    G = nx.DiGraph()
    G.add_edges_from(getEdgesFromGraph(graph))
    return G


def drawGraph(G,colorMap):
    pos = nx.spectral_layout(G)
    nx.draw(G,with_labels=True, pos=pos, node_color=colorMap)

def showGraph():
    plt.show()

def closeGraph():
    plt.close()
