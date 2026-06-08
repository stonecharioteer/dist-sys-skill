#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT / "index.yaml"
DIST_SYS_HOME = Path(
    os.environ.get("DIST_SYS_HOME", str(Path.home() / ".dist-sys"))
).expanduser()


@dataclass
class Attempt:
    attempt_id: str
    date: str | None
    status: str | None
    review_status: str | None
    assets_count: int


@dataclass
class Exercise:
    number: int
    title: str
    tier: str
    prerequisites: list[int]
    folder: Path
    attempts: list[Attempt]

    @property
    def latest(self) -> Attempt | None:
        return self.attempts[-1] if self.attempts else None

    @property
    def has_in_progress(self) -> bool:
        return any((a.status or "").strip() == "in_progress" for a in self.attempts)

    @property
    def latest_unreviewed(self) -> bool:
        latest = self.latest
        return bool(latest and (latest.review_status or "not_reviewed") != "reviewed")


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if re.fullmatch(r"\d+", value):
        return int(value)
    return value


def load_index() -> list[dict[str, Any]]:
    lines = INDEX_PATH.read_text().splitlines()
    exercises: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("  - number:"):
            if current:
                exercises.append(current)
            current = {"number": int(line.split(":", 1)[1].strip())}
            i += 1
            continue
        if current is None:
            i += 1
            continue
        stripped = line.strip()
        if stripped.startswith("title:"):
            current["title"] = parse_scalar(stripped.split(":", 1)[1])
        elif stripped.startswith("tier:"):
            current["tier"] = parse_scalar(stripped.split(":", 1)[1])
        elif stripped.startswith("folder:"):
            current["folder"] = parse_scalar(stripped.split(":", 1)[1])
        elif stripped == "prerequisites:":
            prereqs: list[int] = []
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                if nxt.startswith("      - "):
                    prereqs.append(int(nxt.strip()[2:].strip()))
                    j += 1
                    continue
                if nxt.strip() == "[]":
                    j += 1
                    break
                break
            current["prerequisites"] = prereqs
            i = j
            continue
        i += 1
    if current:
        exercises.append(current)
    return exercises


def parse_metadata(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    if not path.exists():
        return data
    for line in path.read_text().splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def attempt_store_root() -> Path:
    DIST_SYS_HOME.mkdir(parents=True, exist_ok=True)
    return DIST_SYS_HOME


def submissions_dir_for(folder: Path) -> Path:
    return attempt_store_root() / folder.name / "submissions"


def load_exercises() -> list[Exercise]:
    result: list[Exercise] = []
    for item in load_index():
        folder = ROOT / item["folder"]
        subdir = submissions_dir_for(folder)
        attempts: list[Attempt] = []
        if subdir.exists():
            for attempt_dir in sorted(p for p in subdir.iterdir() if p.is_dir()):
                meta = parse_metadata(attempt_dir / "metadata.yaml")
                assets_count = 0
                assets_dir = attempt_dir / "assets"
                if assets_dir.exists():
                    assets_count = len([p for p in assets_dir.iterdir() if p.is_file()])
                attempts.append(
                    Attempt(
                        attempt_id=attempt_dir.name,
                        date=meta.get("date"),
                        status=meta.get("status"),
                        review_status=meta.get("review_status"),
                        assets_count=assets_count,
                    )
                )
        result.append(
            Exercise(
                number=item["number"],
                title=item["title"],
                tier=item["tier"],
                prerequisites=item.get("prerequisites", []),
                folder=folder,
                attempts=attempts,
            )
        )
    return result


def cmd_ls(exercises: list[Exercise], filter_name: str | None) -> int:
    selected = exercises
    if filter_name == "attempted":
        selected = [e for e in exercises if e.attempts]
    elif filter_name == "pending":
        selected = [e for e in exercises if e.has_in_progress or e.latest_unreviewed]

    if not selected:
        print("No matching exercises.")
        return 0

    print("| # | Exercise | Attempts | Latest | Status | Reviewed |")
    print("| --- | --- | ---: | --- | --- | --- |")
    for e in selected:
        latest = e.latest
        print(
            f"| {e.number:02d} | {e.title} | {len(e.attempts)} | "
            f"{latest.attempt_id if latest else '-'} | "
            f"{latest.status if latest and latest.status else '-'} | "
            f"{latest.review_status if latest and latest.review_status else '-'} |"
        )
    return 0


def prereqs_satisfied(exercise: Exercise, by_num: dict[int, Exercise]) -> bool:
    for prereq in exercise.prerequisites:
        ex = by_num.get(prereq)
        if ex is None or not ex.attempts:
            return False
    return True


def cmd_next(exercises: list[Exercise]) -> int:
    by_num = {e.number: e for e in exercises}

    in_progress = [e for e in exercises if e.has_in_progress]
    if in_progress:
        e = in_progress[0]
        print(f"recommended\t{e.number:02d}\t{e.title}\tresume in-progress attempt")
        return 0

    unreviewed = [e for e in exercises if e.latest_unreviewed]
    if unreviewed:
        e = unreviewed[0]
        print(
            f"recommended\t{e.number:02d}\t{e.title}\treview or continue latest unreviewed attempt"
        )
        return 0

    untouched = [
        e for e in exercises if not e.attempts and prereqs_satisfied(e, by_num)
    ]
    if not untouched:
        untouched = [e for e in exercises if not e.attempts]

    if not untouched:
        print(
            "recommended\t--\tAll exercises have at least one attempt\tconsider review or a new attempt"
        )
        return 0

    default = untouched[0]
    print(
        f"recommended\t{default.number:02d}\t{default.title}\tfirst untouched exercise with satisfied prerequisites"
    )
    alternatives = untouched[1:4]
    for e in alternatives:
        print(f"alternative\t{e.number:02d}\t{e.title}\talso a reasonable next step")
    return 0


def cmd_exercise_list(exercises: list[Exercise], number: int) -> int:
    ex = next((e for e in exercises if e.number == number), None)
    if ex is None:
        raise SystemExit(f"Unknown exercise: {number:02d}")
    if not ex.attempts:
        print(f"{number:02d}\t{ex.title}\tno attempts")
        return 0
    print("| Attempt ID | Date | Status | Reviewed | Assets |")
    print("| --- | --- | --- | --- | ---: |")
    for a in ex.attempts:
        print(
            f"| {a.attempt_id} | {a.date or '-'} | {a.status or '-'} | {a.review_status or '-'} | {a.assets_count} |"
        )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    p_ls = sub.add_parser("ls")
    p_ls.add_argument("filter", nargs="?", choices=["attempted", "pending"])

    sub.add_parser("next")

    p_ex_list = sub.add_parser("exercise-list")
    p_ex_list.add_argument("number", type=int)

    args = parser.parse_args()
    exercises = load_exercises()

    if args.command == "ls":
        return cmd_ls(exercises, args.filter)
    if args.command == "next":
        return cmd_next(exercises)
    if args.command == "exercise-list":
        return cmd_exercise_list(exercises, args.number)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
