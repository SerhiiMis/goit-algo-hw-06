import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Дані про лінії метро і трамвай
line_a = [
    'Nemocnice Motol', 'Petriny', 'Nadrazi Veleslavin', 'Borislavska', 'Dejvicka',
    'Hradcanska', 'Malostranska', 'Staromestska', 'Mustek', 'Muzeum', 'Namesti Miru',
    'Jiriho z Podebrat', 'Flora', 'Zelivskeho', 'Strasnicka', 'Skalka', 'Depo Hostivar'
]

line_b = [
    'Zlicin', 'Stodulky', 'Luka', 'Luziny', 'Hurka', 'Nove Butovice', 'Jinonice',
    'Radlicka', 'Smichovske nadrazi', 'Andel', 'Karlovo namesti', 'Narodni trida',
    'Mustek', 'Namesti Republiky', 'Florenc', 'Krizikova', 'Invalidovna', 'Palmovka',
    'Ceskomoravska', 'Vysocanska', 'Kolbenova', 'Hloubetin', 'Rajska zahrada', 'Cerny most'
] 

line_c = [
    'Letnany', 'Prosek', 'Strizkov', 'Ladvi', 'Kobelisy', 'Nadrazi Holesovice', 'Vltavska',
    'Florenc', 'Hlavni nadrazi', 'Muzeum', 'I.P. Pavlova', 'Vysehrad', 'Prazskeho povstani',
    'Pankrac', 'Budejovicka', 'Kacerov', 'Roztyly', 'Chodov', 'Opatov', 'Haje'
]

line_tram = [
    'Barrandov', 'Hlubocepy', 'Lihovar', 'Smichovske nadrazi', 'Andel', 'Ujezd', 
    'Narodni trida', 'Lazarska', 'Jindrisska', 'Hlavni nadrazi'
]

# Створення графу
transport_lines_praha = nx.Graph()

# Додавання вершин та ребер для лінії A
for i in range(len(line_a) - 1):
    transport_lines_praha.add_edge(line_a[i], line_a[i + 1])

# Додавання вершин та ребер для лінії B
for i in range(len(line_b) - 1):
    transport_lines_praha.add_edge(line_b[i], line_b[i + 1])

# Додавання вершин та ребер для лінії C
for i in range(len(line_c) - 1):
    transport_lines_praha.add_edge(line_c[i], line_c[i + 1])

# Додавання вершин та ребер для трамвайної лінії
for i in range(len(line_tram) - 1):
    transport_lines_praha.add_edge(line_tram[i], line_tram[i + 1])

# Функція для виконання DFS
def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex in visited:
            continue
        visited.add(vertex)
        for neighbor in set(graph.neighbors(vertex)) - visited:
            if neighbor == goal:
                return path + [neighbor]
            else:
                stack.append((neighbor, path + [neighbor]))
    return None

# Функція для виконання BFS
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        (vertex, path) = queue.popleft()
        if vertex in visited:
            continue
        visited.add(vertex)
        for neighbor in set(graph.neighbors(vertex)) - visited:
            if neighbor == goal:
                return path + [neighbor]
            else:
                queue.append((neighbor, path + [neighbor]))
    return None

# Вхідні дані для пошуку
start = 'Dejvicka'
goal = 'Haje'

# Виконання DFS і BFS
path_dfs = dfs(transport_lines_praha, start, goal)
path_bfs = bfs(transport_lines_praha, start, goal)

# Результати
print(f"Шлях, знайдений DFS: {path_dfs}")
print(f"Кількість станцій у шляху DFS: {len(path_dfs)}" if path_dfs else "Шлях DFS не знайдено")
print(f"Шлях, знайдений BFS: {path_bfs}")
print(f"Кількість станцій у шляху BFS: {len(path_bfs)}" if path_bfs else "Шлях BFS не знайдено")

# Візуалізація графу з підсвіченими шляхами
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(transport_lines_praha, seed=44)

# Базова візуалізація графу
nx.draw(transport_lines_praha, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold")

# Підсвічування шляху DFS
if path_dfs:
    nx.draw_networkx_nodes(transport_lines_praha, pos, nodelist=path_dfs, node_color="green")
    nx.draw_networkx_edges(transport_lines_praha, pos, edgelist=list(zip(path_dfs, path_dfs[1:])), edge_color="green", width=2)

# Підсвічування шляху BFS
if path_bfs:
    nx.draw_networkx_nodes(transport_lines_praha, pos, nodelist=path_bfs, node_color="red")
    nx.draw_networkx_edges(transport_lines_praha, pos, edgelist=list(zip(path_bfs, path_bfs[1:])), edge_color="red", width=2)

plt.title("Прага Метрополітен: Порівняння шляхів DFS (зелений) та BFS (червоний)")
plt.show()
