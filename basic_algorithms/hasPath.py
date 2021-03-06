import collections


def hasPath(graph, src, dst):

    visited = set()
    def dfs(graph, source, target):
        visited.add(source)
        if source == target:
            return True
        
        canReach = False
        for neighbor in graph[source]:
            if neighbor not in visited:
                canReach = canReach or dfs(graph, neighbor, target)
        return canReach
    
    return dfs(graph, src, dst)

def hasPath(graph, src, dst):
    if src == dst: return True
    
    for neighbor in graph[src]:
        if hasPath(graph, neighbor, dst): return True
    return False

def hasPath(graph, src, dst):
    return src == dst or any(hasPath(graph, neighbor, dst) for neighbor in graph[src])

def hasPathB(graph, src, dst):
    if src == dst: return True

    queue = collections.deque()
    queue.append(src)

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor == dst:
                return True
            queue.append(neighbor)
    return False
                
graph = {
        'f' : ['g', 'i'],
        'g' : ['h'],
        'h' : [],
        'i' : ['g', 'k'],
        'j' : ['i'],
        'k' : []
        }

print(hasPath(graph, 'f', 'k'))