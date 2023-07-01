# Eric Crow 010762848
from utils.csv_reader import read_package_data, read_distance_data
from models.truck import Truck
from models.hash_table import HashMap
from models.graph import AdjacencyList
from datetime import time, datetime, timedelta
import time as tm
import sys
from rich.console import Console
from rich.table import Table
import copy

# call read_package_data from csv_reader to get the HashMap of the package file data
PACKAGE_HASH_MAP = read_package_data('data/WGUPS Package File.csv')
# call read_distance_data from csv_reader to get an AdjacencyList containing the data points from the distance table
DISTANCE_ADJACENCY_LIST = read_distance_data('data/WGUPS Distance Table.csv')

# initialize global variables
WGU = '4001 South 700 East'
NOW = datetime.now()
TIME_DICT = {}
CONSOLE = Console()

def main() -> float:
    '''

    This is the main program. It initializes three truck objects, creates the datetime objects for each, loads the packages on the trucks 
    and then proceeds to call my greedy algorithm for each of them. It then returns the total miles traveled by all three trucks.

    Returns:
    float: The total miles traveled for all three trucks.

    Time Complexity: O(n^2)
    Space Complexity: O(n)

    '''
    # initialize three truck objects
    truck_one, truck_two, truck_three = Truck(), Truck(), Truck()
    # create a list of packages for each of the trucks to deliver
    truck_one_packages = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
    truck_two_packages = [3, 6, 18, 25, 28, 32, 36, 38, 26, 27, 33, 35, 39]
    truck_three_packages = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24]
    # base miles traveled for each of the trucks is set to zero
    miles = 0.0
    # initialize the times each of the trucks will begin delivering at
    time_one, time_two, time_three = time(8, 0), time(9, 5), time(10, 20)
    truck_one_time = datetime.combine(NOW, time_one)
    truck_two_time = datetime.combine(NOW, time_two)
    truck_three_time = datetime.combine(NOW, time_three)
    # load packages and call the greedy algorithm for trucks one and two
    load_packages(truck_one, truck_one_time, truck_one_packages)
    CONSOLE.print(f"\n[cyan]Truck one left WGU at {truck_one_time}.\n")
    truck_one_miles = greedy_algorithm(truck_one, DISTANCE_ADJACENCY_LIST, WGU, miles, truck_one_time, "one")
    load_packages(truck_two, truck_two_time, truck_two_packages)
    CONSOLE.print(f"\n[cyan]Truck two left WGU at {truck_two_time}.\n")
    truck_two_miles = greedy_algorithm(truck_two, DISTANCE_ADJACENCY_LIST, WGU, miles, truck_two_time, "two")
    # address for package 9 is changed at 10:20, when truck three has its packages loaded and begins delivering
    PACKAGE_HASH_MAP.update(9, "410 S State St", "EOD", "Salt Lake City", "84111", "2", "En route")
    # truck three has its packages loaded and the greedy algorithm called on it
    load_packages(truck_three, truck_three_time, truck_three_packages)
    CONSOLE.print(f"\n[cyan]Truck three left WGU at {truck_three_time}.\n")
    truck_three_miles = greedy_algorithm(truck_three, DISTANCE_ADJACENCY_LIST, WGU, miles, truck_three_time, "three")
    # add up and return the total amount of miles traveled by all three trucks
    total_miles = truck_one_miles + truck_two_miles + truck_three_miles
    return total_miles

def load_packages(truck: Truck, truck_time: datetime, packages: list[int]) -> None:
    '''
    This function adds the packages to the given truck, updates the HashMap, takes a snapshot of it,
    and then stores it in the time dictionary using the truck_time as the key.

    Parameters:
    truck (Truck): The current truck object the packages are being loaded onto.
    truck_time (datetime.datetime): The time the truck loads all of the packages.
    packages (list[int]): List of the id numbers of the packages that need to be loaded onto the truck.

    Time Complexity: O(n)
    Space Complexity: O(n) # due to the deepcopy (snapshot) of PACKAGE_HASH_MAP's current state.

    '''
    for package in packages:
        truck.add((package, PACKAGE_HASH_MAP.get(package)))
    for package in truck.packages:
        delivery_address, delivery_deadline, delivery_city, delivery_zip, package_weight, _ = package[1]
        # use deepcopy to take a snapshot of the current HashMap
        updated_hash_map = copy.deepcopy(PACKAGE_HASH_MAP.update(package[0], delivery_address, delivery_deadline, delivery_city, delivery_zip, package_weight, "En Route"))
        TIME_DICT[truck_time] = updated_hash_map

