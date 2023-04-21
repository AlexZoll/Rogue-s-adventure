DEFAULT_BACKPACK = [
    ("Item:100", 10),
    ("Item:101", 3),
    ("Weapon:300", 1),
    ("Heal_pot:400", 1)
]

DEFAULT_OUTFIT = [
    ("Armor:200", 1),
    ("Armor:201", 1),
    ("Armor:202", 1),
]

ITEMS = {
    "Item:100": {
        "name":"Gold",
        "desc":"A valuable gold circle"
    },
    "Item:101": {
        "name":"Lockpick",
        "desc":"Use to open lock"
    },
    "Armor:200": {
        "name": "Leather jacket",
        "defense": 2,
        "slot": "body",
        "desc": "Rough leather jacket"
    },
    "Armor:201": {
        "name": "Leather boots",
        "defense": 1,
        "slot": "feet",
        "desc": "Rough leather boots"
    },
    "Armor:202": {
        "name": "Leather gloves",
        "defense": 1,
        "slot": "hands",
        "desc": "Rough leather gloves"
    },
    "Weapon:300": {
        "name":"Short sword",
        "attack": 5,
        "slot": "main_hand",
        "desc": "Simple iron sword"
    },
    "Heal_pot:400": {
        "name": "Lesser healing potion",
        "hp": 15,
        "desc": "Use it to recover some health"
    }
}