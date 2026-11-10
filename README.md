# Student Result Management System

**Course:** Introduction to Python Programming  
**Project:** Student Result Management System  
**Language:** Python 3

## Description
A menu-driven application for registering students, recording five subject scores, calculating totals/averages/grades, producing report cards and class statistics, sorting records, and storing data in JSON.

## Requirements
- Python 3.8 or newer
- No third-party Python packages are required to run the application.

## How to run
1. Download or clone this repository.
2. Open a terminal in the `student_result_system` folder.
3. Run: `python main.py` (on some computers use `python3 main.py`).
4. Follow the numbered menu.
5. Records are saved automatically in `data/students.json`.

## Subjects and grading scale
Subjects: English, Mathematics, Physics, Chemistry and Biology.

| Average | Grade |
|---|---|
| 70–100 | A |
| 60–69.99 | B |
| 50–59.99 | C |
| 45–49.99 | D |
| Below 45 | F |

Each subject score must be between 0 and 100. The average is the total divided by the number of scores entered.

## Project files
- `main.py` — menu and application operations.
- `student.py` — Student class, totals, averages and grades.
- `results.py` — score entry and validation.
- `storage.py` — JSON loading and saving.
- `reports.py` — report cards, class report and text export.
- `data/students.json` — persistent student records.

## Important
This is an educational project. The grading bands are example bands chosen for this implementation and can be adjusted to match a school's official policy. Student data is stored locally; do not use real sensitive student information in a public demonstration repository.
