from typing import NamedTuple, Optional
from BaseClasses import Location

spel_classic_base_id = 0xC1A551C

class SpelClassicLocation(Location):
    game = "Spelunky Classic"

class SpelClassicLocationData(NamedTuple):
    region: str
    address: Optional[int] = None

# temp locations as a proof of concept
# TODO: implement missing and re-order IDs
location_data_table_worlds = {
    "Mines": SpelClassicLocationData("Mines", spel_classic_base_id + 0),
    "Jungle": SpelClassicLocationData("Jungle", spel_classic_base_id + 1),
    "Ice Caves": SpelClassicLocationData("Ice Caves", spel_classic_base_id + 2),
    "Temple": SpelClassicLocationData("Temple", spel_classic_base_id + 3),
    "City of Gold": SpelClassicLocationData("City of Gold", spel_classic_base_id + 4) # maybe city of gold shouldn't be its own region if this is the only check there
}

location_data_table_kills = {
    "Snake": SpelClassicLocationData("Mines", spel_classic_base_id + 5),
    "Spider": SpelClassicLocationData("Mines", spel_classic_base_id + 6),
    "Giant Spider": SpelClassicLocationData("Mines", spel_classic_base_id + 7),
    "Bat": SpelClassicLocationData("Mines", spel_classic_base_id + 8),
    "Caveman": SpelClassicLocationData("Mines", spel_classic_base_id + 9),
    "Shopkeeper": SpelClassicLocationData("Mines", spel_classic_base_id + 10),
    "Scarab": SpelClassicLocationData("Mines", spel_classic_base_id + 11),
    "Damsel": SpelClassicLocationData("Mines", spel_classic_base_id + 12),

    "Mantrap": SpelClassicLocationData("Jungle", spel_classic_base_id + 13),
    "Frog": SpelClassicLocationData("Jungle", spel_classic_base_id + 14),
    "Fire Frog": SpelClassicLocationData("Jungle", spel_classic_base_id + 15),
    "Monkey": SpelClassicLocationData("Jungle", spel_classic_base_id + 16),
    "Jiang Shi": SpelClassicLocationData("Jungle", spel_classic_base_id + TODO),

    "Yeti": SpelClassicLocationData("Ice Caves", spel_classic_base_id + 17),
    "UFO": SpelClassicLocationData("Ice Caves", spel_classic_base_id + 18),
    "Alien Lord": SpelClassicLocationData("Ice Caves", spel_classic_base_id + 19),

    "Hawk Man": SpelClassicLocationData("Temple", spel_classic_base_id + 20),
    "Mummy": SpelClassicLocationData("Temple", spel_classic_base_id + 21),
    # having olmec be a check is questionable
    "Olmec": SpelClassicLocationData("Temple", spel_classic_base_id + 23)
}

location_data_table_shop = {
    "Bomb Bag": SpelClassicLocationData("Mines", spel_classic_base_id + 24),
    "Bomb Box": SpelClassicLocationData("Mines", spel_classic_base_id + 25),
    "Rope Pile": SpelClassicLocationData("Mines", spel_classic_base_id + 26),
    "Paste": SpelClassicLocationData("Mines", spel_classic_base_id + 27),
    "Pistol": SpelClassicLocationData("Mines", spel_classic_base_id + 28),
    "Bow": SpelClassicLocationData("Mines", spel_classic_base_id + 29),
    "Shotgun": SpelClassicLocationData("Mines", spel_classic_base_id + 30),
    "Climbing Gloves": SpelClassicLocationData("Mines", spel_classic_base_id + 31),
    "Pitcher's MItt": SpelClassicLocationData("Mines", spel_classic_base_id + 32),
    "Teleporter": SpelClassicLocationData("Mines", spel_classic_base_id + 33),
    "Cape": SpelClassicLocationData("Mines", spel_classic_base_id + 34),
    "Jetpack": SpelClassicLocationData("Mines", spel_classic_base_id + 35),
    "Compass": SpelClassicLocationData("Mines", spel_classic_base_id + 35),
    "Spring Shoes": SpelClassicLocationData("Mines", spel_classic_base_id + 35),
    "Spike Shoes": SpelClassicLocationData("Mines", spel_classic_base_id + 35),
    "Parachute": SpelClassicLocationData("Mines", spel_classic_base_id + 35),
    "Spectacles": SpelClassicLocationData("Mines", spel_classic_base_id + 35),
    "Machete": SpelClassicLocationData("Mines", spel_classic_base_id + 35),
    "Mattock": SpelClassicLocationData("Mines", spel_classic_base_id + 35),
    "Web Gun": SpelClassicLocationData("Mines", spel_classic_base_id + 35),
}

location_data_table_misc = {
    # chain items
    "Udjat Eye": SpelClassicLocationData("Mines", spel_classic_base_id + TODO),
    "Ankh Charm": SpelClassicLocationData("Jungle", spel_classic_base_id + TODO),
    "Hedjet": SpelClassicLocationData("Ice Caves", spel_classic_base_id + TODO),
    "Sceptre": SpelClassicLocationData("Temple", spel_classic_base_id + TODO),
    # idols
    "Gold Idol": SpelClassicLocationData("Mines", spel_classic_base_id + TODO),
    "Bone Idol": SpelClassicLocationData("Jungle", spel_classic_base_id + TODO)
}
location_data_table = {
    **location_data_table_worlds,
    **location_data_table_kills,
    **location_data_table_shop,
    **location_data_table_misc
}
