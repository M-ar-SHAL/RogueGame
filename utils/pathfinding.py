from collections import deque
from game.map import FLOOR

def bfs(grid, start, goal):
    visited = set()
    queue = deque([(start, [])])
    while queue:
        (y, x), path = queue.popleft()
        if (y, x) == goal:
            return path
        for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
                if grid[ny][nx] == FLOOR and (ny, nx) not in visited:
                    visited.add((ny, nx))
                    queue.append(((ny, nx), path + [(ny, nx)]))
    return []
