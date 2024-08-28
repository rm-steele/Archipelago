from BaseClasses import Region, Location, Item, ItemClassification, Tutorial
from worlds.AutoWorld import World, WebWorld


class SpelClassicWeb(WebWorld):
    theme = "jungle"
    setup_en = Tutorial(
        "Setup Guide",
        "Setting up Spelunky Classic for Archipelago, unless I haven't written it yet, then maybe not",
        "en",
        "setup_en.md",
        "setup/en",
        ["rm_steele"]
    )
    tutorials = [setup_en]


class SpelClassicWorld(World):
    """TODO: Better docstring"""
    game = "Spelunky Classic"
    web = SpelClassicWeb()
    location_name_to_id = {}
    item_name_to_id = {}

    def create_regions(self) -> None:
        self.multiworld.regions.append(Region("Menu", self.player, self.multiworld))

    def create_items(self) -> None:
        pass

    def create_item(self, name: str) -> "Item":
        item_class = self.get_item_classification(name)
        return TemplateItem(name, item_class, self.item_name_to_id.get(name, None), self.player)

    def get_item_classification(self, name: str) -> ItemClassification:
        return ItemClassification.progression


class TemplateItem(Item):
    game = "Spelunky Classic"


class TemplateLocation(Location):
    game = "Spelunky Classic"
