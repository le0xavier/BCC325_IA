from agents import BFS, DFS
from environment import MazeEnvironment

maze = [
    ['s', 0,   1,   0,   0],
    [ 1 , 0,   1,   0,   1],
    [ 0 , 0,   0,   0,  'g']
]

print("Labirinto original:")
for row in maze:
    print(row)

# Cria o ambiente
env = MazeEnvironment(maze)

print(f'Início: {env.start}')
print(f'Objetivo: {env.goal}')

# Executa BFS
agent = BFS(env)
goal = agent.search()
path = agent.get_path(goal)

print("\nCaminho encontrado (BFS):")
print(path)

# Cria cópia do labirinto e marca o caminho com '*'
maze_with_path = [row.copy() for row in maze]
for r, c in path:
    if maze_with_path[r][c] not in ['s', 'g']:
        maze_with_path[r][c] = '*'

print("\nLabirinto com o caminho marcado:")
for row in maze_with_path:
    print(row)