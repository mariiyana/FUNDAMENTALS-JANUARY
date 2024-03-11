def tribonacci_sequence(number):
    sequence_list = [1, 0, 0]
    for digit in range(number):
        next_number = sum(sequence_list)
        print(next_number, end=" ")
        sequence_list.append(next_number)
        sequence_list.pop(0)


number = int(input())
tribonacci_sequence(number)
