import networkx as nx
import matplotlib.pyplot as plt
from heapq import heappop, heappush

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

# Додавання вершин та ребер з вагами для всіх ліній
def add_line_to_graph(graph, line, weight=1):
    for i in range(len(line) - 1):
        graph.add_edge(line[i], line[i + 1], weight=weight)

add_line_to_graph(transport_lines_praha, line_a)
add_line_to_graph(transport_lines_praha, line_b)
add_line_to_graph(transport_lines_praha, line_c)
add_line_to_graph(transport_lines_praha, line_tram)

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, attributes in graph[current_node].items():
            distance = current_distance + attributes['weight']
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(priority_queue, (distance, neighbor))
    
    return distances

# Знаходження найкоротших шляхів від усіх вершин до всіх інших вершин
shortest_paths = {node: dijkstra(transport_lines_praha, node) for node in transport_lines_praha.nodes}

# Результати: найкоротші шляхи для кожної пари вершин
for start_node, paths in shortest_paths.items():
    print(f"Найкоротші шляхи від {start_node}:")
    for end_node, distance in paths.items():
        print(f"  до {end_node}: {distance}")

# Візуалізація графу
plt.figure(figsize=(14, 9))
pos = nx.spring_layout(transport_lines_praha, seed=44)
nx.draw(transport_lines_praha, pos, with_labels=True, node_size=800, node_color='skyblue', font_size=10, font_weight='bold')

# Виділення трамвайної лінії іншим кольором
tram_edges = list(zip(line_tram, line_tram[1:]))
nx.draw_networkx_edges(transport_lines_praha, pos, edgelist=tram_edges, edge_color='red', width=2)

plt.title("Мапа-схема метрополітену і трамвая Праги")
plt.show()
