from BaseClasses import Location, Region
from . import JerryWorld
import typing

class LocationData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str

class JerryLocation(Location):
	game: str = "Jerry Rigged"

gray_sector = {	# Starting Region
      "Loot Stash 1": 374001
}
cyan_sector = {
	"Loot Stash 2": 375001
}
crimson_sector = {
	"Loot Stash 3": 376001
}
final_sector = {
    "Escape Exit": 377099 # Change to last code when done with all locations
}

# 374000 is location code
locations_table = {}
locations_table.extend({name: LocationData(id, "Gray Sector") for name, id in gray_sector})
locations_table.extend({name: LocationData(id, "Cyan Sector") for name, id in cyan_sector})
locations_table.extend({name: LocationData(id, "Crimson Sector") for name, id in crimson_sector})
locations_table.extend({name: LocationData(id, "Final Sector") for name, id in final_sector})


def create_region(world: "JerryWorld", name: str, locations) -> Region:
	player = world.player
	multiworld = world.multiworld
	new_region = Region(name, player, multiworld)
	new_region.add_locations(locations, JerryLocation)
	multiworld.regions.append(new_region)


def create_regions(world: "JerryWorld"):
	player = world.player
	multiworld = world.multiworld

	menu_region = Region("Menu", player, multiworld)
	multiworld.regions.append(menu_region)

	gray_region = create_region(world, "Gray Sector", gray_sector)
	cyan_region = create_region(world, "Cyan Sector", cyan_sector)
	crimson_region = create_region(world, "Crimson Sector", crimson_sector)
	final_region = create_region(world, "Final Sector", final_sector)

	menu_region.connect(gray_region)

	# Create exits and entances in code because they are randomized!
		# Cyan Sector: Cyan Gate, "Cyan Sector": lambda staet: state.has("Cyan Keycard")
		# Crimson Sector: Crimson Gate, "Crimson Sector": lambda state: state.has("Crimson Keycard")
		# Final Sector: Final Gate, "Final Sector": lambda state: state.has("Final Keycard")