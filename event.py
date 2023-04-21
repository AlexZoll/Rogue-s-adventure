import random


from event_scripts import EVENTS
from items import ITEMS


class Event():
    """Mixing class to handle events."""

    def battle(self, event):
        """Make battle rounds and counting results"""

        # Get character
        char = self.char

        # Create enemy unit
        enemy = self.create_enemy(event["enemy"])

        def strike(atk, dfn):
            """Choose attack direction and set results."""

            # Player picks direction
            while True:
                char_dir = input("Choose strike direction: "\
                                 "1: head 2: body 3: legs\n>>>")
                if char_dir.strip() in ["1", "2", "3"]:
                    break
                else:
                    print("Wrong number! Try again")

            # Enemy picks direction
            enemy_dir = random.randint(1,3)

            if char_dir == enemy_dir:
                self.teletype(f"{atk.name} parry!", 0.02)
            else:
                dmg = max(random.randint(0, atk.stats["attack"])
                          - random.randint(0, dfn.stats["defense"]), 0)
                if dmg:
                    dfn.stats["hp_cur"] -= dmg
                    self.teletype(f"{atk.name} hit the {dfn.name} with {dmg} damage!", 0.03)
                else:
                    self.teletype(f"{atk.name} missed!", 0.03)

        # Start round
        self.teletype("-" * 20 + f"Prepare for battle with {enemy.name}!" +  "-" * 20, 0.03)
        while True:

            # Character turn
            strike(char, enemy)

            # Check for win
            if enemy.stats["hp_cur"] <= 0:
                self.teletype("-" * 20 + "Congratulations! You win the battle!" + "-" * 20)
                return self.start_event(event["next"])
            elif enemy.stats["hp_cur"] / enemy.stats["hp_max"] < 0.5:
                self.teletype(f"{enemy.name} looks hurt!", 0.03)
            elif enemy.stats["hp_cur"] / enemy.stats["hp_max"] < 0.2:
                self.teletype(f"{enemy.name} looks nearly dead!", 0.03)

            # Enemy turn
            strike(enemy, char)

            # Check for lose
            if char.stats["hp_cur"] <= 0:
                self.teletype("-" * 20 + "You've been defeated!" + "-" * 20)
                return 404
            else:
                self.teletype(f"{char.name} has {char.stats['hp_cur']}"\
                      f"/{char.stats['hp_max']} HP", 0.03)

    def check_event_result(self, num):
        match num:
            case 404: self.end()
            case _: return None

    def explore(self, event):
        """Create options to choose and start connected event."""

        while True:

            # Print options
            for idx, opt in enumerate(event["options"], 1):
                print(f"{idx}: {opt:<10}", end="")

            # Choose one option
            if (choice := input("\nChoose option>>>")).isdigit():
                if 0 < (choice := int(choice)) <= len(event["options"]):

                    # Print following description
                    self.teletype(event["desc"][choice-1])

                    # Start connected event
                    if val := self.start_event(event["next"][choice-1]):
                        return val
                else:
                    print("Wrong number! Try again")

            # Check input for special commands
            else: self.check_feedback(choice)


    def guide(self, event):
        """Output guide text and check palyers feedback."""

        with open(event["file"]) as file:
            for line in file:
                if line.startswith("!"):
                    while eval(f"{event['check']}"):
                        print(line.rstrip())
                        self.check_feedback(input(">>>"))
                else:
                    self.teletype(line.rstrip())
                    self.check_feedback(input(">>>"))

    def lockpick(self, event):
        """Emulate lockpicking process."""

        while True:
            if (choice := input("Wanna try to open?\n1: Yes   2: No\n>>>")).isdigit():
                if choice == "1":

                    # Check for lockpicks
                    if self.char.bag.items["Item:101"]:

                        # Try to open
                        self.char.bag.remove("Item:101", 1)
                        if random.randrange(100) > event["level"]:
                            self.teletype("You successfully open the lock!")

                            # Remove lockpick event from event chain
                            prev_event = EVENTS[event["next"]-2]
                            idx = prev_event["next"].index(event["next"]-1)
                            prev_event["next"][idx] = event["next"]

                            # Start connected event
                            return self.start_event(event["next"])

                        else: print("Failed to open lock!")
                    else:
                        print("You have no lockpicks!")
                        return None

                elif choice == "2": return None
                else: print("Wrong number! Try again")

            # Check input for special commands
            elif self.check_feedback(choice): return None


    def loot(self, event):
        """Create loot and interface to grab it."""

        print("-"*20 + "Let's take a look" + "-"*20)
        while True:
            if len(event["items"]):

                # Print item list
                for idx, elem in enumerate(event["items"], 1):
                    id, qty = elem
                    print(f"{idx}.{ITEMS[id]['name']}: {qty}   ", end="")
                print("0. All")
            else: return None

            # Choose option
            if (choice := input("Choose option>>>")).isdigit():
                if 0 < (choice := int(choice)) <= len(event["items"]):

                    # Get item from loot list
                    item = event["items"][choice-1]

                    # Create item object and put into backpack
                    self.char.bag.add(self.create_item([item]))

                    # Delete item from loot dict
                    del event["items"][choice-1]

                elif choice == 0:

                    # Remove all items to backpack
                    self.char.bag.add(self.create_item((event["items"])))
                    event["items"].clear()
                    return None
                else:
                    print("Wrong number! Try again")

            # Check input for special commands
            elif self.check_feedback(choice): return None


    def script(self, event):
        """Go back to script reading."""

        return "Read"

    def start_event(self, event_num):
            """Pick an event and launch it."""

            # Check if event exists
            if (event := EVENTS.get(event_num)):

                # Launch function based on event name
                return eval(f"self.{event['name']}(event)")
            else:
                return None


if __name__ == "__main__":
    ...