from typing import Optional, NamedTuple
from BaseClasses import Item, ItemClassification

spel_classic_base_id: int = 0xC1A551C

class SpelClassicItem(Item):
    game = "Spelunky Classic"

class SpelClassicItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler

item_data_table_worlds = {
    "Jungle": SpelClassicItemData(spel_classic_base_id + 0, ItemClassification.progression),
    "Ice Caves": SpelClassicItemData(spel_classic_base_id + 1, ItemClassification.progression),
    "Temple": SpelClassicItemData(spel_classic_base_id + 2, ItemClassification.progression)
}

item_data_table_chain = {
    "Golden Key": SpelClassicItemData(spel_classic_base_id + 3, ItemClassification.progression),
    "Ankh Charm": SpelClassicItemData(spel_classic_base_id + 4, ItemClassification.progression),
    "Hedjet": SpelClassicItemData(spel_classic_base_id + 5, ItemClassification.progression),
    "Sceptre": SpelClassicItemData(spel_classic_base_id + 6, ItemClassification.progression)
}

item_data_table_useful = {
    "Mattock": SpelClassicItemData(spel_classic_base_id + 7, ItemClassification.useful),
    "Jetpack": SpelClassicItemData(spel_classic_base_id + 8, ItemClassification.useful),
    "Bomb Box": SpelClassicItemData(spel_classic_base_id + 9, ItemClassification.useful),
    "Kapala": SpelClassicItemData(spel_classic_base_id + 10, ItemClassification.useful),
    "Paste": SpelClassicItemData(spel_classic_base_id + 11, ItemClassification.useful),
    "Cape": SpelClassicItemData(spel_classic_base_id + 12, ItemClassification.useful),
    "Shotgun": SpelClassicItemData(spel_classic_base_id + 13, ItemClassification.useful)
}

item_data_table_filler = {
    "Bomb Bag": SpelClassicItemData(spel_classic_base_id + 14),
    "Rope Pile": SpelClassicItemData(spel_classic_base_id + 15),
    "Compass": SpelClassicItemData(spel_classic_base_id + 16),
    "Spectacles": SpelClassicItemData(spel_classic_base_id + 17),
    "Jordans": SpelClassicItemData(spel_classic_base_id + 18),
    "Web Gun": SpelClassicItemData(spel_classic_base_id + 19),
    "Box of Flares": SpelClassicItemData(spel_classic_base_id + 20)
}

item_data_table = {
    **item_data_table_worlds,
    **item_data_table_chain,
    **item_data_table_useful,
    **item_data_table_filler
}
