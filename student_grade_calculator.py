"""A command-line student grade calculator."""


def get_mark(subject_number):
    """Return a valid mark from 0 to 100 for one subject."""
    while True:
        try:
            mark = float(input(f"Enter marks for subject {subject_number} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Please enter a mark from 0 to 100.")
        except ValueError:
            print("Please enter a valid number.")


def get_grade(percentage):
    """Convert a percentage to a letter grade."""
    if percentage >= 90:
        return "A+"
    if percentage >= 80:
        return "A"
    if percentage >= 70:
        return "B"
    if percentage >= 60:
        return "C"
    if percentage >= 50:
        return "D"
    return "F"


def calculate_result(marks):
    """Calculate total, percentage, grade, and pass/fail status."""
    total = sum(marks)
    percentage = total / len(marks)
    grade = get_grade(percentage)
    passed = percentage >= 50 and all(mark >= 35 for mark in marks)
    return total, percentage, grade, passed


def main():
    print("=== Student Grade Calculator ===")
    name = input("Enter student name: ").strip() or "Student"

    while True:
        try:
            subject_count = int(input("How many subjects? "))
            if subject_count > 0:
                break
            print("Please enter at least one subject.")
        except ValueError:
            print("Please enter a whole number.")

    marks = [get_mark(number) for number in range(1, subject_count + 1)]
    total, percentage, grade, passed = calculate_result(marks)

    print("\n--- Report Card ---")
    print(f"Student: {name}")
    print(f"Total: {total:.2f} / {subject_count * 100}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print(f"Result: {'Pass' if passed else 'Fail'}")


if __name__ == "__main__":
    main()
