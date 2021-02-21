# Global or class scope variables
n = 'number of nodes in the graph'
graph = 'adjacency list representing graph'
visited = [False, '...', False]  # size n


def dfs(at):
    if visited[at]:
        return
    visited[at] = True

    neighbours = graph[at]
    for next in neighbours:
        dfs(next)


# start DFS at node zero
start_node = 0
dfs(start_node)
