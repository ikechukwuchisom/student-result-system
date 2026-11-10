from dataclasses import dataclass, field
from datetime import date
from typing import Dict


@dataclass
class Student:
    """Stores one student's personal details and subject scores."""
    student_id: str
    full_name: str
    class_form: str
    gender: str
    date_of_birth: str
    scores: Dict[str, float] = field(default_factory=dict)
    result_date: str = ""

    def __post_init__(self):
        if not self.result_date:
            self.result_date = date.today().isoformat()

    def total_score(self) -> float:
        return sum(self.scores.values())

    def average_score(self) -> float:
        if not self.scores:
            return 0.0
        return self.total_score() / len(self.scores)

    def grade(self) -> str:
        average = self.average_score()
        if average >= 70:
            return "A"
        elif average >= 60:
            return "B"
        elif average >= 50:
            return "C"
        elif average >= 45:
            return "D"
        return "F"

    def to_dict(self) -> dict:
        return {
            "student_id": self.student_id,
            "full_name": self.full_name,
            "class_form": self.class_form,
            "gender": self.gender,
            "date_of_birth": self.date_of_birth,
            "scores": self.scores,
            "result_date": self.result_date,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            student_id=data["student_id"],
            full_name=data["full_name"],
            class_form=data["class_form"],
            gender=data["gender"],
            date_of_birth=data["date_of_birth"],
            scores=data.get("scores", {}),
            result_date=data.get("result_date", ""),
        )
