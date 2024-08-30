from typing import NamedTuple, Optional
from BaseClasses import Location

spel_classic_base_id = 0xC1A551C

class SpelClassicLocation(Location):
    game = "Spelunky Classic"

class SpelClassicLocationData(NamedTuple):
    region: str
    address: Optional[int] = None

location_data_table_worlds = {
    "Mines": SpelClassicLocationData("Mines", spel_classic_base_id + 0),
    "Jungle": SpelClassicLocationData("Jungle", spel_classic_base_id + 1),
    "Ice Caves": SpelClassicLocationData("Ice Caves", spel_classic_base_id + 2),
    "Temple": SpelClassicLocationData("Temple", spel_classic_base_id + 3)
}

location_data_table_kills = {
    "Snake": SpelClassicLocationData("Mines", spel_classic_base_id + 4),
    "Spider": SpelClassicLocationData("Mines", spel_classic_base_id + 5),
    "Giant Spider": SpelClassicLocationData("Mines", spel_classic_base_id + 6),
    "Bat": SpelClassicLocationData("Mines", spel_classic_base_id + 7),
    "Caveman": SpelClassicLocationData("Mines", spel_classic_base_id + 8),
    "Shopkeeper": SpelClassicLocationData("Mines", spel_classic_base_id + 9),
    "Scarab": SpelClassicLocationData("Mines", spel_classic_base_id + 10),
    "Damsel": SpelClassicLocationData("Mines", spel_classic_base_id + 11),

    "Mantrap": SpelClassicLocationData("Jungle", spel_classic_base_id + 12),
    "Frog": SpelClassicLocationData("Jungle", spel_classic_base_id + 13),
    "Fire Frog": SpelClassicLocationData("Jungle", spel_classic_base_id + 14),
    "Monkey": SpelClassicLocationData("Jungle", spel_classic_base_id + 15),
    "Jiang Shi": SpelClassicLocationData("Jungle", spel_classic_base_id + 16),

    "Yeti": SpelClassicLocationData("Ice Caves", spel_classic_base_id + 17),
    "UFO": SpelClassicLocationData("Ice Caves", spel_classic_base_id + 18),
    "Alien Lord": SpelClassicLocationData("Ice Caves", spel_classic_base_id + 19),

    "Hawk Man": SpelClassicLocationData("Temple", spel_classic_base_id + 20),
    "Mummy": SpelClassicLocationData("Temple", spel_classic_base_id + 21),
    # having olmec be a check is questionable
    "Olmec": SpelClassicLocationData("Temple", spel_classic_base_id + 22)
}

location_data_table_shop = {
    "Bomb Bag": SpelClassicLocationData("Mines", spel_classic_base_id + 23),
    "Bomb Box": SpelClassicLocationData("Mines", spel_classic_base_id + 24),
    "Rope Pile": SpelClassicLocationData("Mines", spel_classic_base_id + 25),
    "Paste": SpelClassicLocationData("Mines", spel_classic_base_id + 26),
    "Pistol": SpelClassicLocationData("Mines", spel_classic_base_id + 27),
    "Bow": SpelClassicLocationData("Mines", spel_classic_base_id + 28),
    "Shotgun": SpelClassicLocationData("Mines", spel_classic_base_id + 29),
    "Climbing Gloves": SpelClassicLocationData("Mines", spel_classic_base_id + 30),
    "Pitcher's MItt": SpelClassicLocationData("Mines", spel_classic_base_id + 31),
    "Teleporter": SpelClassicLocationData("Mines", spel_classic_base_id + 32),
    "Cape": SpelClassicLocationData("Mines", spel_classic_base_id + 33),
    "Jetpack": SpelClassicLocationData("Mines", spel_classic_base_id + 34),
    "Compass": SpelClassicLocationData("Mines", spel_classic_base_id + 35),
    "Spring Shoes": SpelClassicLocationData("Mines", spel_classic_base_id + 36),
    "Spike Shoes": SpelClassicLocationData("Mines", spel_classic_base_id + 37),
    "Parachute": SpelClassicLocationData("Mines", spel_classic_base_id + 38),
    "Spectacles": SpelClassicLocationData("Mines", spel_classic_base_id + 39),
    "Machete": SpelClassicLocationData("Mines", spel_classic_base_id + 40),
    "Mattock": SpelClassicLocationData("Mines", spel_classic_base_id + 41),
    "Web Gun": SpelClassicLocationData("Mines", spel_classic_base_id + 42),
}

location_data_table_misc = {
    # chain items
    "Udjat Eye": SpelClassicLocationData("Mines", spel_classic_base_id + 43),
    "Ankh Charm": SpelClassicLocationData("Jungle", spel_classic_base_id + 44),
    "Hedjet": SpelClassicLocationData("Ice Caves", spel_classic_base_id + 45),
    "Sceptre": SpelClassicLocationData("Temple", spel_classic_base_id + 46),
    # idols
    "Gold Idol": SpelClassicLocationData("Mines", spel_classic_base_id + 47),
    "Bone Idol": SpelClassicLocationData("Jungle", spel_classic_base_id + 48)
}
location_data_table = {
    **location_data_table_worlds,
    **location_data_table_kills,
    **location_data_table_shop,
    **location_data_table_misc
}
