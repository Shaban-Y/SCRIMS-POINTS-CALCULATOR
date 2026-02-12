from dataclasses import dataclass


@dataclass(frozen=True)
class ScoringProfile:
    kill_points: int
    placement_points: dict[int, int]

    def placement_value(self, placement: int) -> int:
        return self.placement_points.get(placement, 0)
