from BaseClasses import Region, Location, Item, ItemClassification, Tutorial
from worlds.AutoWorld import World, WebWorld
from .Locations import location_data_table
from .Items import SpelClassicItem, item_data_table, item_data_table_useful, item_data_table_filler
from .Regions import region_data_table


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
    topology_present = True
    location_name_to_id = {name: data.address for name, data in location_data_table.items()}
    item_name_to_id = {name: data.code for name, data in item_data_table.items()}


    def create_regions(self) -> None:
        # create regions
        for region_name in region_data_table.keys():
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        # add locations to them
        for region_name, region_data in region_data_table.items():
            region = self.get_region(region_name)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in location_data_table.items()
                if location_data.region == region_name}, SpelClassicLocation)
            region.add_exits(region_data_table[region_name].exits)

        # add victory event in the city of gold
        goal_location = SpelClassicLocation(self.player, "Victory", None, self.get_region("City of Gold"))
        goal_location.place_locked_item(SpelClassicItem("Victory", ItemClassification.progression, None, self.player))


    def create_item(self, name: str) -> "SpelClassicItem":
        item_class = item_data_table[name].type
        return SpelClassicItem(name, item_class, self.item_name_to_id.get[name], self.player)


    def create_items(self) -> None:
        additions = []
        useful_items_fraction = 5 # 1 / X of filler items will be type useful instead of filler
        num_locations = len(location_data_table)
        num_items = len(item_data_table)
        if num_items > num_locations:
            raise FillError("uh nope you shouldn't have more items than locations how did you manage this?")

        # initial fill: put one copy of everything in
        for name, data in item_data_table.items():
            additions += self.create_item(name)
        num_locations -= num_items

        # remaining fill: add items until the amount of items added is the same as the number of locations
        for i in range(num_locations):
            if self.random.randint(1, useful_items_fraction) == 1:
                self.create_item(self.random.choices(list(item_data_table_useful))[0]) # TODO: add weighting
            else:
                self.create_item(self.random.choices(list(item_data_table_filler))[0]) # TODO: add weighting

        self.multiworld.itempool += additions


    def get_item_classification(self, name: str) -> ItemClassification:
        return ItemClassification.progression
