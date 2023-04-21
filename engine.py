import os
import sys
import time


from character import Character
from enemies import ENEMIES
from event import Event
from items import ITEMS, DEFAULT_BACKPACK, DEFAULT_OUTFIT
from models import *


class Engine(Event, Character):
    """
    Contain game engines attributes and methods.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.chap = 0
        self.char = None
        self.teller = None

    def check_feedback(self, key_word):
        """Choose fucntion to launch based on key_word."""

        match key_word.strip().lower():
            case "b": self.show_bag()
            case "c": self.show_char()
            case "h": self.show_help()
            case _: return True

    def create_container(self, items):
        """Create container with stuff"""

        container = Container()
        container.add(self.create_item(items))
        return container # Do not change to one line

    def create_character(self, name):
        """Create players character."""

        self.char = Unit(name)
        self.char.bag = self.create_container(DEFAULT_BACKPACK)
        self.char.outfit = self.create_outfit(DEFAULT_OUTFIT)
        return self.char

    def create_enemy(self, enemy):
        """Create unit."""

        if enemy in ENEMIES:
            return Unit(**ENEMIES[enemy])
        else:
            raise KeyError(f"Couldn't create {enemy}!")

    def create_item(self, item_list):
        """Create items."""

        for idx, elem in enumerate(item_list):
            id, qty = elem
            if id in ITEMS:

                # Get the class name for item
                cls, _ = id.split(":")

                # Create an item object
                item = eval(f"{cls}(**ITEMS[id])")
                item.id = id
                item.qty = qty
                item_list[idx] = item
            else:
                raise KeyError(f"Couldn't create {id}")
        return item_list

    def create_outfit(self, items):
        """Create unit equipment."""

        outfit = Outfit()
        item_list = self.create_item(items)
        outfit.equip(*item_list)
        for item in item_list:
            self.char.inc_stat(item)
        return outfit

    def create_teller(self):
        """Create link to script generator."""

        self.teller = self.tell(self.get_chap(self.chap))
        return self.teller

    def end(self):
        sys.exit("Game over!")

    def get_chap(self, num):
        return f"script/chapter{num}.txt"

    def loader(self):
        self.teletype("Rogue's Adventure")
        time.sleep(1)
        input("Press 'Enter' to continue>>>")

    def next_chap(self, num):
        if os.path.isfile(self.get_chap(num)):
            self.create_teller()
        else: self.end()

    def show_help(self):
        with open("script/help.txt") as file:
            for line in file: print(line.rstrip())

    def tell(self, textfile):
        """Generator, read lines from textfile"""

        with open(textfile) as file:
            for line in file: yield line

    def teletype(self, string, delay=0.05):
        """Print text with delay."""

        for idx, letter in enumerate(string, 1):
            if idx == len(string) and letter != "\n":
                letter = f"{letter}\n"
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(delay)




