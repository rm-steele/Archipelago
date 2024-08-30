from typing import Optional, NamedTuple
from BaseClasses import Item, ItemClassification

spel_classic_base_id: int = 0xC1A551C

class SpelClassicItem(Item):
    game = "Spelunky Classic"

class SpelClassicItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler

# TODO: re-order IDs so they're, you know, in order
item_data_table_worlds = {
    "Jungle": SpelClassicItemData(spel_classic_base_id + 0, ItemClassification.progression),
    "Ice Caves": SpelClassicItemData(spel_classic_base_id + 1, ItemClassification.progression),
    "Temple": SpelClassicItemData(spel_classic_base_id + 2, ItemClassification.progression),
    "City of Gold": SpelClassicItemData(spel_classic_base_id + 12, ItemClassification.progression)
}

item_data_table_chain = {
    "Golden Key": SpelClassicItemData(spel_classic_base_id + 3, ItemClassification.progression),
    "Ankh Charm": SpelClassicItemData(spel_classic_base_id + 4, ItemClassification.progression),
    "Hedjet": SpelClassicItemData(spel_classic_base_id + 5, ItemClassification.progression),
    "Sceptre": SpelClassicItemData(spel_classic_base_id + 6, ItemClassification.progression)
}

item_data_table_useful = {
    "Mattock": SpelClassicItemData(spel_classic_base_id + 13, ItemClassification.useful),
    "Jetpack": SpelClassicItemData(spel_classic_base_id + 13, ItemClassification.useful),
    "Bomb Box": SpelClassicItemData(spel_classic_base_id + 13, ItemClassification.useful),
    "Kapala": SpelClassicItemData(spel_classic_base_id + 13, ItemClassification.useful),
    "Paste": SpelClassicItemData(spel_classic_base_id + 13, ItemClassification.useful),
    "Cape": SpelClassicItemData(spel_classic_base_id + 13, ItemClassification.useful),
    "Shotgun": SpelClassicItemData(spel_classic_base_id + TODO, ItemClassification.useful)
}

item_data_table_filler = {
    "Bomb Bag": SpelClassicItemData(spel_classic_base_id + 7),
    "Rope Pile": SpelClassicItemData(spel_classic_base_id + 9),
    "Compass": SpelClassicItemData(spel_classic_base_id + 10),
    "Spectacles": SpelClassicItemData(spel_classic_base_id + TODO),
    "Jordans": SpelClassicItemData(spel_classic_base_id + TODO),
    "Web Gun": SpelClassicItemData(spel_classic_base_id + TODO),
    "Box of Flares": SpelClassicItemData(spel_classic_base_id + TODO)
}

item_data_table = {
    **item_data_table_worlds,
    **item_data_table_chain,
    **item_data_table_useful,
    **item_data_table_filler
}
