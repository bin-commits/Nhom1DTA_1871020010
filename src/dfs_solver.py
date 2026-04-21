from src.core_logic import get_start_goal, get_neighbors, print_maze_with_path

def dfs(maze):
    start, goal = get_start_goal(maze)
    stack = [(start, [start])]
    visited = set([start])
    
    # TODO: Sinh viên viết tiếp vòng lặp duyệt đồ thị tại đây.
    # Gợi ý: 
    # - Sử dụng vòng lặp: while stack:
    # - Hàm lấy ra từ ĐỈNH ngăn xếp (LIFO): stack.pop()
    # - Hàm đẩy vào: stack.append()
    
    # ... (Sinh viên code logic Tìm kiếm theo chiều sâu ở đây) ...
    from src.core_logic import get_start_goal, get_neighbors, print_maze_with_path

def dfs(maze):
    start, goal = get_start_goal(maze)
    stack = [(start, [start])]   # Stack (LIFO)
    visited = set([start])
    
    while stack:
        current, path = stack.pop()   # Lấy từ đỉnh stack

        # Kiểm tra đích
        if current == goal:
            return path

        # Duyệt các ô kề
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))  # Đẩy vào stack
    
    return None
    return None