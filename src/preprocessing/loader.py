"""Robust loader for the course version of ``PetFinder_dataset.csv``.

``pd.read_csv`` cannot parse the file as supplied, because:

* every record ends with a run of semicolons (an Excel export artefact);
* about 60% of the records are wrapped in one pair of outer quotes, with the
  inner quotes doubled (``""``);
* many ``Description`` values contain unquoted commas, line breaks and stray
  ``";"`` fragments (semicolons in the original text that Excel split on);
* a few descriptions contain characters such as U+0085 that Python treats as
  line breaks, so the file must be split on ``\\n`` only.

Strategy (see docs/DATA_DICTIONARY.md, section 4):

1. Split the file on ``\\n``. A record ends on the line whose end matches
   ``,<PetID: 9 chars>,<PhotoAmt>,<AdoptionSpeed>``; any other line is a
   continuation of a multi-line description.
2. Read the last 3 fields (``PetID``, ``PhotoAmt``, ``AdoptionSpeed``) from the
   end of the record.
3. Unwrap the outer quotes, read ``Type``, then ``Name`` (which may itself be a
   quoted CSV field containing commas), then the next 18 simple fields
   (``Age`` ... ``VideoAmt``).
4. Everything left is ``Description``.

The function returns the values as found: numeric columns are converted with
``errors="coerce"`` (anything non-numeric becomes NaN), but nothing is
corrected or dropped. Cleaning decisions belong in the notebook.
"""

from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

COLUMNS = [
    "Type", "Name", "Age", "Breed1", "Breed2", "Gender", "Color1", "Color2",
    "Color3", "MaturitySize", "FurLength", "Vaccinated", "Dewormed",
    "Sterilized", "Health", "Quantity", "Fee", "State", "RescuerID",
    "VideoAmt", "Description", "PetID", "PhotoAmt", "AdoptionSpeed",
]
NUMERIC_COLUMNS = [
    "Type", "Age", "Breed1", "Breed2", "Gender", "Color1", "Color2", "Color3",
    "MaturitySize", "FurLength", "Vaccinated", "Dewormed", "Sterilized",
    "Health", "Quantity", "Fee", "State", "VideoAmt", "PhotoAmt",
    "AdoptionSpeed",
]
N_SIMPLE_AFTER_NAME = 18  # Age ... VideoAmt

_TAIL = re.compile(r',([0-9a-z]{9}),([^,]*),([^,]*)$')


def _strip_end(line: str) -> str:
    return line.rstrip("\r").rstrip(";").rstrip().rstrip('"')


def _read_quoted(text: str, start: int) -> tuple[str, int]:
    """Read a CSV quoted field starting at ``text[start] == '"'``.

    Returns the unescaped value and the index just after the closing quote.
    """
    i, out = start + 1, []
    while i < len(text):
        if text[i] == '"':
            if i + 1 < len(text) and text[i + 1] == '"':
                out.append('"')
                i += 2
                continue
            return "".join(out), i + 1
        out.append(text[i])
        i += 1
    raise ValueError(f"Unterminated quoted field: {text[start:start + 60]!r}")


def _parse_record(record: str) -> list[str]:
    body = _strip_end(record)
    tail = _TAIL.search(body)
    pet_id, photo_amt, speed = tail.groups()
    head = body[: tail.start()]
    if head.startswith('"'):
        head = head[1:].replace('""', '"')

    type_, rest = head.split(",", 1)
    if rest.startswith('"'):
        name, end = _read_quoted(rest, 0)
        rest = rest[end + 1:]  # skip the comma after the closing quote
    else:
        name, rest = rest.split(",", 1)

    parts = rest.split(",", N_SIMPLE_AFTER_NAME)
    simple, description = parts[:N_SIMPLE_AFTER_NAME], parts[N_SIMPLE_AFTER_NAME]
    description = description.strip()
    if len(description) >= 2 and description[0] == '"' and description[-1] == '"':
        description = description[1:-1]
    description = description.replace('";"', ";")
    return [type_, name, *simple, description, pet_id, photo_amt, speed]


def _records(text: str):
    """Yield logical records (header excluded), joining multi-line descriptions."""
    lines = text.split("\n")[1:]
    buffer: list[str] = []
    for line in lines:
        if not buffer and not line.strip():
            continue
        buffer.append(line.rstrip("\r"))
        if _TAIL.search(_strip_end(line)):
            yield " ".join(buffer)
            buffer = []
    if buffer:
        raise ValueError(f"Trailing incomplete record: {buffer[0][:80]!r}")


def load_petfinder(path: str | Path) -> pd.DataFrame:
    """Load ``PetFinder_dataset.csv`` into a DataFrame without altering values."""
    text = Path(path).read_bytes().decode("utf-8")
    df = pd.DataFrame([_parse_record(r) for r in _records(text)], columns=COLUMNS)
    for col in NUMERIC_COLUMNS:
        df[col] = pd.to_numeric(df[col].str.strip(), errors="coerce")
    for col in ["Name", "Description", "RescuerID"]:
        df[col] = df[col].str.strip().replace("", pd.NA)
    return df


def load_labels(raw_dir: str | Path) -> dict[str, pd.DataFrame]:
    """Load the three lookup tables (breeds, colours, states)."""
    raw_dir = Path(raw_dir)
    return {
        "breed": pd.read_csv(raw_dir / "breed_labels.csv"),
        "color": pd.read_csv(raw_dir / "color_labels.csv"),
        "state": pd.read_csv(raw_dir / "state_labels.csv"),
    }
