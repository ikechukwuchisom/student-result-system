import json
from pathlib import Path
from student import Student

DATA_FILE = Path(__file__).parent / "data" / "students.json"


def load_students():
    """Load student records. Return an empty list if no data file exists yet."""
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            records = json.load(file)
        return [Student.from_dict(item) for item in records]
    except (json.JSONDecodeError, KeyError, TypeError) as error:
        print(f"Warning: the data file could not be read: {error}")
        return []


def save_students(students):
    """Write all student records to the JSON data file."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump([student.to_dict() for student in students],
                  file, indent=4, ensure_ascii=False)
