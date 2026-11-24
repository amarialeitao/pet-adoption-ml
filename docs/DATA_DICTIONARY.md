# Data dictionary

Source: `PetFinder_dataset.csv` (course version) and the lookup tables `breed_labels.csv`, `color_labels.csv`, `state_labels.csv`, all supplied by the professor. Code meanings follow the original Kaggle data description; the professor's notebook takes precedence where they differ.

> The counts below come from a **first audit** run while setting up the repository (24 Nov 2026), using a custom parser (see §4). They are descriptive facts about the file, not modelling results. They should be re-checked in the notebook (issue: *Audit data quality*).

## 1. Main table — 14,993 rows × 24 columns

| Column | Type | Description | Codes / range observed |
|---|---|---|---|
| `Type` | categorical | Type of animal | 1 = Dog (8,128), 2 = Cat (6,855); **10 missing** |
| `Name` | text | Name of the pet | 1,257 empty; values such as "No Name Yet" also occur |
| `Age` | numeric | Age when listed, **in months** | 0–255; median 3; **9 missing** |
| `Breed1` | categorical | Primary breed → `breed_labels.csv` | 307 = "Mixed Breed" is the most common; **4 missing** |
| `Breed2` | categorical | Secondary breed (0 = none) → `breed_labels.csv` | **1 missing** |
| `Gender` | categorical | 1 = Male, 2 = Female, 3 = Mixed (group listing) | 1: 5,536 · 2: 7,275 · 3: 2,173 · **invalid: 0 (4), 265, 266, 307 (4 total)**, 1 missing |
| `Color1`–`Color3` | categorical | Colours → `color_labels.csv` (0 = none) | Out-of-range codes occur (e.g. `Color1` = 266, `Color2` = 307) |
| `MaturitySize` | ordinal | 1 = Small, 2 = Medium, 3 = Large, 4 = Extra Large, 0 = Not specified | **invalid: 6 (1), 7 (4)** |
| `FurLength` | ordinal | 1 = Short, 2 = Medium, 3 = Long, 0 = Not specified | **invalid: 7 (2)** |
| `Vaccinated` | categorical | 1 = Yes, 2 = No, 3 = Not sure | 5,900 / 7,226 / 1,867 |
| `Dewormed` | categorical | 1 = Yes, 2 = No, 3 = Not sure | **invalid: 5 (1)** |
| `Sterilized` | categorical | 1 = Yes, 2 = No, 3 = Not sure | 3,105 / 10,074 / 1,814 |
| `Health` | ordinal | 1 = Healthy, 2 = Minor injury, 3 = Serious injury, 0 = Not specified | 14,472 / 487 / 34 |
| `Quantity` | numeric | Number of pets in the listing | 1–20 |
| `Fee` | numeric | Adoption fee (0 = free) | 0–3,000; median 0 |
| `State` | categorical | Malaysian state → `state_labels.csv` | Selangor 8,709 and Kuala Lumpur 3,843 dominate; **invalid: 0, 3, 4, 50 (9 rows)** |
| `RescuerID` | ID | Anonymised rescuer | 5,596 distinct |
| `VideoAmt` | numeric | Number of videos uploaded | Mostly 0; **max 41,401 (looks like a State code in the wrong column)**; 5 missing |
| `Description` | text | Free-text profile, mainly English; some Malay and Chinese | Contains commas, quotes, line breaks and some mis-encoded characters |
| `PetID` | ID | Unique listing ID | No duplicates found |
| `PhotoAmt` | numeric | Number of photos uploaded | 0–30, stored as float (e.g. `2.0`) |
| `AdoptionSpeed` | **target**, ordinal | 0 same day · 1 = 1–7 days · 2 = 8–30 days · 3 = 31–90 days · 4 = not adopted after 100 days | 0: 410 · 1: 3,085 · 2: 4,034 · 3: 3,259 · 4: 4,194 · **11 missing / non-numeric** |

### Derived target (required by the assignment)

| Column | Definition |
|---|---|
| `ADOPTION` | 1 if `AdoptionSpeed` ∈ {0, 1, 2, 3} (adopted), 0 if `AdoptionSpeed` = 4 (not adopted). Expected balance ≈ 72% / 28%. See open issue §5.1. |

## 2. Lookup tables

| File | Columns | Rows | Notes |
|---|---|---|---|
| `breed_labels.csv` | `BreedID`, `Type`, `BreedName` | 307 | 241 dog breeds (`Type` = 1), 66 cat breeds (`Type` = 2) |
| `color_labels.csv` | `ColorID`, `ColorName` | 7 | Black, Brown, Golden, Yellow, Cream, Gray, White |
| `state_labels.csv` | `StateID`, `StateName` | 15 | Malaysian states and federal territories |

## 3. Data-quality issues found so far

1. **Missing values** in `Type`, `Age`, `Breed1`, `Breed2`, `Gender`, `VideoAmt` and the target `AdoptionSpeed` (11 rows).
2. **Out-of-domain codes** in `Gender`, `MaturitySize`, `FurLength`, `Dewormed`, `State`, `Color1`, `Color2`.
3. **Values that look shifted into the wrong column** (e.g. breed codes 265/266/307 inside `Gender`, a state code inside `VideoAmt`).
4. **Possible typos / outliers**: `Age` up to 255 months (21 years), `Fee` up to 3,000.
5. The professor confirms the data "can contain errors/typos" on purpose, so cleaning choices are part of the graded work.

## 4. How to load the CSV (important)

`pd.read_csv("PetFinder_dataset.csv")` **does not parse this file correctly**:

- every line ends with `;;;;;;;;;;` (an Excel export artefact);
- roughly 9,100 lines are wrapped in one pair of outer quotes with inner quotes doubled (`""`);
- many `Description` values contain unquoted commas;
- a few descriptions contain line breaks or mis-encoded text.

A robust approach that recovered all 14,993 records in the audit: strip the trailing semicolons, remove the outer quotes and un-double inner quotes, then take the **first 20 fields**, the **last 3 fields** (`PetID`, `PhotoAmt`, `AdoptionSpeed`) and join everything in between as `Description`. This will be implemented and documented in the notebook's *0.1 Loading Data* section (issue: *Robust data loader*).

## 5. Open questions

1. **`ADOPTION` definition.** The template says `ADOPTION = 1` when `AdoptionSpeed` ∈ **[0,4]**, but 4 means "not adopted", so the interval should be **[0,3]**. We will use [0,3] and confirm with the professor.
2. **Class 0 is missing from the template's list.** The notebook lists codes 1–4 only; the original Kaggle definition is "adopted on the same day". To confirm with the professor.
3. **The 11 rows without a valid target**: drop, or investigate whether the value was shifted?
4. **Rows with shifted columns**: repair or drop?
