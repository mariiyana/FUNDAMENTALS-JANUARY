number_of_snowballs = int(input())
max_weight = 0
max_time = 0
max_quality = 0
max_value = 0

for snow in range(number_of_snowballs):
    weight_of_snowball = int(input())
    needed_time = int(input())
    quality_of_snowball = int(input())
    snowball_value = (weight_of_snowball / needed_time) ** quality_of_snowball
    if snowball_value > max_value:
        max_value = snowball_value
        max_weight = weight_of_snowball
        max_time = needed_time
        max_quality = quality_of_snowball
print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")