def greedy_algorithm(truck: Truck, distance_adjacency_list: AdjacencyList, starting_dest: str, miles: float, truck_time: datetime, truck_number: str) -> float:
    '''
    My implementation of the nearest neighbor algorithm using recursion.
    
    Parameters: 
    truck (Truck): The truck the algorithm is currently running on.
    distance_adjacency_list (AdjacencyList): Takes in the adjacency list containing the distances between every other point given in the provided matrix.
    starting_dest (str): The last address visited.
    miles (int): The current miles the truck has traveled. This is continually updated as the function is called recursively.
    truck_time (datetime.datetime): The current time in which the truck has been delivering packages. This is continually updated as the function is called recursively.
    truck_number (str): The number of the truck that is delivering packages.

    Returns:
    float: The total miles the truck had to travel to deliver all of the packages.

    Time Complexity: O(n^2)
    Space Complexity: O(n)

    '''
    lowest_distance = 100000
    # This for loop finds the lowest distance for delivering the next package from the current destination
    for package in truck.packages:
        distance = distance_adjacency_list.get_distance(starting_dest, package[1][0])
        if distance < lowest_distance:
            lowest_distance = distance
            closest_package = package
    # then we append miles
    miles += lowest_distance
    # then we calculate the time it takes to travel and append that to truck time
    traveled_time_in_mins = (lowest_distance / 18) * 60
    traveled_time = timedelta(minutes=traveled_time_in_mins)
    truck_time += traveled_time
    # then we remove the package that is delivered from our truck
    truck.packages.remove(closest_package)
    # then we take a snapshot of our hash map and add it to our time dictionary
    delivery_address, delivery_deadline, delivery_city, delivery_zip, package_weight, delivery_status = closest_package[1]
    delivery_status = f"Delivered {truck_time}"
    updated_hash_map = copy.deepcopy(PACKAGE_HASH_MAP.update(closest_package[0], delivery_address, delivery_deadline, delivery_city, delivery_zip, package_weight, delivery_status))
    TIME_DICT[truck_time] = updated_hash_map
    print(f"Truck {truck_number} delivered package {closest_package[0]} to {delivery_address} at {truck_time}")
    # this is the terminating condition which is met when there are no longer any packages on the truck
    if len(truck.packages) == 0:
        # return to WGU
        distance = distance_adjacency_list.get_distance(closest_package[1][0], WGU)
        traveled_time_in_mins = (distance / 18) * 60
        traveled_time = timedelta(minutes=traveled_time_in_mins)
        truck_time += traveled_time
        miles += distance
        CONSOLE.print(f"\n[green]Truck {truck_number} returned to WGU at {truck_time}.\n\nTotal distance traveled for truck {truck_number} was {miles} miles.[/green]\n")
        tm.sleep(1)
        return miles
    # recursively call our algorithm until the terminating condition is met
    return greedy_algorithm(truck, distance_adjacency_list, closest_package[1][0], miles, truck_time, truck_number)

def return_dict_values(inputted_time: datetime) -> HashMap:
    '''
    Function for reversing my time dictionary and returning the first HashMap whose key value is less than or equal to inputted_time.

    Found information on reversing the dictionary in the link below under "Method #6: Using the sorted() function and a lambda function":
    # Source: https://www.geeksforgeeks.org/python-reverse-dictionary-keys-order/
    
    Parameters:
    inputted_time (datetime.datetime): The time up to when the values should be returned.

    Returns:
    HashMap: Returns the snapshot of the HashMap in which its key value is less than or equal to inputted_time.

    Time Complexity: O(n log n) # due to the sorted function being called on TIME_DICT
    Space Complexity: O(n)

    '''
    time_dict_reversed = {k: TIME_DICT[k] for k in sorted(TIME_DICT, key=lambda x: list(TIME_DICT.keys()).index(x), reverse=True)}
    for key, value in time_dict_reversed.items():
        if key <= inputted_time:
            return value

