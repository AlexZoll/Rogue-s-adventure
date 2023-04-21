from models import Item


def test_init():
    item = Item("itemname", "do some stuff")
    assert item.name == "itemname"
    assert item.desc == "do some stuff"


def test_str():
    item = Item("itemname", "do some stuff")
    assert str(item) == "do some stuff"
