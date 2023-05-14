# dfs-visualizer
This project is built to visualize how dfs algorithms work to find the expanded nodes and the final path of a graph, the supported algorithms are:<br>
1- Depth First Search.<br>
2- Limited Depth First Search.<br>
3- Iterative deepening search.<br>

# Preview
https://github.com/mohammednawas8/dfs-visualizer/assets/78867217/7d29552d-ebbf-439c-8bcb-1ebb8e065930

# Project structure
This project is divided into 5 files, they are:<br><br>
1- algorithms.py : Contains the raw algorithms code. i.e:dfs and depth_limited_search.<br>
| function  | usage |
| ------------- | ------------- |
| dfs(graph,start,goal)  | Returns the expanded nodes and the final path when visualizing dfs |
| depth_limited_search(graph,start,goal)  | Returns the expanded nodes and the final path when visualizing depth_limited_search  |
<br>

2- helper.py : Contains helper functions that are commonly used accross the the other files.

| function  | usage |
| ------------- | ------------- |
| buildGraphUI(graph)  | Build the the graph nodes |
| drawGraph()  | Draw the graph but note that this will not show the graph window  |
| showGraph()  | Shows up the graph window  |
| closeGraph()  | Close the graph window  |
| getEdgesFromGraph()  | This function will get each parent and its children as pairs and group them in a tuple then return them as a list<br>Example: [(1,2),(1,3)] 1 is a parent node that has "2" and "3" as children.  |

closeGraph() and showGraph().
