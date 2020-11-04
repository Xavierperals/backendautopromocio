from enum import Enum
from typing import Tuple, List


class Rooms(Enum):
    ZERO = '0', '0'
    ONE = '1', '1'
    TWO = '2', '2'
    THREE = '3', '3'
    FOUR = '4', '4'
    FIVE = '5', '5'
    MORE_THAN_FIVE = '>5', '>5'

    @classmethod
    def choices(cls) -> List[Tuple[str, Tuple[str, str]]]:
        return [(field.name, field.value) for field in cls]
