from dataclasses import dataclass

from Options import Toggle, Range, Choice, PerGameCommonOptions


class Goal(Choice):
    # TODO: CoG: decide if win the same run or just a run
    # and if scorerun should require you to win with the money
    """Sets the victory condition.
     - olmec: Defeat Olmec and win the game.
     - city_of_gold: Reach the City of Gold and then win the run.
     - scorerun: Reach the amount of money defined in "score".
     - shortcuts: Unlock all three shortcuts."""
     display_name = "Goal"
     option_olmec = 0
     option_city_of_gold = 1
     option_scorerun = 2
     option_shortcuts = 3
     alias_cog = 1
     alias_all_shortcuts = 3
     default = 1

class Score(Range):
    """Sets the required amount of gold to achieve victory."""
    display_name = "Score to Win"
    range_start  =  150000
    range_end    = 1000000
    default      =  500000

class FillerDenominator(Range):
    """Sets the ratio of Useful to Filler items.
    1 / X items will be a random useful item, the others will be filler.
    Keep in mind that one of each item is placed before filling locations."""
    display_name = "Useful to Filler Item Ratio"
    range_start = 1
    range_end = 50
    default = 5

class CanRobChecks(Toggle):
    """Determines if you're allowed to anger a shopkeeper to get items for free, or if you must pay for the items."""
    display_name = "Steal Checks from Shops"

class RandomGhost(Toggle):
    """Whether or not to rnadomize the ghost timer in each level."""
    display_name = "Randomized Ghost Timer"

class GhostTimerMin(Range):
    """Minimum timer for the ghost timer to be randomized to."""
    display_name = "Minimum Ghost Timer"
    range_start = 1
    range_end = 3600
    default = 60

class GhostTimerMax(Range):
    """Maximum timer for the ghost timer to be randomized to."""
    display_name = "Maximum Ghost Timer"
    range_start = 1
    range_end = 3600
    default = 300

# TODO: damselsanity: each level has a check for rescuing the damsel, you must rescue one on every level
# it's a memey option but it could be fun. leaving it out for the time being.
# class Damselsanity(Toggle):
#     """Each level has a check for rescuing the damsel, you must rescue on on every level."""
#     display_name = "Damselsanity"


@dataclass
class SpelClassicOptions(PerGameCommonOptions):
    goal: Goal
    score: Score
    filler_denom: FillerDenominator
    can_rob_checks: CanRobChecks
    rand_ghost: RandomGhost
    rand_ghost_min: GhostTimerMin
    rand_ghost_max: GhostTimerMax
    # damselsanity: Damselsanity
