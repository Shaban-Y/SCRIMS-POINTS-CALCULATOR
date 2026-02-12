import csv
import json
from pathlib import Path

from .models import MatchResult, Team
from .scoring import ScoringProfile


def load_teams(path: str | Path) -> dict[int, Team]:
    teams: dict[int, Team] = {}
    with Path(path).open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            number = int(row["team_number"])
            teams[number] = Team(name=row["team_name"], number=number)
    return teams


def load_results(path: str | Path) -> list[MatchResult]:
    results: list[MatchResult] = []
    with Path(path).open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            results.append(
                MatchResult(
                    team_number=int(row["team_number"]),
                    placement=int(row["placement"]),
                    kills=int(row["kills"]),
                )
            )
    return results


def load_scoring(path: str | Path) -> ScoringProfile:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    placement_points = {int(k): int(v) for k, v in data["placement_points"].items()}
    return ScoringProfile(
        kill_points=int(data["kill_points"]),
        placement_points=placement_points,
    )
