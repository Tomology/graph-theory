# Global or class scope variables

n = 'number of nodes in the graph'
graph = 'adjacency list representing graph'
count = 0
components = []  # size n
visited = [False, '...', False]  # size n


def findComponents():
    for i in range(0, len(n)):
        if not visited[i]:
            count = count + 1
            dfs(i)
    return (count, components)


def dfs(at):
    visited[at] = True
    components[at] = count
    for next in range(graph[at]):
        if not visited[next]:
            dfs(next)
