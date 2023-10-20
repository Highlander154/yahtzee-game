from .dice import Die

# ============
# SHAKER CLASS
# ============


class Shaker:
    def __init__(self, name: str = "Player 1", dice: int = 5) -> None:
        self._player_name = name
        self._dice_list = []
        self._dice_values = []
        self._dice_icons = []
        self._dice = dice

    def __repr__(self) -> str:
        return f"Shaker (Player: {self._player_name})"

    @property
    def dice(self) -> list:
        return self._dice_list

    @property
    def values(self) -> list:
        return self._dice_values

    @property
    def num_dice(self) -> int:
        return self._dice

    def roll_dice(self) -> None:
        self._dice_list = [Die() for _ in range(self._dice)]
        self._dice_values = [die.value for die in self._dice_list]
        self._dice_icons = [die.icon for die in self._dice_list]

        for n, die in enumerate(self._dice_list):
            die._number = n + 1
