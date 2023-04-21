EVENTS = {
    100:{
        "name": "script"
    },
    101:{
        "name": "next_chap",
        "chap": 1
    },
    200:{
        "name": "guide",
        "check": "getattr(self.char.outfit.items['main_hand'], 'id', None) != 'Weapon:300'",
        "file": "script/guide1.txt",
        "next": None
    },
    201:{
        "name": "explore",
        "options": ("Attack", "Sneak Past"),
        "desc": (
            "Briefly think you rush to the attack",
            "You attempt to carefully sneak past the skeleton. When suddenly you step on something. Treacherous crunch betrays you. The skeleton immediately turns around and charges."
            ),
        "next":[202, 202]
    },
    202:{
        "name": "battle",
        "enemy": "Unit:002",
        "next": 100
    },
    203:{
        "name": "guide",
        "check": "self.char.bag.items.get('Heal_pot:400')",
        "file": "script/guide2.txt",
        "next": None
    },
    300:{
        "name": "explore",
        "options": ("Book", "Chest", "Orb"),
        "desc": (
            "a heavy book in a greasy leather binding, inside there are clearly descriptions of some kind of dark magical rituals.",
            "a very old but still strong chest, it seems to be locked with a key",
            "the dark orb looks serenely calm."
            ),
        "next":[None, 301, 100]
    },
    301:{
        "name": "lockpick",
        "level": 30,
        "next": 302
    },
    302:{
        "name": "loot",
        "items": [("Item:100", 10), ("Heal_pot:400", 1)],
        "next": None
    },
    400:{
        "name": "battle",
        "enemy": "Unit:001",
        "next": None
    }
}