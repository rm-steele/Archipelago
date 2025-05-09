from typing import Any
from BaseClasses import Region, Location, Item, ItemClassification, Tutorial
from worlds.AutoWorld import World, WebWorld
from worlds.generic.Rules import set_rule
from .Locations import location_data_table, SpelClassicLocation
from .Items import SpelClassicItem, item_data_table, item_data_table_useful, item_data_table_filler, SpelClassicItem
from .Regions import region_data_table
from .Options import SpelClassicOptions
from .Rules import set_standard_rules


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
    # i don't think i need this, i misunderstood its purpose
    # topology_present = True
    location_name_to_id = {name: data.address for name, data in location_data_table.items()}
    item_name_to_id = {name: data.code for name, data in item_data_table.items()}
    origin_region_name = "Mines"
    options_dataclass = SpelClassicOptions
    options: SpelClassicOptions
    goal = 0
    cog_goal = False

    def generate_early(self) -> None:
        self.goal = self.options.goal
        self.cog_goal = self.goal == 1 or self.goal == 2
        if self.goal != 2:
            self.options.score.visibility &= 0b0111
        if self.options.rand_ghost != True:
            self.options.rand_ghost_min.visibility &= 0b0111
            self.options.rand_ghost_max.visibility &= 0b0111


    def create_regions(self) -> None:
        # create regions
        for region_name in region_data_table.keys():
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)
#             print(f"added region {region_name} for player {self.player_name}")

        if self.cog_goal:
            self.multiworld.regions.append(Region("City of Gold", self.player, self.multiworld))
#             print(f"added region City of Gold for player {self.player_name}")
            region = self.get_region("Temple")
            region.add_exits(["City of Gold"])

        # add locations to them
        for region_name, region_data in region_data_table.items():
            region = self.get_region(region_name)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in location_data_table.items()
                if location_data.region == region_name}, SpelClassicLocation)
            if region_data_table[region_name].exits != None:
                region.add_exits(region_data_table[region_name].exits)

        # add victory event in the correct region
        # i "arbitrarily" decided that shortcuts are temple and scoreruns are CoG
        if not self.cog_goal:
            goal_location = SpelClassicLocation(self.player, "Victory", None, self.get_region("Temple"))
            self.get_region("Temple").locations.append(goal_location)
        else:
            goal_location = SpelClassicLocation(self.player, "Victory", None, self.get_region("City of Gold"))
            self.get_region("City of Gold").locations.append(goal_location)
        goal_location.place_locked_item(SpelClassicItem("Victory", ItemClassification.progression, None, self.player))
        # use self.multiworld.completion_condition
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)


    def create_items(self) -> None:
        additions = []
        useful_items_fraction = self.options.filler_denom # 1 / X of filler items will be type useful instead of filler
        num_locations = len(location_data_table)
        num_items = len(item_data_table)
        if num_items > num_locations:
            raise FillError("uh nope you shouldn't have more items than locations how did you manage this?")

        # initial fill: put one copy of everything in
        for name, data in item_data_table.items():
            additions.append(self.create_item(name))
        num_locations -= num_items

        # remaining fill: add items until the amount of items added is the same as the number of locations
        for i in range(num_locations):
        # TODO: look into allowing the player to enter a decimal number using FreeText
            if self.random.randint(1, useful_items_fraction) == 1:
                additions.append(self.create_item(self.random.choices(list(item_data_table_useful))[0])) # TODO: add weighting
            else:
                additions.append(self.create_item(self.random.choices(list(item_data_table_filler))[0])) # TODO: add weighting

        self.multiworld.itempool += additions


    def set_rules(self) -> None:
        set_standard_rules(self, self.player)
        if self.cog_goal:
            set_rule(self.get_entrance("Temple -> City of Gold"), lambda state: state.has_all(
                                    ["Golden Key", "Ankh Charm", "Hedjet", "Sceptre"], self.player))


    def fill_slot_data(self) -> dict[str, Any]:
        return self.options.as_dict("goal", "score", "can_rob_checks", "rand_ghost", "rand_ghost_min", "rand_ghost_max")

    def create_item(self, name: str) -> "SpelClassicItem":
        item_class = item_data_table[name].type
        return SpelClassicItem(name, item_class, self.item_name_to_id[name], self.player)


# literally no idea what this does or why i added it. probably a copypaste thing
#     def get_item_classification(self, name: str) -> ItemClassification:
#         return ItemClassification.progression
