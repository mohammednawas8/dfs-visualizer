def dfs(graph, start,goal):
    visited = []
    path = []
    s = [start]
    temp = []
    chpg = {}
    
    while s:
        v = s.pop()
        if v in visited:
            continue
        visited.append(v)
        if goal == v:
            break
        for i in graph.get(v, []):
            temp.append(i)
            chpg[i] = v
        while temp:
            s.append(temp.pop())

    # Finding the Final path:
    path.append(goal)
    while goal != start:
        try:
            goal = chpg[goal]
            path.insert(0, goal)
        except KeyError:
            print(f"Cannot find the path for start={start} and goal={goal}")
            return visited,[]

    return visited,path


##########################################################################################################################


def depth_limited_search(graph, start, goal,limit):
    visited, path, temp, path = [], [], [], []
    s = [(start, 0)]
    chpg = {}

    while s:
        v, d = s.pop()  # d: is the depth of the node


        if v in visited:
            continue

        visited.append(v)

        if v == goal:
            break

        for i in graph.get(v, []):
            if d < limit:       # Question: Why don't we take this condition out of the loop?
                                #Answer: Because if we do so then we won't be able to go back to visit the other neighbours of the same parent node.
                temp.append((i, d+1))
                chpg[i] = v
        while temp:
            s.append(temp.pop())

    path.append(goal) # To include the goal in the final path.
    while goal != start:
        try:
            goal = chpg[goal]
            path.insert(0, goal)
        except KeyError: # If we catch KeyError that means we can't find a path at the specified limit.
            print(f"Cannot find the path for goal={goal} and limit={limit}")
            return visited,[]
    return visited,path