class HashMap:
    '''
    HashMap implemented from the help of this video:
    # Source: https://www.youtube.com/watch?v=9HFbhPscPU0
    
    Added resize method to meet the self-adjusting requirement.
    Modified the _get_hash method to something much more simple and reliable for my use case.

    '''
    def __init__(self, size=40):
        self.size = size
        self.map = [None] * self.size
    
    def _get_hash(self, key: int) -> int:
        '''
        Method to create the hash for the package.

        Parameters:
        key (int): The key (package id) used to create the hash.

        Returns:
        int: Returns the hash for the package.

        Time Complexity: O(1)
        Space Complexity: O(1)
        
        '''
        return key - 1
    
    def resize(self) -> object:
        '''
        Resizes HashMap by twice its size when called.

        Returns:
        object: Returns itself (the HashMap object)

        Time Complexity: O(n)
        Space Complexity: O(n)

        '''
        old_map = self.map
        self.size *= 2
        new_map = [None] * self.size
        for item in old_map:
            if item is not None:
                key, value = item
                key_hash = self._get_hash(key)
                key_value = [key, value]
                new_map[key_hash] = key_value
        self.map = new_map
        return self
    
    def insert(self, package_id: int, delivery_address: str, delivery_deadline: str, delivery_city: str, 
               delivery_zip: str, package_weight: str, delivery_status: str) -> object:
        '''
        Insert function for the HashMap.

        Parameters:
        package_id (int): The package id number.
        delivery_address (str): The delivery address for the package.
        delivery_deadline (str): The delivery deadline for the package.
        delivery_city (str): The delivery city for the package.
        delivery_zip (str): The delivery zip code for the package.
        package_weight (str): The weight of the package (KILOS).
        delivery_status (str): The delivery status of the package.

        Returns:
        object: Returns itself (the HashMap object)

        Time Complexity: O(1), O(n) if resize gets triggered
        Space Complexity: O(1)

        '''
        key = package_id
        if key > self.size:
            self.resize()
        value = [delivery_address, delivery_deadline, delivery_city, delivery_zip, package_weight, delivery_status]
        key_hash = self._get_hash(key)
        key_value = [key, value]
        self.map[key_hash] = key_value
        return self
    
    def update(self, package_id: int, delivery_address: str, delivery_deadline: str, delivery_city: str, 
            delivery_zip: str, package_weight: str, delivery_status: str) -> object:
        '''
        Update function for the HashMap.

        Parameters:
        package_id (int): The package id number.
        delivery_address (str): The delivery address for the package.
        delivery_deadline (str): The delivery deadline for the package.
        delivery_city (str): The delivery city for the package.
        delivery_zip (str): The delivery zip code for the package.
        package_weight (str): The weight of the package (KILOS).
        delivery_status (str): The delivery status of the package.

        Returns:
        object: Returns itself (the HashMap object)

        Time Complexity: O(1)
        Space Complexity: O(1)


        '''
        key = package_id
        value = [delivery_address, delivery_deadline, delivery_city, delivery_zip, package_weight, delivery_status]
        key_hash = self._get_hash(key)
        key_value = [key, value]
        self.map[key_hash] = key_value
        return self
  
    def get(self, key: int) -> list:
        '''
        Lookup function for the HashMap

        Parameters:
        key (int): The package id number.

        Returns:
        list: Returns a list which contains the package data.

        Time Complexity: O(1)
        Space Complexity: O(1)

        '''
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            return self.map[key_hash][1]
        return None