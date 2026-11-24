# Submission

**Deadline:** Sunday, 20 December 2026, end of day — upload to Moodle (one member uploads).

## Contents of `AA202627nn.zip` (`nn` = Moodle group number)

- [ ] `AA_202627_Project.ipynb` — completed, executed, cleaned (only relevant experiments)
- [ ] `AA_202627_Project.html` — HTML export **with all outputs**
- [ ] `src/` helper modules imported by the notebook (if any)
- [ ] Orange workflow files (`.ows`) and their figures, if Orange is used
- [ ] `requirements.txt`
- [ ] Any other file needed to reproduce the results

## Final checklist

- [ ] Group number confirmed on Moodle
- [ ] Kernel restarted and notebook run top to bottom without errors
- [ ] Every experiment has objective, method, parameters, results, interpretation and limitations
- [ ] Every decision justified; results critically discussed (code-only notebooks are capped at 10/20)
- [ ] External sources cited
- [ ] HTML export opened and checked (plots and tables visible)
- [ ] ZIP name is exactly `AA202627nn.zip`

## Building the package

```bash
jupyter nbconvert --to html notebooks/AA_202627_Project.ipynb --output-dir submission/
# then zip the notebook, the HTML and the required files as AA202627nn.zip
```

Generated ZIP and HTML files in this folder are git-ignored.
