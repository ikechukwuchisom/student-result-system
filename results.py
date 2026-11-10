from datetime import date

SUBJECTS = ["English", "Mathematics", "Physics", "Chemistry", "Biology"]


def get_valid_score(subject):
    """Ask repeatedly until a valid score from 0 to 100 is entered."""
    while True:
        try:
            score = float(input(f"Enter {subject} score (0-100): "))
            if 0 <= score <= 100:
                return score
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a number, for example 76 or 82.5.")


def enter_scores(student):
    """Enter or replace scores for the five required subjects."""
    print(f"\nEntering results for {student.full_name}")
    for subject in SUBJECTS:
        student.scores[subject] = get_valid_score(subject)
    student.result_date = date.today().isoformat()
    print("Scores saved in the current session.")


def result_summary(student):
    return {
        "total": student.total_score(),
        "average": student.average_score(),
        "grade": student.grade(),
    }
