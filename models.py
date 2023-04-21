class Container:
    """
    Base class to contain stuff.

    .add(items) to add item
    .remove(items) to remove item
    """

    def __init__(self, capacity=50):
        self.capacity = capacity
        self.items = {}
        self.weight = 0

    def add(self, item_dict):
        """Add item."""

        for obj in item_dict:
            if obj.id in self.items:
                self.items[obj.id].qty += obj.qty
            else:
                self.items[obj.id] = obj

    def remove(self, id, qty):
        """Remove item."""

        if self.items[id].qty - qty == 0:
            return self.items.pop(id)
        elif self.items[id].qty - qty < 0:
            raise ValueError("Not enough {name}!")
        else:
            self.items[id].qty -= qty

    def __str__(self):
        return ",   ".join(f"{idx}. '{obj.name}: {obj.qty}'"
                           for idx, obj in enumerate(self.items.values(), 1))


class Item():
    """Base class for all items."""

    def __init__(self, name, desc, qty=1):
        self.name = name
        self.desc = desc
        self.qty = qty

    def __str__(self):
        return f"{self.desc}"


class Unit:
    """Base class for any unit with atributes."""

    def __init__(self, name, hp=30, attack=1, defense=1):
        self.bag = None
        self.name = name
        self.outfit = None
        self.stats = {
            "attack": attack,
            "defense": defense,
            "hp_cur": hp,
            "hp_max": hp,
        }


    def inc_stat(self, obj):
        """Increase stats based on obj stats."""
        for stat in self.stats:
            if num := getattr(obj, stat, None):
                self.stats[stat] += num

    def dec_stat(self, obj):
        """Decrease stats based on obj stats."""

        for stat in self.stats:
            if num := getattr(obj, stat, None):
                self.stats[stat] -= num

    def __str__(self):
        return (f"Name: {self.name}, "\
            f"HP: {self.stats['hp_cur']}/{self.stats['hp_max']}, "\
            f"Atack: {self.stats['attack']}, "\
            f"Defense: {self.stats['defense']}")

    def consume(self, obj):
        if hp := getattr(obj, "hp_cur", None):
            if self.stats["hp_cur"] + hp > self.stats["hp_max"]:
                self.stats["hp_cur"] = self.stats["hp_max"]
                print(f"You restored maximum hit points!")
            else:
                self.stats["hp_cur"] += hp
                print(f"You restored {hp} hit points!")
        else: self.inc_stat(obj)



class Potion(Item):
    """Base class for potions."""

    def __init__(self, name, desc):
        super().__init__(name, desc)
        self.consumable = True


class Heal_pot(Potion):
    """Base class for healing potions."""

    def __init__(self, name, hp, desc):
        super().__init__(name, desc)
        self.hp_cur = hp


class Outfit():
    """
    Contain all characters equipment.

    Use .equip(item) to add item
    Use .unequip(item) to remove item
    """

    def __init__(self):
        self.items = {
            "main_hand": None,
            "off_hand": None,
            "body": None,
            "head": None,
            "hands": None,
            "shoulders": None,
            "feet": None,
            "finger": None,
            "neck": None,
            "waist": None
        }

    def __str__(self):
        return ", ".join(f"{idx}. {elem[0]}: {elem[1].name}"
                         for idx, elem in enumerate(self.items.items(), 1)
                         if elem[1])

    def equip(self, *item_list):
        """Equip item."""

        for item in item_list:
            self.items[item.slot] = item

    def unequip(self, slot):
        """Unequip item."""

        if item := self.items.get(slot):
            self.items[slot] = None
            return item
        else:
            print("Nothing to unequip!")


class Equipment(Item):
     """Base class for equimpent."""

     def __init__(self, name, slot, desc):
        super().__init__(name, desc)
        self.slot = slot


class Weapon(Equipment):
    """Base class for weapon."""

    def __init__(self, name, attack, slot, desc):
        super().__init__(name, slot, desc)
        self.attack = attack


class Armor(Equipment):
    """Base class for armor."""

    def __init__(self, name, defense, slot, desc):
        super().__init__(name, slot, desc)
        self.defense = defense


