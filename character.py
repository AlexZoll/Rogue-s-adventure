class Character():
    """Mixing class to handle character."""

    def show_bag(self):
        """Allow to interact with bag content."""

        print("-"*20 + "Character's backpack" + "-"*20)
        while True:
            print(self.char.bag)

            # Choose item to use
            if (choice := input("Choose item>>>")).isdigit():
                if 0 < (choice := int(choice)) <= len(self.char.bag.items):

                    # Find chosen item
                    for idx, obj in enumerate(self.char.bag.items.values(), 1):
                        if idx == choice and obj: break
                    print(obj)

                    # Equip item
                    if hasattr(obj, "slot"):
                        choice = input("1.equip\n>>>")
                        if choice == "1":
                            self.char.outfit.equip(obj)
                            self.char.bag.remove(obj.id, 1)
                            self.char.inc_stat(obj)

                    # Use item
                    elif hasattr(obj, "consumable"):
                        choice = input("1.use\n>>>")
                        if choice == "1":
                            self.char.consume(obj)
                            self.char.bag.remove(obj.id, 1)
                else:
                    print("Wrong number! Try again")
            else: return None

    def show_char(self):
        """Show character stats and equipment."""

        print("-"*20 + "Character list" + "-"*20)
        while True:
            print(self.char)
            print(self.char.outfit)

            # Choose item to unequip
            if (choice := input("Choose item to unequip>>>")).isdigit():
                if 0 < (choice := int(choice)) <= len(self.char.outfit.items):

                    # Find chosen item and unequip
                    for idx, obj in enumerate(self.char.outfit.items.values(), 1):
                        if idx == choice and obj: break
                    self.char.outfit.unequip(obj.slot)
                    self.char.bag.add([obj])
                    self.char.dec_stat(obj)
                else:
                    print("Wrong number! Try again")
            else: return None