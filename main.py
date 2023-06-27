# Eric Crow 010762848
from utils.csv_reader import read_package_data, read_distance_data
from models.truck import Truck

def main():
    package_hash_map = read_package_data('data/WGUPS Package File.csv')
    distance_adjacency_list = read_distance_data('data/WGUPS Distance Table.csv')
    truck_one, truck_two, truck_three = Truck(), Truck(), Truck()
    truck_one_packages = [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40]
    truck_two_packages = [3, 6, 18, 25, 28, 32, 36, 38, 26, 27, 33, 35, 39]
    truck_three_packages = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 19, 21, 22, 23, 24]
    for package in truck_one_packages:
        truck_one.add(package_hash_map.get(package))
    for package in truck_two_packages:
        truck_two.add(package_hash_map.get(package))
    for package in truck_three_packages:
        truck_three.add(package_hash_map.get(package))

main()