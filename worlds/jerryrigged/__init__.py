from worlds.AutoWorld import WebWorld, World
from BaseClasses import Region, ItemClassification, Tutorial, CollectionState

# IDK WHAT I'M DOING!

class JerryRiggedWeb(WebWorld):
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

class JerryRiggedWorld(World):
	'''
	DESCRIPTION
	Jerry Rigged is a game made custom for the Archipelago 2026 Game Jam.
	'''
	game = "Jerry Rigged"