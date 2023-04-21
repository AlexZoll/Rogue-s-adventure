from models import Heal_pot, Container, Unit


def test_init():
    potion = Heal_pot("potionname", 5, "do some stuff")
    assert potion.name == "potionname"
    assert potion.desc == "do some stuff"
    assert potion.hp_cur == 5


def test_str():
    item = Heal_pot("itemname", 5, "do some stuff")
    assert str(item) == "do some stuff"


