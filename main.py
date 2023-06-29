# Eric Crow 010762848
from utils.csv_reader import read_package_data, read_distance_data
from models.truck import Truck
from datetime import time, datetime, timedelta
import time as tm
import sys
from rich.console import Console
from rich.table import Table

package_hash_map = read_package_data('data/WGUPS Package File.csv')
distance_adjacency_list = read_distance_data('data/WGUPS Distance Table.csv')

now = datetime.now()
time_dict = {}
console = Console()

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
    time_one, time_two, time_three = time(8, 0), time(9, 5), time(10, 15)
    truck_one_time = datetime.combine(now, time_one)
    truck_two_time = datetime.combine(now, time_two)
    truck_three_time = datetime.combine(now, time_three)
    load_packages(truck_one, truck_one_time)
    truck_one_miles = greedy_algorithm(truck_one, distance_adjacency_list, hub, miles, truck_one_time)
    load_packages(truck_two, truck_two_time)
    truck_two_miles = greedy_algorithm(truck_two, distance_adjacency_list, hub, miles, truck_two_time)
    load_packages(truck_three, truck_three_time)
    truck_three_miles = greedy_algorithm(truck_three, distance_adjacency_list, hub, miles, truck_three_time)
    total_miles = truck_one_miles + truck_two_miles + truck_three_miles
    return total_miles

def load_packages(truck, truck_time):
    for package in truck.packages:
        delivery_address, delivery_deadline, delivery_city, delivery_zip, package_weight, delivery_status = package[1]
        updated_hash_map = package_hash_map.update(package[0], delivery_address, delivery_deadline, delivery_city, delivery_zip, package_weight, "En Route").copy()
        time_dict[truck_time] = updated_hash_map

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
    delivery_status = f"Delivered {truck_time}"
    updated_hash_map = package_hash_map.update(closest_package[0], delivery_address, delivery_deadline, delivery_city, delivery_zip, package_weight, delivery_status).copy()
    time_dict[truck_time] = updated_hash_map
    if len(truck.packages) == 0:
        # return to hub
        distance = distance_adjacency_list.get_distance(closest_package[1][0], '4001 South 700 East')
        miles += distance
        return miles
    return greedy_algorithm(truck, distance_adjacency_list, closest_package[1][0], miles, truck_time)

def return_dict_values(inputted_time):
    time_dict_reversed = {k: time_dict[k] for k in sorted(time_dict, key=lambda x: list(time_dict.keys()).index(x), reverse=True)}
    for key, value in time_dict_reversed.items():
        if key <= inputted_time:
            return value

def display_all_package_information(inputted_time):
    values = return_dict_values(inputted_time)
    table = Table(show_header=True)
    table.add_column("Package ID")
    table.add_column("Delivery Address")
    table.add_column("Delivery Deadline")
    table.add_column("Delivery City")
    table.add_column("Delivery Zip Code")
    table.add_column("Package Weight (KILOS)")
    table.add_column("Delivery Status")
    for item in values:
        if "Delivered" in item[1][5]:
            color = "green"
        elif item[1][5] == "En Route":
            color = "yellow"
        else:
            color = "red"
        table.add_row(f"[{color}]{str(item[0])}", f"[{color}]{item[1][0]}", f"[{color}]{item[1][1]}", f"[{color}]{item[1][2]}", 
                      f"[{color}]{item[1][3]}", f"[{color}]{item[1][4]}", f"[{color}]{item[1][5]}")
    console.print(table)
        
if __name__ == "__main__":
    print('Welcome to WGUSPS Routing!\n')
    tm.sleep(1)
    print('Starting program...\n')
    tm.sleep(1)
    print('Delivering packages...\n')
    tm.sleep(1)
    miles = main()
    print('All packages have been delivered!\n\n')
    print(f'Total mileaged traveled by trucks: {miles} miles\n')
    print('Enter a time to view the status of the packages\n')
    while True:
        command = input(">")
        if command.lower().strip() == "exit":
            print('Goodbye!\n')
            sys.exit(0)
        else:
            hour, minute = command.split(":")
            hour, minute = int(hour), int(minute)
            inputted_time = time(hour, minute)
            inputted_time = datetime.combine(now, inputted_time)
            display_all_package_information(inputted_time)

