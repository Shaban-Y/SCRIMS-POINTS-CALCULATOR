# SCRIMS Points Calculator

A starter implementation for calculating Call of Duty private room scrim points from team result screenshots.

## What this solves

- Maps uploaded team names to in-game team numbers (e.g., `Alpha Squad 4` means team number `4`).
- Accepts extracted screenshot values (kills/placement per team).
- Calculates total points using a scoring system profile of your choice.

## Suggested end-to-end flow

1. **Upload teams list** (names ending in team number).
2. **Upload screenshot** of private room team results.
3. **Extract values from screenshot** using OCR (Tesseract/EasyOCR/cloud vision).
4. **Normalize OCR output** into structured fields:
   - `team_number`
   - `placement`
   - `kills`
5. **Run calculator** with selected scoring profile.
6. **Publish leaderboard** by total points.

## Included starter CLI

This repo includes a small Python CLI that expects:

- `teams.csv` (Team Name, Team Number)
- `results.csv` (Team Number, Placement, Kills)
- `scoring.json` (placement + kill points)

Then computes totals and prints rankings.

## Quick start

```bash
python3 -m src.scrims_calc.cli \
  --teams examples/teams.csv \
  --results examples/results.csv \
  --scoring examples/scoring_codm.json
```

## Example scoring profile format

```json
{
  "kill_points": 1,
  "placement_points": {
    "1": 15,
    "2": 12,
    "3": 10,
    "4": 8,
    "5": 6,
    "6": 4,
    "7": 2,
    "8": 1
  }
}
```

## OCR integration note

The current implementation starts **after OCR**. You can plug in any OCR engine and map its output into `results.csv` format.

A practical next step is adding an OCR adapter module that:

- Crops the scoreboard region,
- Reads rows (team number / kills / placement),
- Applies cleanup rules for OCR mistakes (e.g., `O` vs `0`, `I` vs `1`).

## Future extensions

- Web app upload flow (FastAPI + React).
- Multiple match aggregation (series/week).
- Validation UI to fix OCR-detected values before scoring.
- Export to CSV/Google Sheets/Discord embeds.
