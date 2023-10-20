from .shaker import Shaker

NUM_DICE = 5

# ============
# PLAYER CLASS
# ============


class Player:
    def __init__(self, name: str = "Player 1", is_computer: bool = False) -> None:
        self._name = name
        self._is_computer = is_computer
        self._shaker = Shaker(name=self._name, dice=NUM_DICE)

    def __repr__(self):
        return f"Player: {self._name}"

    @property
    def name(self):
        return self._name

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def shaker(self):
        return self._shaker

    @shaker.setter
    def shaker(self, shaker: object) -> None:
        self._shaker = shaker
