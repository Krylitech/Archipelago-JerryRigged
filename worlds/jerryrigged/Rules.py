from worlds.generic.Rules import set_rule, add_rule
from . import JerryWorld


def set_rules(world: "JerryWorld"):
	player = world.player
	multiworld = world.multiworld

	set_rule(multiworld.get_entrance("Cyan Gate", player), 
		  lambda state: state.has("Cyan Keycard"))
	set_rule(multiworld.get_entrance("Crimson Gate", player), 
		  lambda state: state.has("Crimson Keycard"))
	set_rule(multiworld.get_entrance("Final Gate", player), 
		  lambda state: state.has("Prism Key", player, world.options.prism_keys.value))


def set_completion_rules(world: "JerryWorld"):
	player = world.player
	multiworld = world.multiworld
	multiworld.get_location("Escape Exit", player).place_locked_item(world.create_event("Victory"))
	multiworld.completion_condition[player] = lambda state: state.has("Victory", player)