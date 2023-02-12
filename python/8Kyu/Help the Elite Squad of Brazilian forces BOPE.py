from typing import Tuple
def mag_number(info: Tuple[str, int]) -> int:
    weapons = {
        "PT92": 17,
        "M4A1": 30,
        "M16A2": 30,
        "PSG1": 5}
    weapon, streets = info
    return __import__("math").ceil((streets * 3) / weapons[weapon])
    