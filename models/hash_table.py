class HashMap:
    '''
    HashMap implemented from the help of this video:
    # Source: https://www.youtube.com/watch?v=9HFbhPscPU0
    '''
    def __init__(self, size=40):
        self.size = size
        self.map = [None] * self.size
    
    def _get_hash(self, key: int) -> int:
        return key - 1
    
    def resize(self) -> object:
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
        key = package_id
        value = [delivery_address, delivery_deadline, delivery_city, delivery_zip, package_weight, delivery_status]
        key_hash = self._get_hash(key)
        key_value = [key, value]
        self.map[key_hash] = key_value
        return self

    
    def get(self, key: int) -> list:
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            return self.map[key_hash][1]
        return None

    def delete(self, key: int) -> object:
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        self.map[key_hash] = None
        return self
    
    def print(self) -> None:
        print('---PACKAGES----')
        for index, item in enumerate(self.map):
            if item is not None:
                print(index, item)