from models import Potion


def test_init():
    potion = Potion("potionname", "do some stuff")
    assert potion.name == "potionname"
    assert potion.desc == "do some stuff"


def test_str():
    item = Potion("itemname", "do some stuff")
    assert str(item) == "do some stuff"
