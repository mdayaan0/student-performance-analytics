# functions.py

def assign_grade(average):
    """Assigns a grade based on average marks."""
    if average >= 80:
        return 'A'
    elif average >= 60:
        return 'B'
    elif average >= 40:
        return 'C'
    else:
        return 'F'

def check_pass_fail(average):
    """Determines pass/fail status."""
    if average >= 40:
        return 'Pass'
    else:
        return 'Fail'