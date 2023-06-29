# https://www.youtube.com/watch?v=9HFbhPscPU0
class HashMap:
    def __init__(self, size=40):
        self.size = size
        self.map = [None] * self.size
    
    def _get_hash(self, key: int) -> int:
        return key - 1
    
    def resize(self):
        old_map = self.map
        self.size *= 2
        new_map = [None] * self.size
        for items in old_map:
            if items is not None:
                key, value = items
                key_hash = self._get_hash(key)
                key_value = [key, value]
                new_map[key_hash] = key_value
        self.map = new_map
        return self
    
    def insert(self, package_id: int, delivery_address: str, delivery_deadline: str, delivery_city: str, 
               delivery_zip: str, package_weight: str, delivery_status: str) -> bool:
        key = package_id
        if key > self.size:
            self.resize()
        value = [delivery_address, delivery_deadline, delivery_city, delivery_zip, package_weight, delivery_status]
        key_hash = self._get_hash(key)
        key_value = [key, value]
        self.map[key_hash] = key_value
        return self
    
    def update(self, package_id: int, delivery_address: str, delivery_deadline: str, delivery_city: str, 
            delivery_zip: str, package_weight: str, delivery_status: str) -> list:
        key = package_id
        value = [delivery_address, delivery_deadline, delivery_city, delivery_zip, package_weight, delivery_status]
        key_hash = self._get_hash(key)
        key_value = [key, value]
        self.map[key_hash] = key_value
        return self

    
    def get(self, key: int) -> list or None:
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            return self.map[key_hash][1]
        return None

    def delete(self, key: int) -> bool:
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        self.map[key_hash] = None
        return True
    
    def print(self) -> None:
        print('---PACKAGES----')
        for index, item in enumerate(self.map):
            if item is not None:
                print(index, item)