from typing import Optional, NamedTuple, List

class SpelClassicRegionData(NamedTuple):
    exits: Optional[List[str]] = None

# City of Gold region serves as an easy way to manage the rules for the Victory location
# so even though that's the only check there, i think it's useful to keep
region_data_table = {
    "Mines": SpelClassicRegionData(["Jungle"]),
    "Jungle": SpelClassicRegionData(["Ice Caves"]),
    "Ice Caves": SpelClassicRegionData(["Temple"]),
    "Temple": SpelClassicRegionData(None),
#    "City of Gold": SpelClassicRegionData()
}
