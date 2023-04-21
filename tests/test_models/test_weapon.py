from models import Weapon


def test_init():
    attrs = {"name":"sword", "attack": 3, "slot": "main_hand", "desc": "sword description"}
    weapon = Weapon(**attrs)
    assert weapon.name == "sword"
    assert weapon.desc == "sword description"
    assert weapon.attack == 3
    assert weapon.slot == "main_hand"