from collections import defaultdict


class Graph():
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight


graph = Graph()


def findshorterspatch(graph, initial, end):

    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)
                                   ] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {
            node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations,
                           key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    weight = []
    while current_node is not None:
        path.append(current_node)
        weight.append(shortest_paths[current_node][1])
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    weight = weight[::-1]
    getlast = len(weight)-1
    return ('Rutenya adalah : ', path, ' dengan jarak tempuh ', weight[getlast], ' KM')


def menu():
    userinput = input(
        "----- GRAPH -----\n1. Masukan Kota\n2. Masukan Lintasan\n3. Cek Rute\n\nPilih Menu : ")
    if userinput == '1':
        kota()
    elif userinput == '2':
        lintasan()
    elif userinput == '3':
        rute()
    else:
        print("\nInvalid Key Input\n")


def kota():
    input("Masukan Kota : ")
    pertanyaan()


def lintasan():
    l = input("Masukkan lintasan (dari, ke, jarak):")
    lintasan = l.split(", ")
    dari = lintasan[0]
    ke = lintasan[1]
    jarak = int(lintasan[2])
    graph.add_edge(dari, ke, jarak)
    pertanyaan()


def rute():
    r = input("Masukkan rute (dari, ke):")
    rute = r.split(", ")
    initial = rute[0]
    end = rute[1]
    print(findshorterspatch(graph, initial, end))
    pertanyaan()


def pertanyaan():
    w = input("Pilih Menu : ")
    if w == '1':
        kota()
    elif w == '2':
        lintasan()
    elif w == '3':
        rute()
    else:
        print("\nInvalid Key Input\n")


menu()
