numbers = list(map(int, input().split()))
removed_numbers = int(input())

for n in range(removed_numbers):
    numbers.remove(min(numbers))
result = ", ".join(map(str, numbers))
print(result)
