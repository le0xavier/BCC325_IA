class BFS:
    def __init__(self, env):
        self.env = env
        self.goal = env.goal
        self.visited = {env.start: None}
        self.F = [env.start]

    def search(self):
        while self.F:
            node = self.F.pop(0)
            if node == self.goal:
                return self.goal
            for neighbor in self.env.get_neighbors(node):
                if neighbor not in self.visited:
                    self.visited[neighbor] = node
                    self.F.append(neighbor)
        return None  # se não encontrar

    def get_path(self, goal):
        if goal is None:
            return []
        node = goal
        path = []
        while node is not None:
            path.append(node)
            node = self.visited[node]
        path.reverse()
        return path


class DFS:
    def __init__(self, env):
        self.env = env
        self.goal = env.goal
        self.visited = {env.start: None}
        self.F = [env.start]

    def search(self):
        while self.F:
            node = self.F.pop()
            if node == self.goal:
                return self.goal
            for neighbor in self.env.get_neighbors(node):
                if neighbor not in self.visited:
                    self.visited[neighbor] = node
                    self.F.append(neighbor)
        return None  # se não encontrar

    def get_path(self, goal):
        if goal is None:
            return []
        node = goal
        path = []
        while node is not None:
            path.append(node)
            node = self.visited[node]
        path.reverse()
        return path