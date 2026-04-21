from collections import deque
from src.core_logic import get_start_goal, get_neighbors, print_maze_with_path

def bfs(maze):
    start, goal = get_start_goal(maze)
    queue = deque([(start, [start])])
    visited = set([start])
    
    # TODO: Sinh viên viết tiếp vòng lặp duyệt đồ thị tại đây.
    # Gợi ý: 
    # - Sử dụng vòng lặp: while queue:
    # - Hàm lấy ra: queue.popleft()
    # - Hàm đẩy vào: queue.append()
    # ... (Sinh viên code ở đây) ...
    from collections import deque
    from src.core_logic import get_start_goal, get_neighbors, print_maze_with_path

def bfs(maze):
    start, goal = get_start_goal(maze)
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        current, path = queue.popleft()

        # Nếu đến đích
        if current == goal:
            return path

        # Duyệt các ô kề
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None
    return None