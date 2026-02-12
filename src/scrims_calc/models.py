from dataclasses import dataclass


@dataclass(frozen=True)
class Team:
    name: str
    number: int


@dataclass(frozen=True)
class MatchResult:
    team_number: int
    placement: int
    kills: int


@dataclass(frozen=True)
class TeamScore:
    team_name: str
    team_number: int
    placement: int
    kills: int
    placement_points: int
    kill_points: int
    total_points: int