def display_single_package_information(inputted_time: datetime, package_id_number: int) -> None:
    '''
    This is a function for returning and displaying a single package by its id number given the current time.
    Displays them in a table using the rich library.

    Parameters:
    inputted_time (datetime.datetime): The time up to when the package was last updated should be returned.
    package_id_number (int): The id number of the package. Necessary for the lookup function that has been implemented in my HashMap.

    Time Complexity: O(n log n)
    Space Complexity: O(n)

    '''
    # call the return dict values to get the first HashMap whose key value is less than or equal to inputted_time
    values = return_dict_values(inputted_time)
    CONSOLE.print(f"Status time: {inputted_time}")
    # create a table and add columns to display the information in an easy to read format
    table = Table(show_header=True)
    table.add_column("Package ID")
    table.add_column("Delivery Address")
    table.add_column("Delivery Deadline")
    table.add_column("Delivery City")
    table.add_column("Delivery Zip Code")
    table.add_column("Package Weight (KILOS)")
    table.add_column("Delivery Status")
    # retrieve a single package using the lookup function implemented in my HashMap
    single_package = values.get(package_id_number)
    # conditonal statement for determing what colors to display the row in (based on its delivery status)
    if "Delivered" in single_package[5]:
        color = "green"
    elif single_package[5] == "En Route":
        color = "yellow"
    else:
        color = "red"
    # create the row based on the values retrieved from the variable single_package
    table.add_row(f"[{color}]{str(package_id_number)}", f"[{color}]{single_package[0]}", f"[{color}]{single_package[1]}", f"[{color}]{single_package[2]}", 
                f"[{color}]{single_package[3]}", f"[{color}]{single_package[4]}", f"[{color}]{single_package[5]}")
    # prints the table to the terminal
    return CONSOLE.print(table)

def display_all_package_information(inputted_time: datetime) -> None:
    '''
    This is a function for returning and displaying all by packages current status given the inputted time.
    Displays them in a table using the rich library.

    Parameters:
    inputted_time (datetime.datetime): The time up to when the time dictionary was last updated should be returned.

    Time Complexity: O(n log n)
    Space Complexity: O(n)

    '''
    # call the return dict values to get the first HashMap whose key value is less than or equal to inputted_time
    values = return_dict_values(inputted_time)
    CONSOLE.print(f"Status time: {inputted_time}")
    # create a table and add columns to display the information in an easy to read format
    table = Table(show_header=True)
    table.add_column("Package ID")
    table.add_column("Delivery Address")
    table.add_column("Delivery Deadline")
    table.add_column("Delivery City")
    table.add_column("Delivery Zip Code")
    table.add_column("Package Weight (KILOS)")
    table.add_column("Delivery Status")
    # iterate through the HashMap that is returned through calling return_dict_values and add rows to the table with each of the package's information
    for item in values.map:
        if "Delivered" in item[1][5]:
            color = "green"
        elif item[1][5] == "En Route":
            color = "yellow"
        else:
            color = "red"
        table.add_row(f"[{color}]{str(item[0])}", f"[{color}]{item[1][0]}", f"[{color}]{item[1][1]}", f"[{color}]{item[1][2]}", 
                      f"[{color}]{item[1][3]}", f"[{color}]{item[1][4]}", f"[{color}]{item[1][5]}")
    # prints the table to the terminal
    return CONSOLE.print(table)
        
if __name__ == "__main__":
    ''' 

    Calls the main() function and then starts a while loop so users can interact and find packages by status time.
    
    '''
    CONSOLE.print('\n[cyan]Welcome to WGUSPS Routing!\n')
    tm.sleep(0.75)
    print('Starting program...\n')
    tm.sleep(0.75)
    print('Delivering packages...\n')
    tm.sleep(0.25)
    miles = main()
    print('All packages have been delivered!\n\n')
    print(f'Total mileaged traveled by all trucks: {miles} miles\n')
    while True:
        print('Enter a time to view the status of the packages\n')
        command = input("> ")
        if command.lower().strip() == "exit":
            print('Goodbye!\n')
            sys.exit(0)
        else:
            try:
                hour, minute = command.split(":")
                hour, minute = int(hour), int(minute)
                inputted_time = time(hour, minute)
                inputted_time = datetime.combine(NOW, inputted_time)
                print("\na - Display all packages\ni - Search by package ID number\n")
                while True:
                    command = input("> ")
                    if command.lower().strip() == "a":
                        display_all_package_information(inputted_time)
                        break
                    elif command.lower().strip() == "i":
                        print("Enter package ID number\n")
                        command = input("> ")
                        package_id_number = int(command.strip())
                        display_single_package_information(inputted_time, package_id_number)
                        break
                    else:
                        print("Please input either 'a' or 'i'.")
            except ValueError:
                print("Please input time in this format HH:MM\n")


