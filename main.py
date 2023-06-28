# Eric Crow 010762848
from utils.csv_reader import read_package_data, read_distance_data
from models.truck import Truck
from datetime import time, timedelta

package_hash_map = read_package_data('data/WGUPS Package File.csv')
distance_adjacency_list = read_distance_data('data/WGUPS Distance Table.csv')

time_dict = {}

def main():
    truck_one, truck_two, truck_three = Truck(), Truck(), Truck()
    truck_one_packages = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
    truck_two_packages = [3, 6, 18, 25, 28, 32, 36, 38, 26, 27, 33, 35, 39]
    truck_three_packages = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24]
    for package in truck_one_packages:
        truck_one.add((package, package_hash_map.get(package)))
    for package in truck_two_packages:
        truck_two.add((package, package_hash_map.get(package)))
    for package in truck_three_packages:
        truck_three.add((package, package_hash_map.get(package)))
    hub, miles = '4001 South 700 East', 0
    truck_one_time, truck_two_time, truck_three_time = time(8, 0), time(9, 5), time(10, 15)
    truck_one_miles = greedy_algorithm(truck_one, distance_adjacency_list, hub, miles, truck_one_time)
    truck_two_miles = greedy_algorithm(truck_two, distance_adjacency_list, hub, miles, truck_two_time)
    truck_three_miles = greedy_algorithm(truck_three, distance_adjacency_list, hub, miles, truck_three_time)
    total_miles = truck_one_miles + truck_two_miles + truck_three_miles
    print(time_dict)

def greedy_algorithm(truck, distance_adjacency_list, starting_dest, miles, truck_time):
    lowest_distance = 100000
    for package in truck.packages:
        distance = distance_adjacency_list.get_distance(starting_dest, package[1][0])
        if distance < lowest_distance:
            lowest_distance = distance
            closest_package = package
    miles += lowest_distance
    traveled_time = lowest_distance / 18
    traveled_time_in_mins = traveled_time * 60
    traveled_time = timedelta(minutes=traveled_time_in_mins)
    truck_time = truck_time + traveled_time
    truck.packages.remove(closest_package)
    delivery_address, delivery_deadline, delivery_city, delivery_zip, package_weight, delivery_status = closest_package[1]
    delivery_status = "delivered"
    updated_hash_map = package_hash_map.update(closest_package[0], delivery_address, delivery_deadline, delivery_city, delivery_zip, package_weight, delivery_status)
    time_dict[truck_time] = updated_hash_map
    if len(truck.packages) == 0:
        # return to hub
        distance = distance_adjacency_list.get_distance(closest_package[1][0], '4001 South 700 East')
        miles += distance
        return miles
    return greedy_algorithm(truck, distance_adjacency_list, closest_package[1][0], miles)

        

main()