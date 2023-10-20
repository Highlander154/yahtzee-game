import os
from time import sleep
from pprint import pprint
from .player import Player
from .checks import Checks
from pyfiglet import Figlet


class Game:
    def __init__(self):
        self._players: list[Player] = []
        self._round = 0

    @property
    def players(self):
        return self._players

    def cls(self):
        os.system("cls")

    def welcome_message(self) -> None:
        self.cls()
        f = Figlet(font="poison")
        print(f.renderText("YaHtZeE"))
        # print("\n==================")
        # print("Welcome to YAHTZEE")
        # print("==================")

    def number_of_players(self) -> int:
        while True:
            my_input = input("\n🎲  How many player will play the game 🎲: ")
            if my_input.isdigit():
                return int(my_input)

    def setup_players(self, num_players: int):
        self.cls()
        players = []
        for i in range(int(num_players)):
            player_name = input(f"\nPlease enter name for player {i+1}: ")
            is_cpu = input(f"\nis {player_name.title()} a human player (y/n): ").lower()
            while True:
                if is_cpu in ["y", "n"]:
                    is_cpu = True if is_cpu == "n" else False
                    players.append(Player(name=player_name, is_computer=is_cpu))
                    break
        self._players = players

    def player_info(self, player: Player):
        print("\n===========")
        print("PLAYER INFO")
        print("===========\n")
        print(f"Player Name: {player.name}")
        print(f"Computer Player: {player.is_computer}")
        print(f"{player.shaker}")
        print(f"Dice Values: {player.shaker.values}")
        print(f"Dice Icons: {player.shaker._dice_icons}")

    def roll_dice(self, player: Player):
        player.shaker.roll_dice()

    def lock_dice(self):
        pass

    def print_round(self) -> None:
        self.cls()
        frame = (6 + len(str(self._round))) * "="
        print("\n" + frame)
        print(f"ROUND {self._round}")
        print(frame)

    def print_roll(self, roll=int) -> None:
        print("\n======")
        print(f"ROLL {roll+1}")
        print("======")

    def show_die(self, player: Player):
        for value in player.shaker.values:
            print(value, end=" ")
            sleep(1)

    def run(self):
        self.welcome_message()
        num_players = self.number_of_players()
        self.setup_players(num_players)

        self._round += 1

        for player in self._players:
            for i in range(3):
                self.roll_dice(player)

                value_string = ""
                for value in player.shaker.values:
                    self.print_round()
                    print(f"\n{player.name.title()}'s turn")
                    print("\nRolling the dice ... ")
                    self.print_roll(roll=i)
                    print()
                    value_string += f"{value} "
                    print(value_string)
                    sleep(0.5)
                input("\npress key to continue")
                self.lock_dice()
            self.cls()
            check = Checks(player.shaker._dice_values)
            self.player_info(player)
            print()
            pprint(check.check_result)
            input("\npress key to continue")
