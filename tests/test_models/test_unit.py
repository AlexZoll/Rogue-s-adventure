from models import Unit


def test_init():
    char = Unit("char_name", 15, 1, 2)
    assert char.name == "char_name"
    assert char.stats["hp_cur"] == 15
    assert char.stats["hp_max"] == 15
    assert char.stats["attack"] == 1
    assert char.stats["defense"] == 2


def test_str():
    char = Unit("char_name", 15, 1, 2)
    assert str(char) == "Name: char_name, HP: 15/15, Atack: 1, Defense: 2"


def test_consume():
    class Test:
        ...
    hpot = Test()
    hpot.hp_cur = 15
    char = Unit(name="tester", hp=30, attack=1, defense=1)
    char.stats["hp_cur"] = 10
    assert char.consume(hpot) == print("You restored 15 hit points!")
    assert char.stats["hp_cur"] == 25
    assert char.consume(hpot) == print("You restored max hit points!")
    assert char.stats["hp_cur"] == 30


def test_inc_stat():
    class Test:
        ...
    arm = Test()
    arm.attack = 5
    char = Unit(name="tester", hp=30, attack=1, defense=1)
    char.inc_stat(arm)
    assert char.stats["attack"] == 6
    assert char.stats["defense"] == 1


def test_dec_stat():
    class Test:
        ...
    arm = Test()
    arm.attack = 5
    char = Unit(name="tester", hp=30, attack=6, defense=1)
    char.dec_stat(arm)
    assert char.stats["attack"] == 1
    assert char.stats["defense"] == 1
