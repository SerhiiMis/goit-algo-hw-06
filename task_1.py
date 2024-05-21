import networkx as nx
import matplotlib.pyplot as plt

# Дані про лінії метро Праги
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

# Додавання вершин та ребер для лінії трамваю
for i in range(len(line_tram) - 1):
    transport_lines_praha.add_edge(line_tram[i], line_tram[i + 1])

# Визначення кольорів вершин і ребер
node_colors = ['skyblue' if node not in line_tram else 'orange' for node in transport_lines_praha.nodes()]
edge_colors = ['black' if not transport_lines_praha.has_edge(u, v) else 'orange' for u, v in transport_lines_praha.edges()]

# Візуалізація графу
plt.figure(figsize=(12, 7))
pos = nx.spring_layout(transport_lines_praha, seed=44) 
nx.draw(transport_lines_praha, pos, with_labels=True, node_size=800, node_color=node_colors, font_size=9, font_weight='bold', edge_color=edge_colors)
plt.title("Мапа-схема метрополітену і трамвая Праги")
plt.show()

# Аналіз основних характеристик графу
num_nodes = transport_lines_praha.number_of_nodes()
num_edges = transport_lines_praha.number_of_edges()
degrees = dict(transport_lines_praha.degree()) 

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Ступінь вершин: {degrees}")
