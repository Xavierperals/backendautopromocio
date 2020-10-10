from enum import Enum
from typing import Tuple, List


class HomeSize(Enum):
    LESS_THAN_60 = 'LESS_THAN_60', 'Menos de 60'
    BETWEEN_60_AND_80 = 'BETWEEN_60_AND_80', 'Entre 60 y 80'
    BETWEEN_80_AND_100 = 'BETWEEN_80_AND_100', 'Entre 80 y 100'
    BETWEEN_100_AND_120 = 'BETWEEN_100_AND_120', 'Entre 100 y 120'
    MORE_THAN_120 = 'MORE_THAN_120', 'Más de 120'

    @classmethod
    def choices(cls) -> List[Tuple[str, Tuple[str, str]]]:
        return [(field.name, field.value) for field in cls]
