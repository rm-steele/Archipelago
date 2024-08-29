from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule

def set_standard_rules(world: "SpelClassicWorld", player: int):

    # regions
    set_rule(world.get_enterance("Menu -> Mines"), lambda state: True)
    set_rule(world.get_enterance("Jungle -> Ice Caves"), lambda state: state.has("Jungle", player))
    set_rule(world.get_enterance("Mines -> Jungle"), lambda state: state.has("Jungle", player))
    set_rule(world.get_enterance("Mines -> Jungle"), lambda state: state.has("Jungle", player))
    set_rule(world.get_enterance("Mines -> Jungle"), lambda state: state.has("Jungle", player))
