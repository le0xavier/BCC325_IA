class MazeEnvironment:
    def __init__(self, maze):
        self.maze = maze
        self.start, self.goal = self.pos_start_goal()

    def pos_start_goal(self):
        start = None
        goal = None
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == 's':
                    start = (i, j)
                elif self.maze[i][j] == 'g':
                    goal = (i, j)
        return start, goal

    def get_neighbors(self, pos):
        directions = [(-1,0), (1,0), (0,-1), (0,1)]  # cima, baixo, esquerda, direita
        neighbors = []
        rows = len(self.maze)
        cols = len(self.maze[0])

        for dr, dc in directions:
            r, c = pos[0] + dr, pos[1] + dc
            if 0 <= r < rows and 0 <= c < cols:  # dentro da matriz
                if self.maze[r][c] != 1:  # não é parede
                    neighbors.append((r, c))
        return neighbors