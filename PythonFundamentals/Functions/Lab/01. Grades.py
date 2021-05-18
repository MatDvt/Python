def calculate_grade_text(grd):
    if 2.00 <= grd <= 2.99:
        return "Fail"
    elif 3.00 <= grd <= 3.49:
        return "Poor"
    elif 3.50 <= grd <= 4.49:
        return "Good"
    elif 4.50 <= grd <= 5.49:
        return "Very Good"
    elif 5.50 <= grd <= 6.00:
        return "Excellent"


grade = float(input())
result = calculate_grade_text(grade)
print(result)
