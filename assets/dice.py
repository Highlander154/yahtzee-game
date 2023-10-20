from random import randint

# =========
# DIE CLASS
# =========


class Die:
    """Class for generating an instance of a die"""

    DICE_ICONS = "⚀⚁⚂⚃⚄⚅"

    def __init__(self, sides: int = 6, value: int = None) -> None:
        """Initializes the die instance

        Args:
            sides (int, optional): set a manual value for the sides of the die. Defaults to 6.
            value (int, optional): set a manual value for the visible value of the die. Defaults to None.
        """
        self._number = 1
        self._sides = sides

        if value:
            self._value = value
            self._img = f"img\die_{value:0>2}.png"
            self._icon = Die.DICE_ICONS[value - 1]
        else:
            self.roll()

    def __repr__(self) -> str:
        return f"Die {self._number}. (value: {self._value})"

    @property
    def sides(self) -> int:
        """
        Returns:
            int: sides of the dice
        """
        return self._sides

    @sides.setter
    def sides(self, sides: int) -> None:
        """
        Setter for the maximum amount of sides of the dice

        Args:
            sides (int): sides of the dice

        """
        self._sides = sides

    @property
    def value(self) -> int:
        """
        Returns:
            int: current value of the die
        """
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        """
        Setter use for manually overriding the current value of the die.

        Args:
            value (int): value of the die
        """

        self._value = value

    @property
    def icon(self) -> str:
        return self._icon

    @property
    def image(self) -> str:
        """
        Returns:
            str: path and filename of the image used for displaying the die
        """

        return self._img

    @image.setter
    def image(self, filename: str) -> None:
        """
        Setter for the path and filename of the image used for displaying the die.

        Args:
            filename (str): path and filename of the corresponding die image.
        """

        self._img = filename

    def roll(self) -> None:
        """
        Class method for rolling the die.
        The method generates a pseudo random number between 1 and the maximum amount of sides of the die
        and also generated the path and filename of the picture used for displaying the die.
        """

        value = randint(1, self._sides)
        self._value = value
        self._img = f"img\die_{value:0>2}.png"
        self._icon = Die.DICE_ICONS[value - 1]
