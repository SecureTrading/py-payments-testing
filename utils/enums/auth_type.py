from enum import Enum, auto


class AuthType(Enum):
    V1 = auto()
    V2 = auto()

    @property
    def value(self) -> str:
        return self.name