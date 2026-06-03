from BaseClasses import Item, ItemClassification
import typing

class ItemData(typing.NamedTuple):
	code: typing.Optional[int]
	classification: any

class JerryItem(Item):
	game: str = "Jerry Rigged"

# 373000 is item code
progression = {	# Progression Items codes: 373000
	"Prism Key": 373000,
	"Cyan Keycard": 373001,
	"Crimson Keycard": 373002,
}
useful = {		# Useful items: 373200

}
filler = {		# Filler items: 373300

}

item_table = {}
item_table.extend(
	{name: ItemData(code, ItemClassification.progression) for name, code in progression.items()}
)
item_table.extend(
	{name: ItemData(code, ItemClassification.useful) for name, code in useful.items()}
)
item_table.extend(
	{name: ItemData(code, ItemClassification.filler) for name, code in filler.items()}
)
