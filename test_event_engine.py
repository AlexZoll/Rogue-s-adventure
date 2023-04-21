import sys


from engine import Engine
from event_scripts import EVENTS
from models import Container, Outfit, Unit


def test_battle():
    eng = Engine()
    eng.char = Unit("Tester")
    eng.char.outfit = eng.create_outfit([("Armor:200", 1), ("Armor:201", 1), ("Armor:202", 1), ("Weapon:300", 1)])
    eng.battle(EVENTS[202])


def test_explore():
    eng = Engine()
    eng.char = Unit("Tester")
    eng.char.bag = Container()
    eng.char.bag.add(eng.create_item([("Item:101", 3)]))
    eng.explore(EVENTS[300])


def test_guide():
    eng = Engine()
    eng.char = Unit("Tester")
    eng.char.bag = Container()
    eng.char.outfit = Outfit()
    eng.char.bag.add(eng.create_item([("Heal_pot:400", 1),("Item:101", 3),("Weapon:300", 1)]))
    eng.guide(EVENTS[203])


def test_lockpick():
    eng = Engine()
    eng.char = Unit("Tester")
    eng.char.bag = Container()
    eng.char.bag.add(eng.create_item([("Item:101", 3)]))
    eng.lockpick(EVENTS[301])


def test_loot():
    eng = Engine()
    eng.char = Unit("Tester")
    eng.char.bag = Container()
    eng.loot(EVENTS[302])


def test_show_bag():
    eng = Engine()
    eng.char = Unit("Tester")
    eng.char.bag = Container()
    eng.char.outfit = Outfit()
    eng.char.bag.add(eng.create_item([("Item:100", 10),("Item:101", 3),("Weapon:300", 1)]))
    eng.show_bag()


def test_show_char():
    eng = Engine()
    eng.char = Unit("Tester")
    eng.char.bag = Container()
    eng.char.outfit = eng.create_outfit([("Armor:200", 1), ("Armor:201", 1), ("Armor:202", 1)])
    eng.show_char()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        eval(f"test_{sys.argv[1]}()")