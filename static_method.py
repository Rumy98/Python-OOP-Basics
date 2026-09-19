class School:
    school_name="BSI"
    @staticmethod
    def calculate_grade(marks):
        if marks>=90:
            return "A+"
        elif marks>=50 and marks<=90:
            return "pass"
        else:
            return "F"

print(School.calculate_grade(89))