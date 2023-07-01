from models.hash_table import HashMap
from models.graph import AdjacencyList
from itertools import islice
import csv

def read_package_data(file: str) -> HashMap:
    '''
    Reads in package data from the provided csv and inserts each row into the HashMap.

    Parameters:
    file (str): The file path to the csv.

    Returns:
    HashMap: HashMap of the package data.

    Time Complexity: O(n)
    Space Complexity: O(n)

    '''
    h = HashMap()
    with open(file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # skip first five lines of the file, iterate through each row and then add the corresponding data elements to the HashMap
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
    '''
    Reads in the distance data from the provided csv and inserts each point into an AdjacencyList.

    Parameters:
    file (str): The file path to the csv.

    Returns:
    AdjacencyList: An AdjacencyList containing all of the distance data from the provided csv.

    
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)

    '''
    # intialize an AdjacencyList
    adjList = AdjacencyList()
    # initialize list of addresses
    addresses = []
    reader = csv.reader(open(file), delimiter=',')
    # start reading at the fifth line of the file
    headers = next(islice(reader, 4, None))
    # iterate through and add all of the addresses located in the headers to the addresses list and adjList
    for h in headers[2:]:
        h = h.split('\n')
        address = h[1].replace(',', '').strip()
        new_vertex = address
        addresses.append(new_vertex)
        adjList.add_vertex(new_vertex)
    index = 0
    # iterate through the file
    for lst in reader:
        # set counter to zero to insure all of the addresses for each row are grabbed
        counter = 0
        # iterate through the current line
        for obj in lst[2:]:
            if obj == '':
                continue
            distance = float(obj)
            # add edge to the adjacency list
            adjList.add_undirected_edge(addresses[index], addresses[counter], distance)
            counter += 1
        index += 1
    return adjList
