import pytest


from engine import Engine


from project import check_event_res, create_teller, find_event


def test_check_event_res():
    assert check_event_res(100) is None
    with pytest.raises(SystemExit):
        assert check_event_res(404)


def test_create_teller():
    eng = Engine()
    gen = create_teller()
    assert next(gen) == "__________PROLOGUE__________\n"


def test_find_event():
    assert find_event("noevent") is None
    assert find_event("100") == 100
