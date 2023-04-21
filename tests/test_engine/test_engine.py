import pytest


from engine import Engine
from models import Unit


def test_new():
    eng1 = Engine()
    eng2 = Engine()
    assert eng1 is eng2


def test_init():
    eng = Engine()
    assert eng.chap == 0
    assert eng.char == None


def test_check_feedback():
    eng = Engine()
    assert eng.check_feedback("none") == True
    with pytest.raises(AttributeError):
        assert eng.check_feedback("c")
        assert eng.check_feedback("b")
    assert eng.check_feedback("h") == print("Type 'b' to open character bag\n"\
                                            "Type 'c' to open character list")


def test_get_chap():
    eng = Engine()
    assert eng.get_chap(2) == "script/chapter2.txt"


def test_tell():
    eng = Engine()
    gen = eng.tell("tests/test_engine/test.txt")
    assert next(gen) == "test1\n"
    assert next(gen) == "test2\n"


def test_create_item():
    eng = Engine()
    items = eng.create_item([("Item:100", 10), ("Item:101", 3)])
    assert items[0].name == "Gold"
    assert items[0].qty == 10
    assert items[1].qty == 3
    assert items[1].id == "Item:101"


def test_create_container():
    eng = Engine()
    eng.char = Unit("tester")
    bp = eng.create_container([('Weapon:300', 1), ('Item:100', 10), ('Item:101', 3)])
    assert bp.items['Item:100'].qty == 10
    assert str(bp) == "1. 'Short sword: 1',   2. 'Gold: 10',   3. 'Lockpick: 3'"


def test_create_character():
    eng = Engine()
    char = eng.create_character(name="tester")
    assert str(char) == "Name: tester, HP: 30/30, Atack: 1, Defense: 5"
    assert str(char.outfit) == "3. body: Leather jacket, 5. hands: Leather gloves, 7. feet: Leather boots"
    assert str(char.bag) == "1. 'Gold: 10',   2. 'Lockpick: 3',   3. 'Short sword: 1',   4. 'Lesser healing potion: 1'"


def test_create_enemy():
    eng = Engine()
    with pytest.raises(KeyError):
        eng.create_enemy("Noname")
    enemy = eng.create_enemy("Unit:001")
    assert enemy.name == "Necromancer"
    assert enemy.stats["hp_max"] == 20
    assert enemy.stats["attack"] == 7
    assert enemy.stats["defense"] == 2


def test_create_outfit():
    eng = Engine()
    eng.char = Unit("tester")
    ouf = eng.create_outfit([('Armor:200', 1), ('Armor:201', 1)])
    assert str(ouf) == "3. body: Leather jacket, 7. feet: Leather boots"
    assert eng.char.stats["defense"] == 4


def test_create_teller():
    eng = Engine()
    gen = eng.create_teller()
    assert next(gen) == "__________PROLOGUE__________\n"


def test_end():
    eng = Engine()
    with pytest.raises(SystemExit):
        assert eng.end()


def test_next_chap():
    eng = Engine()
    eng.next_chap(0)
    next(eng.teller) == print("__________PROLOGUE__________")
    with pytest.raises(SystemExit):
        assert eng.next_chap(99)


def test_show_help():
    eng = Engine()
    assert eng.show_help() == print("Type 'b' to open character bag\n"\
                                        "Type 'c' to open character list")


def test_teletype():
    eng = Engine()
    assert eng.teletype("test", 0.1) == print("test")