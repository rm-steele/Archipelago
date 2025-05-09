from typing import NamedTuple, Optional
from BaseClasses import Location

class SpelClassicLocation(Location):
    game = "Spelunky Classic"

class SpelClassicLocationData(NamedTuple):
    region: str
    address: Optional[int] = None


location_data_table_worlds = {
    "Jungle": SpelClassicLocationData("Jungle", 1),
    "Ice Caves": SpelClassicLocationData("Ice Caves", 2),
    "Temple": SpelClassicLocationData("Temple", 3)
}

location_data_table_kills = {
    "Snake": SpelClassicLocationData("Mines", 4),
    "Spider": SpelClassicLocationData("Mines", 5),
    "Giant Spider": SpelClassicLocationData("Mines", 6),
    "Bat": SpelClassicLocationData("Mines", 7),
    "Skeleton": SpelClassicLocationData("Mines", 8),
    "Caveman": SpelClassicLocationData("Mines", 9),
    "Shopkeeper": SpelClassicLocationData("Mines", 10),
    "Scarab": SpelClassicLocationData("Mines", 11),
    "Damsel": SpelClassicLocationData("Mines", 12),

    "Mantrap": SpelClassicLocationData("Jungle", 13),
    "Frog": SpelClassicLocationData("Jungle", 14),
    "Fire Frog": SpelClassicLocationData("Jungle", 15),
    "Monkey": SpelClassicLocationData("Jungle", 16),
    "Jiang Shi": SpelClassicLocationData("Jungle", 17),
    "Piranha": SpelClassicLocationData("Jungle", 18),
    "Vampire": SpelClassicLocationData("Jungle", 19),

    "Yeti": SpelClassicLocationData("Ice Caves", 20),
    "UFO": SpelClassicLocationData("Ice Caves", 21),
    "Alien Lord": SpelClassicLocationData("Ice Caves", 22),

    "Hawk Man": SpelClassicLocationData("Temple", 23),
    "Mummy": SpelClassicLocationData("Temple", 24),
    # having olmec be a check is questionable
    "Olmec": SpelClassicLocationData("Temple", 25)
}

location_data_table_shop = {
    "Bomb Bag": SpelClassicLocationData("Mines", 26),
    "Bomb Box": SpelClassicLocationData("Mines", 27),
    "Rope Pile": SpelClassicLocationData("Mines", 28),
    "Paste": SpelClassicLocationData("Mines", 29),
    "Pistol": SpelClassicLocationData("Mines", 30),
    "Bow": SpelClassicLocationData("Mines", 31),
    "Shotgun": SpelClassicLocationData("Mines", 32),
    "Climbing Gloves": SpelClassicLocationData("Mines", 33),
    "Pitcher's MItt": SpelClassicLocationData("Mines", 34),
    "Teleporter": SpelClassicLocationData("Mines", 35),
    "Cape": SpelClassicLocationData("Mines", 36),
    "Jetpack": SpelClassicLocationData("Mines", 37),
    "Compass": SpelClassicLocationData("Mines", 38),
    "Spring Shoes": SpelClassicLocationData("Mines", 39),
    "Spike Shoes": SpelClassicLocationData("Mines", 40),
    "Parachute": SpelClassicLocationData("Mines", 41),
    "Spectacles": SpelClassicLocationData("Mines", 42),
    "Machete": SpelClassicLocationData("Mines", 43),
    "Mattock": SpelClassicLocationData("Mines", 44),
    "Web Cannon": SpelClassicLocationData("Mines", 45),
}

location_data_table_misc = {
    # chain items
    "Udjat Eye": SpelClassicLocationData("Mines", 46),
    "Ankh Charm": SpelClassicLocationData("Jungle", 47),
    "Hedjet": SpelClassicLocationData("Ice Caves", 48),
    "Sceptre": SpelClassicLocationData("Temple", 49),
    # idols
    "Gold Idol": SpelClassicLocationData("Mines", 50),
    "Bone Idol": SpelClassicLocationData("Jungle", 51)
}
location_data_table = {
    **location_data_table_worlds,
    **location_data_table_kills,
    **location_data_table_shop,
    **location_data_table_misc
}
