from models import Outfit


def test_equip():
    class Test:
        ...
    item1 = Test()
    item2 = Test()
    item1.slot, item2.slot = "head", "body"
    item1.name, item2.name = "helm", "armor"
    outf = Outfit()
    outf.equip(item1)
    outf.equip(item2)
    assert outf.items["head"] == item1
    assert outf.items["body"] == item2
    assert str(outf) == "3. body: armor, 4. head: helm"


def test_unequip():
    class Test:
        ...
    item1 = Test()
    item2 = Test()
    item1.slot, item2.slot = "head", "body"
    item1.name, item2.name = "helm", "armor"
    outf = Outfit()
    outf.equip(item1)
    outf.equip(item2)
    assert outf.unequip("head") == item1
    assert outf.items["head"] is None
    assert str(outf) == "3. body: armor"
    assert outf.unequip("body") == item2
    assert str(outf) == ""
    assert outf.unequip("hands") == print("Nothing to unequip!")

