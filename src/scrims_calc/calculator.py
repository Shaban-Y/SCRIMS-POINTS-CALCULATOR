from .models import MatchResult, Team, TeamScore
from .scoring import ScoringProfile


def calculate_scores(
    teams_by_number: dict[int, Team],
    results: list[MatchResult],
    scoring: ScoringProfile,
) -> list[TeamScore]:
    scores: list[TeamScore] = []
    for result in results:
        team = teams_by_number.get(result.team_number)
        if team is None:
            team_name = f"Unknown Team {result.team_number}"
        else:
            team_name = team.name

        placement_points = scoring.placement_value(result.placement)
        kill_points = result.kills * scoring.kill_points
        total_points = placement_points + kill_points

        scores.append(
            TeamScore(
                team_name=team_name,
                team_number=result.team_number,
                placement=result.placement,
                kills=result.kills,
                placement_points=placement_points,
                kill_points=kill_points,
                total_points=total_points,
            )
        )

    return sorted(scores, key=lambda s: (-s.total_points, s.placement, -s.kills))
