from aocutils import *
import random
import re
import networkx as nx


def main():
    graph = nx.Graph()
    with open(txt(), 'r') as file:
        for line in file.readlines():
            a, *n = re.findall("[a-z]{3}", line)
            for b in n:
                graph.add_edge(a, b, capacity=1)
    nodes = list(graph.nodes())
    cut = 0
    while cut != 3:
        cut, partition = nx.minimum_cut(graph, *random.choices(nodes, k=2))
        result = len(partition[0]) * len(partition[1])
    print(result)


if __name__ == "__main__":
    main()
