from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models import Grid, GameState, Mark
    from tic_tac_toe.game.players import Player

import re

from .exceptions import InvalidGameState


def validate_grid(grid: Grid) -> None:
    if not re.match(r"^[\sXO]{9}$", grid.cells):
        raise ValueError(f"Must contain 9 cells with only 'X', 'O' or space")


def validate_game_state(game_state: GameState) -> None:
    validate_number_of_marks(game_state.grid)
    validate_starting_mark(game_state.grid, game_state.starting_mark)
    validate_winner(game_state.grid, game_state.starting_mark, game_state.winner)


def validate_number_of_marks(grid: Grid) -> None:
    if abs(grid.x_count - grid.o_count) > 1:
        raise InvalidGameState("Difference between X and O count must be 0 or 1")


def validate_starting_mark(grid: Grid, starting_mark: Mark) -> None:
    if grid.x_count > grid.o_count:
        if starting_mark != "X":
            raise InvalidGameState("Wrong starting mark")
    elif grid.x_count < grid.o_count:
        if starting_mark != "O":
            raise InvalidGameState("Wrong starting mark")


def validate_winner(
        grid: Grid, starting_mark: Mark, winner: str | None) -> None:
    if winner == "X":
        if starting_mark == "X":
            if grid.x_count <= grid.o_count:
                raise InvalidGameState("Invalid winner! Wrong number of X")
        else:
            if grid.x_count != grid.o_count:
                raise InvalidGameState("Invalid winner! Wrong number of X")
    elif winner == "O":
        if starting_mark == "O":
            if grid.x_count < grid.o_count:
                raise InvalidGameState("Invalid winner! Wrong number of O")
        else:
            if grid.x_count != grid.o_count:
                raise InvalidGameState("Invalid winner! Wrong number of O")


def validate_players(player1: Player, player2: Player) -> None:
    if player1.mark is player2.mark:
        raise ValueError("Players must use different marks")
