def loading_bar(progress):
    num_progress = progress // 10
    target = 10

    if target == num_progress:
        return "100% Complete!\n" + "[" + target * "%" + "]"
    else:
        return f"{progress}% "+"[" + num_progress * "%" + (target - num_progress) * "." + "]\n" + "Still loading..."


number = int(input())
print(loading_bar(number))
