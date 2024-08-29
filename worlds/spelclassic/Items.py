from typing import Optional, NamedTuple
from BaseClasses import Item, ItemClassification

spel_classic_base_id: int = 0xC1A551C

class SpelClassicItem(Item):
    game = "Spelunky Classic"

class SpelClassicItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler

# temp items just as a proof of concept
# TODO: put in actual items
item_data_table_worlds = {
    "Jungle": SpelClassicItemData(spel_classic_base_id + 0, ItemClassification.progression),
    "Ice Caves": SpelClassicItemData(spel_classic_base_id + 1, ItemClassification.progression),
    "Temple": SpelClassicItemData(spel_classic_base_id + 2, ItemClassification.progression)
}

item_data_table_chain = {
    "Golden Key": SpelClassicItemData(spel_classic_base_id + 3, ItemClassification.progression),
    "Ankh": SpelClassicItemData(spel_classic_base_id + 4, ItemClassification.progression),
    "Hedjet": SpelClassicItemData(spel_classic_base_id + 5, ItemClassification.progression),
    "Scepter": SpelClassicItemData(spel_classic_base_id + 6, ItemClassification.progression)
}

item_data_table_filler = {
    "Bomb Bag": SpelClassicItemData(spel_classic_base_id + 7),
    "Bomb Box": SpelClassicItemData(spel_classic_base_id + 8),
    "Rope Pile": SpelClassicItemData(spel_classic_base_id + 9),
    "Compass": SpelClassicItemData(spel_classic_base_id + 10),
    "Mattock": SpelClassicItemData(spel_classic_base_id + 11)
}

item_data_table = {**item_data_table_worlds, **item_data_table_chain, **item_data_table_filler}
