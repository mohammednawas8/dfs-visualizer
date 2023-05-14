from algorithms import depth_limited_search, dfs
from helper import *
import matplotlib.pyplot as plt
import networkx as nx
from helper import getEdgesFromGraph

def startVisualizing(graph,visited,path):
    G = buildGraphUI(graph)
    colorMap = ['blue' for node in G]
    drawGraph(G, colorMap)

    plt.pause(0.2)

    # Draw the expanded nodes (Red Color)
    expandedNodes = [] # To remember the all expanded nodes colors.
    for expandedNode in visited:
        plt.pause(0.5)
        expandedNodes.append(expandedNode)
        colorMap = ['red' if node in expandedNodes else 'blue' for node in G] # بكل لفة بدنا نمر على جميع النودز ونفحص الوانهم واستخدمت الليست اللي برا اللوب عشان اتذكر الوان النودز اللي تم اكتشافهم
        drawGraph(G,colorMap)

    plt.pause(1.2)

    # Draw the final path (Green color)
    finalPath = []
    placeHolder = -1 # Placeholder solved a bug that is the last node never get colored.
    path.append(placeHolder)
    for pathNode in path:
        plt.pause(0.5)
        finalPath.append(pathNode)
        colorMap = ['green' if node in finalPath else 'blue' for node in G]
        drawGraph(G, colorMap)


##########################################################################################################################


def startDfsVisualizer(graph, start, goal,self=None):

    visited, path = dfs(graph, start, goal)
    print(f"Expanded nodes: {visited}")
    print(f"Final path: {path}")


    self.txtExpandedNodes.setText(f"Expanded Nodes: {visited}")

    if (path==[]):
        self.txtFinalPath.setText(f"Cannot find the path for start={start} and goal={goal}")
    else:
        self.txtFinalPath.setText(f"Final Path: {path}")
        startVisualizing(graph,visited,path)
        plt.show()


##########################################################################################################################


def startLimitedDFSVisualizer(graph, start,goal,limit,self):
    visited,path=depth_limited_search(graph=graph,start=start,goal=goal,limit=limit)
    print(f"Expanded nodes: {visited}")
    print(f"Final path: {path}")

    self.txtExpandedNodes.setText(f"Expanded Nodes: {visited}")
    if(path == []):
        self.txtFinalPath.setText(f"Final Path: Cannot find the path for goal={goal} and limit={limit}")
    else:
        self.txtFinalPath.setText(f"Final Path: {path}")
    startVisualizing(graph,visited,path)
    plt.show()


##########################################################################################################################


def startIteretiveVisualizer(graph, start, goal,depth,self):
    for limit in range(1,depth+1):
        visited,path = depth_limited_search(graph=graph,start=start,goal=goal,limit=limit)
        # print(f"Expanded nodes: {visited}")
        # print(f"Final path: {path}")

        self.txtExpandedNodes.setText(f"Expanded Nodes: {visited}")
        if(path == []):
            self.txtFinalPath.setText(f"Final Path: Cannot find the path for goal={goal} and depth={limit}")
        else:
            self.txtFinalPath.setText(f"Final Path: {path}")

        startVisualizing(graph,visited,path)

        path.pop() # I pop that last element because i found out that -1 is appended to the list after each iteration.
        if len(path) > 0: #Ending Case
            break

    plt.show()  # To show the drawing window.