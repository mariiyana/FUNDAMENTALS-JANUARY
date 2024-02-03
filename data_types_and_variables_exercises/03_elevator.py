import math

number_of_people = int(input())
capacity_of_elevator = int(input())

total_courses = number_of_people / capacity_of_elevator

print(math.ceil(total_courses))
