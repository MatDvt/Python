class Inventory:
    __capacity = 0

    def __init__(self, capacity):
        self.capacity = capacity
        Inventory.__capacity = capacity
        self.items = []

    def add_item(self, item):
        if len(self.items) < self.capacity:
            result = self.items.append(item)
            Inventory.__capacity -= 1
            return result
        return f"not enough room in the inventory"

    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {Inventory.__capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
