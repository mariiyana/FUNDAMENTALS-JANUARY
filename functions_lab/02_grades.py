def school(grades):

    if grades < 3:
        return "Fail"
    elif grades < 3.50:
        return "Poor"
    elif grades < 4.50:
        return "Good"
    elif grades < 5.50:
        return "Very Good"
    else:
        return "Excellent"


grade = float(input())
print(school(grade))


# Other way of solving the problem.
# #grade = float(input())
# grade_word = ''
#
# if grade < 3:
#     grade_word = "Fail"
# elif grade < 3.50:
#     grade_word = "Poor"
# elif grade < 4.50:
#     grade_word = "Good"
# elif grade < 5.50:
#     grade_word = "Very Good"
# else:
#     grade_word = "Excellent"
# print(grade_word)
