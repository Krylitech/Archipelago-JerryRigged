from worlds.AutoWorld import WebWorld, World
from worlds.generic.Rules import add_rule, set_rule, forbid_item, add_item_rule
from typing import Union, Tuple, List, Dict, Set
from BaseClasses import Region, ItemClassification, Tutorial, CollectionState
from .Items import JerryItem, item_table
from .Locations import JerryLocation, locations_table, create_regions
from .Rules import set_rules, set_completion_rules
from .Options import JerryOptions

# IDK WHAT I'M DOING!

class JerryWeb(WebWorld):
	tutorials = [
		Tutorial(
			"Multiworld Setup Guide",		# tutorial_name: str
			"A guide to set up the custom game Jerry Rigged's randomizer" \
			" to connect to an Archipelago Multiworld.",	# description: str
			"English",	# Language: str
			"setup_en.mid",	# file_name: str
			"setup/en",	# link: str  # unused
			["Kryliwitch"]	# authors: List[str]
		)
	]

class JerryWorld(World):
	'''
	Jerry Rigged is a game made custom for the Archipelago 2026 Game Jam.
	'''
	game = "Jerry Rigged"
	web = JerryWeb()
	options: JerryOptions

	item_name_to_id = {name: data.code for name, data in item_table.items()}
	location_name_to_id = {name: data.code for name, data in locations_table.items()}

	def _get_jerry_data(self) -> Dict:
		return {
			"world_seed": self.multiworld.seed,
			"seed_name": self.multiworld.seed_name,
			"player_name": self.multiworld.get_player_name(self.player),
			"player_id": self.player,
			"prism_keys": int(self.options.prism_keys.value)
		}


	def create_regions(self) -> None:
		create_regions(self)

	def create_item(self, item: str) -> JerryItem:
		item_data = item_data[item]
		return JerryItem(item, item_data.classification, item_data.code, self.player)

	def create_items(self) -> None:
		itempool = []
		for name, _data in item_table:
			if name == "Prism Key":
				itempool += ["Prism Key"] * self.player.options.prism_keys.value
			else:
				itempool.append(name) 

		if self.options.prism_keys > 1:
			itempool += ["P"]

		for item in map(self.create_item, item_table):
			self.multiworld.itempool.append(item)

		# itempool and number of locations should match up.
		# If this is not the case we want to fill the itempool with junk.
		junk = 0  # calculate this based on player options
		self.multiworld.itempool += [self.create_item("nothing") for _ in range(junk)]

	def create_event(self, event: str) -> JerryItem:
		return JerryItem(event, ItemClassification.progression, None, self.player)

	def set_rules(self) -> None:
		set_rules(self)
		set_completion_rules(self)

	def fill_slot_data(self):
		return self._get_jerry_data