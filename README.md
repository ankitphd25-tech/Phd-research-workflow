# Project Title

Student Experiment Data Analysis and Visualization

---

# Project Structure

```
project/
│── docs/
│   ├── Expected outputs
│   ├── Files and folders used
│   ├── Future scope
│   ├── How to run the project.md
│   ├── Project structure
│   ├── Project title.md
│   ├── methodology.md
│   ├── reproducibility_checklist.md
│   └── analysis_notes.md
│
│── student_data.csv
│── cleaned_student_data.csv
│── analysis.py
│── requirements.txt
│── README.md
```

---

# Files and Folders Used

* `student_data.csv` → Original dataset
* `cleaned_student_data.csv` → Dataset after handling missing values
* `analysis.py` → Python script for preprocessing and visualization
* `docs/` → Contains all project documentation
* `requirements.txt` → List of dependencies

---

# How to Run the Project

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the script:

```
python analysis.py
```

3. View generated outputs (plots and cleaned dataset)

---

# Expected Outputs

* Cleaned dataset (`cleaned_student_data.csv`)
* Visualizations:

  * Student ID vs Temperature (line/scatter plot)
  * Histogram of experiment scores
  * Box plot for score distribution

---

# Assumptions Made in Data Cleaning and Visualization

* Missing values are randomly distributed
* Mean imputation (84.11) is appropriate for `experiment_score`
* Dataset contains no significant outliers
* `student_id` is used only for identification, not analysis

---

# Future Scope

* Apply advanced imputation techniques (median, ML-based)
* Include more features for deeper analysis
* Use machine learning models for prediction
* Improve visualizations and statistical analysis
* Increase dataset size for better reliability
