from Options import Choice, Toggle, Range, PerGameCommonOptions
from dataclasses import dataclass

class PrismKeys(Range):
	"""How many Prism Keys are needed to access the final sector"""
	display_name = "Prism Key Amount"
	default = 3
	range_start = 1
	range_end = 10


@dataclass
class JerryOptions(PerGameCommonOptions):
	prism_keys:		PrismKeys