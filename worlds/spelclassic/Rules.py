from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule

def set_standard_rules(world: "SpelClassicWorld", player: int):

    # regions
    set_rule(world.get_enterance("Menu -> Mines"), lambda state: True)
    set_rule(world.get_enterance("Mines -> Jungle"), lambda state: state.has("Jungle", player))
    set_rule(world.get_enterance("Jungle -> Ice Caves"), lambda state: state.has("Ice Caves", player))
    set_rule(world.get_enterance("Ice Caves -> Temple"), lambda state: state.has("Temple", player))
    set_rule(world.get_enterance("Temple -> City of Gold"), lambda state: state.has_all(
                                         ["City of Gold", "Hedjet", "Sceptre"], player))

    # locations > chain
    set_rule(world.get_location("Udjat Eye"), lambda state: state.has("Golden Key", player))
    set_rule(world.get_location("Ankh Charm"), lambda state: state.has_all(["Ankh Charm", "Udjat Eye"])
    set_rule(world.get_location("Hedjet"), lambda state: state.has_all(["Ankh Charm", "Hedjet"], player))
    set_rule(world.get_location("Sceptre"), lambda state: state.has("Sceptre"))
