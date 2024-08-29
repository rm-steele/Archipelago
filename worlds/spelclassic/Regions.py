from typing import Optional, NamedTuple

class SpelClassicRegionData(NamedTuple):
    exits: Optional[List[str]] = None

# might change but idk what else might be needed
# TODO: change this, or don't, not current me's problem
region_data_table = {
    "Menu": SpelClassicRegionData(["Mines"]),
    "Mines": SpelClassicRegionData(["Jungle"]),
    "Jungle": SpelClassicRegionData(["Ice Caves"]),
    "Ice Caves": SpelClassicRegionData(["Temple"]),
    "Temple": SpelClassicRegionData(["City of Gold"]),
    "City of Gold": SpelClassicRegionData()
}
