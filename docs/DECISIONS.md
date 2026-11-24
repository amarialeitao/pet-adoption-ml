# Decision log

Record every significant decision here so the team can defend it in the notebook. Newest first.

| # | Date | Decision | Reason | Status |
|---|---|---|---|---|
| D-005 | 2026-11-24 | Define `ADOPTION = 1` for `AdoptionSpeed` ∈ {0,1,2,3} and 0 for 4 | The template writes [0,4], which would label every pet as adopted; value 4 means "no adoption after 100 days" | **Proposed** — confirm with professor |
| D-004 | 2026-11-24 | Do not add a license for now | Course materials and Kaggle data have their own terms; choose a license for *our* code later as a team | Accepted |
| D-003 | 2026-11-24 | Include the professor's notebook template in `notebooks/`; exclude the data files and lookup tables | The template is the deliverable we edit. The CSV files derive from Kaggle competition data whose redistribution terms we could not confirm, and no permission from the professor is recorded | Accepted — revisit if the professor allows publishing the data |
| D-002 | 2026-11-24 | Repository name `pet-adoption-ml` (instead of the longer name proposed in CLAUDE.md) | Shorter, cleaner name chosen by the repo owner | Accepted |
| D-001 | 2026-11-24 | English for all repository content; Conventional Commits; issues + project board for tracking | International team; consistent history | Accepted |

## Template

```markdown
| D-XXX | YYYY-MM-DD | What was decided | Why (evidence, alternatives considered) | Proposed / Accepted / Superseded by D-YYY |
```
