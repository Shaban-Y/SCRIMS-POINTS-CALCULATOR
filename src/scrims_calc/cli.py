import argparse

from .calculator import calculate_scores
from .io import load_results, load_scoring, load_teams


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Calculate scrim points from teams/results/scoring files")
    parser.add_argument("--teams", required=True, help="CSV path with team_name,team_number")
    parser.add_argument("--results", required=True, help="CSV path with team_number,placement,kills")
    parser.add_argument("--scoring", required=True, help="JSON scoring profile path")
    return parser


def main() -> None:
    args = build_parser().parse_args()

    teams = load_teams(args.teams)
    results = load_results(args.results)
    scoring = load_scoring(args.scoring)

    final_scores = calculate_scores(teams, results, scoring)

    print("rank,team_name,team_number,placement,kills,placement_points,kill_points,total_points")
    for idx, score in enumerate(final_scores, start=1):
        print(
            f"{idx},{score.team_name},{score.team_number},{score.placement},{score.kills},"
            f"{score.placement_points},{score.kill_points},{score.total_points}"
        )


if __name__ == "__main__":
    main()
