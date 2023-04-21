import pytest


from models import Container


def test_init():
    bp = Container(30)
    assert bp.capacity == 30


def test_str():
    bp = Container()
    assert str(bp) == ""


def test_add():
    class Test:
        ...
    hpot = Test()
    hpot.name = "health potion"
    hpot.qty = 1
    hpot.id = "1"
    bp = Container()
    bp.add([hpot, hpot])
    assert str(bp) == "1. 'health potion: 2'"
    hpot = Test()
    hpot.name = "health potion"
    hpot.qty = 1
    hpot.id = "1"
    bp.add([hpot])
    assert str(bp) == "1. 'health potion: 3'"


def test_remove():
    class Test:
        ...
    hpot = Test()
    hpot.name = "health potion"
    hpot.qty = 3
    hpot.id = "1"
    bp = Container()
    bp.add([hpot])
    bp.remove(hpot.id, 1)
    assert str(bp) == "1. 'health potion: 2'"
    with pytest.raises(ValueError):
        assert bp.remove("1", 5)
    item = bp.remove("1", 2)
    assert item.qty == 2

