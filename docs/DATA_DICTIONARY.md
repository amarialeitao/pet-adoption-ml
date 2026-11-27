# Data dictionary

Source: `PetFinder_dataset.csv` (course version) and the lookup tables `breed_labels.csv`, `color_labels.csv`, `state_labels.csv`, all supplied by the professor. Code meanings follow the original Kaggle data description; the professor's notebook takes precedence where they differ.

> The counts below come from `notebooks/01_EDA.ipynb` (27 Nov 2026), using the loader in `src/preprocessing/loader.py` (see §4). They are descriptive facts about the file, not modelling results.
>
> **Correction (27 Nov 2026).** The first version of this page (24 Nov) used a simpler parser and reported missing values in `Type`, `Age`, `Breed1`, `AdoptionSpeed` and out-of-domain codes (e.g. `Gender = 265`, `VideoAmt = 41401`). Those were **parsing artefacts** from shifted columns. With the current loader, only `Name` has missing values and every code is within its domain.

## 1. Main table — 14,993 rows × 24 columns

| Column | Type | Description | Codes / range observed |
|---|---|---|---|
| `Type` | categorical | Type of animal | 1 = Dog (8,132), 2 = Cat (6,861) |
| `Name` | text | Name of the pet | **1,257 empty**; 129 placeholders such as "No Name Yet"; ~840 group names ("2 Kittens") |
| `Age` | numeric | Age when listed, **in months** | 0–255; median 3; 75% of ages ≥ 12 are whole years |
| `Breed1` | categorical | Primary breed → `breed_labels.csv` | 176 distinct; 307 "Mixed Breed" 39.5%; 0 (none) in 5 rows; 12 rows with a breed of the other species |
| `Breed2` | categorical | Secondary breed (0 = none) → `breed_labels.csv` | 0 in 72% of rows; equals `Breed1` in 1,510 rows; 3 rows with a breed of the other species |
| `Gender` | categorical | 1 = Male, 2 = Female, 3 = Mixed (group listing) | 5,536 / 7,277 / 2,180 |
| `Color1`–`Color3` | categorical | Colours → `color_labels.csv` (0 = none) | All codes valid; `Color2`/`Color3` never repeat a previous colour |
| `MaturitySize` | ordinal | 1 = Small, 2 = Medium, 3 = Large, 4 = Extra Large, 0 = Not specified | 3,395 / 10,305 / 1,260 / 33; 0 never used |
| `FurLength` | ordinal | 1 = Short, 2 = Medium, 3 = Long, 0 = Not specified | 8,808 / 5,361 / 824; 0 never used |
| `Vaccinated` | categorical | 1 = Yes, 2 = No, 3 = Not sure | 5,898 / 7,227 / 1,868 |
| `Dewormed` | categorical | 1 = Yes, 2 = No, 3 = Not sure | 8,397 / 4,815 / 1,781 |
| `Sterilized` | categorical | 1 = Yes, 2 = No, 3 = Not sure | 3,101 / 10,077 / 1,815 |
| `Health` | ordinal | 1 = Healthy, 2 = Minor injury, 3 = Serious injury, 0 = Not specified | 14,478 / 481 / 34; 0 never used |
| `Quantity` | numeric | Number of pets in the listing | 1–20; 1 in 77% of rows |
| `Fee` | numeric | Adoption fee (0 = free) | 0–3,000; 0 in 84% of rows |
| `State` | categorical | Malaysian state → `state_labels.csv` | 14 of 15 states used; Selangor 8,714 and Kuala Lumpur 3,845 |
| `RescuerID` | ID | Anonymised rescuer | 5,595 distinct; 3,783 with one listing; largest 459 |
| `VideoAmt` | numeric | Number of videos uploaded | 0–8; 0 in 96% of rows |
| `Description` | text | Free-text profile, mainly English; some Malay and Chinese | Never empty; contains commas, quotes, line breaks |
| `PetID` | ID | Unique listing ID (9 characters) | No duplicates; but 8 pairs of rows identical in every other column |
| `PhotoAmt` | numeric | Number of photos uploaded | 0–30, stored as float (e.g. `2.0`); 0 in 341 rows |
| `AdoptionSpeed` | **target**, ordinal | 0 same day · 1 = 1–7 days · 2 = 8–30 days · 3 = 31–90 days · 4 = no adoption after 100 days | 0: 410 · 1: 3,090 · 2: 4,037 · 3: 3,259 · 4: 4,197 · no missing values |

### Derived target (required by the assignment)

| Column | Definition |
|---|---|
| `ADOPTION` | 1 if `AdoptionSpeed` ∈ {0, 1, 2, 3} (adopted), 0 if `AdoptionSpeed` = 4 (not adopted), as defined in the updated template (26 Nov 2026). Balance: 10,796 (72.0%) / 4,197 (28.0%). |

## 2. Lookup tables

| File | Columns | Rows | Notes |
|---|---|---|---|
| `breed_labels.csv` | `BreedID`, `Type`, `BreedName` | 307 | 241 dog breeds (`Type` = 1), 66 cat breeds (`Type` = 2) |
| `color_labels.csv` | `ColorID`, `ColorName` | 7 | Black, Brown, Golden, Yellow, Cream, Gray, White |
| `state_labels.csv` | `StateID`, `StateName` | 15 | Malaysian states and federal territories |

## 3. Data-quality issues

See `reports/EDA_DIAGNOSTIC.md` §3–4 for details and proposed handling.

1. **Missing values:** only `Name` (1,257 rows). "Not sure" (code 3) in `Vaccinated`, `Dewormed`, `Sterilized` (12–13% each) is missing information in disguise.
2. **No out-of-domain codes** in any coded column.
3. **Inconsistencies between columns:** breed of the wrong species (15 rows), `Breed1 = 0` (5), `Breed2 = Breed1` (1,510), sterilised at ≤ 3 months (279).
4. **Implausible or skewed values:** `Age` up to 255 months, `Fee` up to 3,000, age heaping on whole years.
5. **Duplicates:** 8 pairs of listings identical except for `PetID`.
6. **Encoding:** 147 names contain mis-encoded (double-decoded UTF-8) characters.

## 4. How to load the CSV (important)

`pd.read_csv("PetFinder_dataset.csv")` **does not parse this file correctly**:

- every record ends with a run of `;` (an Excel export artefact);
- about 60% of records are wrapped in one pair of outer quotes with inner quotes doubled (`""`);
- many `Description` values contain unquoted commas, line breaks and `";"` fragments;
- a few descriptions contain characters such as U+0085 that Python's `str.splitlines()` treats as line breaks.

Use `src.preprocessing.loader.load_petfinder`. It splits the file on `\n` only, ends a record on the line that finishes with `,<PetID>,<PhotoAmt>,<AdoptionSpeed>`, reads the first 20 fields from the start (handling quoted names), and keeps the rest as `Description`. It recovers all 14,993 records with every numeric field parsed.

## 5. Open questions

1. ~~`ADOPTION` definition.~~ **Resolved** by the updated template (26 Nov 2026): `ADOPTION = 1` for `AdoptionSpeed` ∈ {0,1,2,3}.
2. ~~Class 0 missing from the template.~~ **Resolved**: class 0 = adopted on the same day.
3. How to fix breed/species inconsistencies (unknown vs. species' mixed code).
4. Whether to drop or merge the 8 duplicate pairs.
