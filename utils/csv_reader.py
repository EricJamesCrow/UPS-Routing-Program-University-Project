from models.hash_table import HashMap
from models.graph import AdjacencyList
from itertools import islice
import csv

def read_package_data(file: str) -> HashMap:
    h = HashMap()
    with open(file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in islice(readCSV, 5, None):
            package_id = int(row[0])
            delivery_address = row[1]
            delivery_deadline = row[5]
            delivery_city = row[2]
            delivery_zip = row[4]
            delivery_weight = row[6]
            h.insert(package_id, delivery_address, delivery_deadline, delivery_city, delivery_zip, delivery_weight, 'At the hub')
    return h

def read_distance_data(file: str) -> AdjacencyList:
    adjList = AdjacencyList()
    vertexes = []
    reader = csv.reader(open(file), delimiter=',')
    headers = next(islice(reader, 4, None))
    for h in headers[2:]:
        h = h.split('\n')
        address = h[1].replace(',', '').strip()
        new_vertex = address
        vertexes.append(new_vertex)
        adjList.add_vertex(new_vertex)
    index = 0
    for lst in reader:
        counter = 0
        for obj in lst[2:]:
            if obj == '':
                continue
            distance = float(obj)
            adjList.add_undirected_edge(vertexes[index], vertexes[counter], distance)
            counter += 1
        index += 1
    return adjList
