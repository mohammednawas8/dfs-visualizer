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
| depth_limited_search(graph,start,goal)  | Returns the expanded nodes and the final path when visualizing depth limited search  |
<br>

2- helper.py : Contains helper functions that are commonly used accross the the other files.

| function  | usage |
| ------------- | ------------- |
| buildGraphUI(graph)  | Build the the graph nodes |
| drawGraph()  | Draw the graph but note that this will not show the graph window  |
| showGraph()  | Shows up the graph window  |
| closeGraph()  | Close the graph window  |
| getEdgesFromGraph()  | This function will get each parent and its children as pairs and group them in a tuple then return them as a list<br>Example: [(1,2),(1,3)] 1 is a parent node that has "2" and "3" as children.  |
<br>

3- visualizers.py : Handles the visualizing proccess.
| function  | usage |
| ------------- | ------------- |
| startVisualizing(graph,visited,path) | Receives the graph, plot it, and colors the expanded/final-path nodes |
| startDfsVisualizer(graph, start, goal,self)  | -Recevies the graph and call dfs() to get the expanded nodes and the final path<br>-Update the expanded nodes label, final path label<br>-then calls startVisualizing() |
| startLimitedDFSVisualizer(graph, start,goal,limit,self)  | it does the same thing the startDfsVisualizer() function does but for Limited depth first search |
| startIteretiveVisualizer(graph, start, goal,depth,self)  | it does the same as the previous functions but it calls dfs() from a for loop that iterate all depths until finding the path |
<br>

4- main.py : Where the app starts and handles the user events.
| function  | usage |
| ------------- | ------------- |
| showGraphPreivew(self)  | Show the graph when the "Show Graph" button is clicked |
| closeGraphPreview(self)  | Close the graph when the "Close Graph" button is clicked |
| selectCheckboxDfs(self)  | Selects dfs |
| selectCheckboxLdfs(self)  | Selects limited dfs and enable the depth text field |
| selectCheckboxIds(self)  | Selects Iterative deepening search and enable the depth text field |
| startSearchingInGraph(self)  | Start the visualizing when "Start"  button is clicked |
<br>

5- GUI.ui : Contains the user interface design code (XML code).
<br>
# How to Run
To run this project on your own computer you can follow up with the following steps :<br>
-Note that i am using VSCode to install and run the project.
<br>
*Download this repository and extract the files

