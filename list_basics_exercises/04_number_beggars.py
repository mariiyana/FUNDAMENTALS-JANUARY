string = list(map(int, input().split(", ")))
count_of_beggars = int(input())

beggars_sum = [0] * count_of_beggars

for beggar in range(len(string)):
    beggar_index = beggar % count_of_beggars
    beggars_sum[beggar_index] += string[beggar]

print(beggars_sum)
