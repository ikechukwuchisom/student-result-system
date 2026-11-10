from results import SUBJECTS


def student_report(student):
    lines = [
        "=" * 48,
        "             STUDENT REPORT CARD",
        "=" * 48,
        f"Student ID : {student.student_id}",
        f"Name       : {student.full_name}",
        f"Class      : {student.class_form}",
        f"Gender     : {student.gender}",
        f"Date of birth: {student.date_of_birth}",
        f"Result date: {student.result_date}",
        "-" * 48,
        "SUBJECT                         SCORE",
        "-" * 48,
    ]
    for subject in SUBJECTS:
        score = student.scores.get(subject)
        lines.append(f"{subject:<30} {score if score is not None else 'Not entered'}")
    lines.extend([
        "-" * 48,
        f"Total score : {student.total_score():.2f}",
        f"Average     : {student.average_score():.2f}%",
        f"Grade       : {student.grade()}",
        "=" * 48,
    ])
    return "\n".join(lines)


def class_report(students):
    lines = ["STUDENT RESULT SUMMARY", "-" * 72,
             f"{'ID':<12}{'NAME':<24}{'TOTAL':>10}{'AVERAGE':>12}{'GRADE':>10}",
             "-" * 72]
    for student in sorted(students, key=lambda item: item.average_score(), reverse=True):
        lines.append(
            f"{student.student_id:<12}{student.full_name[:22]:<24}"
            f"{student.total_score():>10.2f}{student.average_score():>12.2f}"
            f"{student.grade():>10}"
        )
    if students:
        averages = [student.average_score() for student in students]
        lines.extend([
            "-" * 72,
            f"Highest average: {max(averages):.2f}%",
            f"Lowest average : {min(averages):.2f}%",
            f"Class average  : {sum(averages) / len(averages):.2f}%",
        ])
    else:
        lines.append("No students have been registered.")
    return "\n".join(lines)


def save_text_report(content, filename="class_report.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    return filename
