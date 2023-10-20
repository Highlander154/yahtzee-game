class Checks:
    def __init__(self, values: list) -> None:
        self._val_set = set(values)
        self._val_lst = values
        self._val_str = self.values_string()
        self._check_result = {}
        self.checks()

    def __repr__(self) -> str:
        return "Shaker Dice Checks"

    @property
    def check_result(self) -> dict:
        return self._check_result

    @property
    def values_list(self) -> list:
        return self._val_lst

    def values_string(self) -> str:
        tmp = sorted(self._val_lst)
        tmp = [str(i) for i in tmp]
        return "".join(tmp)

    def sum_all_eyes(self) -> int:
        return sum(self._val_lst)

    def numbers(self, num=1) -> tuple[bool, int]:
        if not num in self._val_lst:
            return False, 0
        return True, self._val_lst.count(num) * num

    def three_of_a_kind(self) -> tuple[bool, int]:
        for i in range(1, 7):
            if self._val_lst.count(i) >= 3:
                return True, self.sum_all_eyes()
        return False, 0

    def four_of_a_kind(self) -> tuple[bool, int]:
        for i in range(1, 7):
            if self._val_lst.count(i) >= 4:
                return True, self.sum_all_eyes()
        return False, 0

    def full_house(self) -> tuple[bool, int]:
        if not len(self._val_set) == 2:
            return False, 0
        if self._val_lst.count(list(self._val_set)[1]) not in [1, 4]:
            return True, 25
        return False, 0

    def small_straight(self) -> tuple[bool, int]:
        if (
            "1234" in self._val_str
            or "2345" in self._val_str
            or "3456" in self._val_str
        ):
            return True, 30
        return False, 0

    def large_straight(self) -> tuple[bool, int]:
        if "12345" in self._val_str or "23456" in self._val_str:
            return True, 40
        return False, 0

    def yahtzee(self) -> tuple[bool, int]:
        if len(self._val_set) == 1:
            return True, 50
        return False, 0

    def chance(self) -> tuple[bool, int]:
        return True, self.sum_all_eyes()

    def checks(self) -> dict:
        self._check_result["1. aces"] = self.numbers(num=1)
        self._check_result["2. twos"] = self.numbers(num=2)
        self._check_result["3. threes"] = self.numbers(num=3)
        self._check_result["4. fours"] = self.numbers(num=4)
        self._check_result["5. fives"] = self.numbers(num=5)
        self._check_result["6. sixes"] = self.numbers(num=6)
        self._check_result["A. 3_of_a_kind"] = self.three_of_a_kind()
        self._check_result["B. 4_of_a_kind"] = self.four_of_a_kind()
        self._check_result["C. full_house"] = self.full_house()
        self._check_result["D. small_straight"] = self.small_straight()
        self._check_result["E. large_straight"] = self.large_straight()
        self._check_result["F. yahtzee"] = self.yahtzee()
        self._check_result["G. chance"] = self.chance()
        return self._check_result
