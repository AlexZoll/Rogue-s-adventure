from models import Armor


def test_init():
    attrs = {"name": "Leather gloves", "defense": 1, "slot": "hands", "desc": "Rough leather gloves"}
    armor = Armor(**attrs)
    assert armor.name == "Leather gloves"
    assert armor.desc == "Rough leather gloves"
    assert armor.defense == 1
    assert armor.slot == "hands"